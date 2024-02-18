import time
from concurrent.futures import Future, ThreadPoolExecutor
from pathlib import Path
from typing import Callable, List
from urllib.parse import urlparse

import fsspec
import requests
from fsspec.implementations.dirfs import DirFileSystem
from loguru import logger

from fused._global_api import get_api
from fused._options import options as OPTIONS


def filesystem(protocol: str, **storage_options) -> fsspec.AbstractFileSystem:
    """Get an fsspec filesystem for the given protocol.

    Args:
        protocol: Protocol part of the URL, such as "s3" or "gs".
        storage_options: Additional arguments to pass to the storage backend.

    Returns:
        An fsspec AbstractFileSystem.
    """
    if protocol == "fd":
        # fused team directory
        api = get_api()
        if hasattr(api, "_resolve"):
            root = api._resolve("fd://")
            root_parsed = urlparse(root)
            return DirFileSystem(
                path=root, fs=fsspec.filesystem(root_parsed.scheme, **storage_options)
            )
        else:
            raise ValueError("Could not determine root of Fused team directory")
    return fsspec.filesystem(protocol, **storage_options)


def fused_path(file_path: str, mkdir: bool = True) -> str:
    """Create a path in the job's temporary directory

    Args:
        file_path: The file path to locate.
        mkdir: If True, create the directory if it doesn't already exist. Defaults to True.

    Returns:
        The located file path.
    """
    # TODO: Move this onto the context object
    # TODO: Return Path objects rather than converting to str
    global_path = str(Path("/tmp/fused")) + "/"

    tmp = file_path.split("/")
    if tmp[-1].rfind(".") < 0:
        folder = Path(global_path + "/" + file_path)
    else:
        folder = Path(global_path + "/" + "/".join(tmp[:-1]))
    if mkdir:
        folder.mkdir(parents=True, exist_ok=True)
    return str(Path(global_path + "/" + file_path))


def _download_requests(url: str) -> bytes:
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def _download_signed(url: str) -> bytes:
    api = get_api()
    return _download_requests(api.sign_url(url))


def download(url: str, file_path: str) -> str:
    """Download a file.

    May be called from multiple processes with the same inputs to get the same result.

    Args:
        url: The URL to download.
        file_path: The local path where to save the file.

    Returns:
        The string of the local path.
    """
    path = fused_path(file_path)

    def _download():
        parsed_url = urlparse(url)
        logger.debug(f"Downloading {url} -> {path}")

        if parsed_url.scheme in ["s3", "gs"]:
            content = _download_signed(url)
        else:
            if parsed_url.scheme not in ["http", "https"]:
                logger.debug(f"Unexpected URL scheme {parsed_url.scheme}")
            content = _download_requests(url)

        with open(path, "wb") as file:
            file.write(content)

    _run_once(signal_name=file_path, fn=_download)

    return path


def download_folder(url: str, file_path: str) -> str:
    """Download a folder.

    May be called from multiple processes with the same inputs to get the same result.

    Args:
        url: The URL to download.
        file_path: The local path where to save the files.

    Returns:
        The string of the local path.
    """
    path = fused_path(file_path)

    if not url.endswith("/"):
        url = f"{url}/"

    def _download():
        parsed_url = urlparse(url)
        logger.debug(f"Downloading {url} -> {path}")

        if parsed_url.scheme in ["s3", "gs"]:
            api = get_api()
            all_files = api.sign_url_prefix(url)

            root_path = Path(path)
            to_remove = parsed_url.path.lstrip("/")

            def _download_single_file(filename: str, signed_url: str) -> None:
                logger.debug(f"Downloading {filename}...")
                content = _download_requests(signed_url)

                curr_path = root_path / Path(filename)
                curr_path.parent.mkdir(parents=True, exist_ok=True)

                with open(curr_path, "wb") as file:
                    file.write(content)

            with ThreadPoolExecutor(max_workers=OPTIONS.max_workers) as pool:
                futures: List[Future] = []
                for filename, signed_url in all_files.items():
                    if filename.startswith(to_remove):
                        filename = filename[len(to_remove) :]

                    futures.append(
                        pool.submit(
                            _download_single_file,
                            filename=filename,
                            signed_url=signed_url,
                        )
                    )
                pool.shutdown(wait=True)
        else:
            raise NotImplementedError(f"Unexpected URL scheme {parsed_url.scheme}")

    _run_once(signal_name=file_path, fn=_download)

    return path


def _run_once(signal_name: str, fn: Callable) -> None:
    """Run a function once, waiting for another process to run it if in progress.

    Args:
        signal_key: A relative key for signalling done status. Files are written using `fused_path` and this key to deduplicate runs.
        fn: A function that will be run once.
    """
    path_in_progress = Path(fused_path(signal_name + ".in_progress"))
    path_done = Path(fused_path(signal_name + ".done"))
    path_error = Path(fused_path(signal_name + ".error"))

    def _wait_for_file_done():
        logger.debug(f"Waiting for {signal_name}")
        while not path_done.exists() and not path_error.exists():
            time.sleep(1)
        if path_error.exists():
            raise ValueError(f"{signal_name} failed in another chunk")
        logger.info(f"already cached ({signal_name}).")

    if path_in_progress.is_file():
        _wait_for_file_done()
    else:
        try:
            with open(path_in_progress, "x") as file:
                file.write("requesting")
        except FileExistsError:
            _wait_for_file_done()
            return
        logger.debug(f"Running fn -> {signal_name}")

        try:
            fn()
        except:
            with open(path_error, "w") as file:
                file.write("done")
            raise

        with open(path_done, "w") as file:
            file.write("done")
        logger.info(f"waited successfully ({signal_name}).")
