"""
Module containing functions to enable/disable quantum jobs.

"""

import os
import site
import subprocess
import sys
import threading
from importlib.metadata import PackageNotFoundError, version

import requests

from ._display import print_progress_linear
from .exceptions import QuantumJobsException


def get_latest_boto3_version() -> str:
    """Retrieves the latest version of botocore from PyPI."""
    url = "https://pypi.org/pypi/boto3/json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except requests.RequestException as err:
        raise QuantumJobsException("Failed to retrieve latest boto3 version.") from err


def get_local_boto3_version() -> str:
    """Retrieves the local version of boto3."""
    try:
        return version("boto3")
    except PackageNotFoundError as err:
        raise QuantumJobsException(
            "boto3 is not installed in the current environment."
        ) from err


def get_target_site_packages_path() -> str:
    """Retrieves the site-packages path of the current Python environment."""

    # List of all site-packages directories
    site_packages_paths = site.getsitepackages()

    if len(site_packages_paths) == 1:
        return site_packages_paths[0]

    # Path to the currently running Python interpreter
    python_executable_path = sys.executable

    # Base path of the Python environment
    env_base_path = os.path.dirname(os.path.dirname(python_executable_path))

    # Find the site-packages path that is within the same environment
    for path in site_packages_paths:
        if env_base_path in path:
            return path

    raise QuantumJobsException("Failed to find site-packages path.")


def get_local_boto3_path() -> str:
    """Retrieves the local path of boto3."""
    try:
        site_packages_path = get_target_site_packages_path()
        return os.path.join(site_packages_path, "boto3")
    except PackageNotFoundError as err:
        raise QuantumJobsException(
            "boto3 is not installed in the current environment."
        ) from err


def verify_boto3_compatible() -> None:
    """Verifies that the local version of boto3 is compatible with qBraid Quantum Jobs."""
    stop_event = threading.Event()
    message = "Collecting package metadata..."
    interval = 0.1

    # Start the progress bar in a separate thread
    progress_thread = threading.Thread(
        target=print_progress_linear,
        args=(
            stop_event,
            message,
            interval,
        ),
    )
    progress_thread.start()

    installed_version = get_local_boto3_version()
    latest_version = get_latest_boto3_version()

    installed_major, intalled_minor, _ = installed_version.split(".")
    latest_major, latest_minor, _ = latest_version.split(".")

    # Signal the progress thread to stop
    stop_event.set()
    progress_thread.join()

    if installed_major == latest_major and intalled_minor == latest_minor:
        return None

    boto3_location = get_local_boto3_path()

    print("==> WARNING: A newer version of boto3 exists. <==")
    print(f"  current version: {installed_version}")
    print(f"  latest version: {latest_version}\n\n")
    print(
        "Enabling quantum jobs will automatically update boto3, "
        "which may cause incompatibilities with the amazon-braket-sdk and/or awscli.\n\n"
    )
    print("## Package Plan ##\n")
    print(f"  boto3 location: {boto3_location}\n\n")
    user_input = input("Proceed ([y]/n)? ")

    if user_input.lower() in ["n", "no"]:
        print("\nqBraidSystemExit: Exiting.")
        sys.exit()

    print("")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade", "boto3"]
    )
    print("")

    return None


def manage_package(action, package, exception_message) -> None:
    """Generic function to install or uninstall packages.

    Args:
        action (str): 'install' or 'uninstall'
        package (str): The package to install or uninstall
        exception_message (str): Error message to raise in case of exception

    Returns:
        None

    Raises:
        QuantumJobsException: If the action fails.
    """
    try:
        if action == "uninstall":
            subprocess.check_call(
                [sys.executable, "-m", "pip", "uninstall", package, "-y", "--quiet"]
            )
        elif action == "install":
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", package, "--quiet"]
            )
    except subprocess.CalledProcessError as err:
        raise QuantumJobsException(exception_message) from err


def enable_quantum_jobs() -> None:
    """Enables qBraid quantum jobs."""
    try:
        verify_boto3_compatible()
        stop_event = threading.Event()
        message = "Installing qBraid botocore..."
        interval = 1.5

        # Start the progress bar in a separate thread
        progress_thread = threading.Thread(
            target=print_progress_linear,
            args=(
                stop_event,
                message,
                interval,
            ),
        )
        progress_thread.start()
        manage_package(
            "uninstall",
            "botocore",
            "Failed to install qBraid botocore.",
        )
        manage_package(
            "install",
            "git+https://github.com/qBraid/botocore.git",
            "Failed to install qBraid botocore.",
        )
        stop_event.set()
        progress_thread.join()
    except Exception as err:
        stop_event.set()
        progress_thread.join()
        raise QuantumJobsException("Failed to enable qBraid quantum jobs.") from err

    print("\nSuccessfully enabled qBraid quantum jobs.\n")


def disable_quantum_jobs() -> None:
    """Disables qBraid quantum jobs."""
    try:
        stop_event = threading.Event()
        message = "Uninstalling qBraid botocore..."
        interval = 0.5

        # Start the progress bar in a separate thread
        progress_thread = threading.Thread(
            target=print_progress_linear,
            args=(
                stop_event,
                message,
                interval,
            ),
        )
        progress_thread.start()
        manage_package(
            "uninstall",
            "botocore",
            "Failed to uninstall qBraid botocore.",
        )
        manage_package("install", "botocore", "Failed to reinstall original boto3.")
        stop_event.set()
        progress_thread.join()
    except Exception as err:
        stop_event.set()
        progress_thread.join()
        raise QuantumJobsException("Failed to disable qBraid quantum jobs.") from err

    print("\nSuccessfully disabled qBraid quantum jobs.\n")
