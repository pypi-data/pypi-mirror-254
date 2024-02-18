"""
Module for interfacing with qBraid environments.

"""

import json
import os
import shutil
import subprocess
import sys
import threading
from typing import List, Optional

from jupyter_client.kernelspec import KernelSpecManager
from qbraid.api import QbraidSession

from ._display import print_progress_cycle

DEFAULT_VISIBILITY = "private"

DEFAULT_ENVS_PATH = os.path.join(os.path.expanduser("~"), ".qbraid", "environments")
QBRAID_ENVS_PATH = os.getenv("QBRAID_USR_ENVS", DEFAULT_ENVS_PATH)


def create_alias(slug: str) -> str:
    """Create an alias from a slug."""
    return slug[:-7].replace("_", "-").strip("-")


def replace_str(target: str, replacement: str, file_path: str) -> None:
    """Replace all instances of string in file"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.replace(target, replacement)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def update_install_status(
    slug_path: str, complete: int, success: int, message: Optional[str] = None
) -> None:
    """Update environment's install status values in a JSON file.
    Truth table values: 0 = False, 1 = True, -1 = Unknown
    """
    # Set default message if none provided
    message = "" if message is None else message.replace("\n", " ")

    # File path for state.json
    state_json_path = os.path.join(slug_path, "state.json")

    # Read existing data or use default structure
    if os.path.exists(state_json_path):
        with open(state_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"install": {}}

    # Update the data
    data["install"]["complete"] = complete
    data["install"]["success"] = success
    data["install"]["message"] = message

    # Write updated data back to state.json
    with open(state_json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def create_venv(slug_path: str, prompt: str) -> None:
    """Create virtual environment and swap PS1 display name."""
    venv_path = os.path.join(slug_path, "pyenv")
    subprocess.run([sys.executable, "-m", "venv", venv_path], check=True)

    bin_path = os.path.join(venv_path, "bin")
    activate_files = ["activate", "activate.csh", "activate.fish"]

    for file in activate_files:
        file_path = os.path.join(bin_path, file)
        replace_str("(pyenv)", f"({prompt})", file_path)

    replace_str(
        "include-system-site-packages = false",
        "include-system-site-packages = true",
        os.path.join(venv_path, "pyvenv.cfg"),
    )

    update_install_status(slug_path, 1, 1)


def create_qbraid_env(slug: str, prompt: str, display_name: str) -> None:
    """Create a qBraid environment including python venv, PS1 configs,
    kernel resource files, and qBraid state.json."""
    slug_path = os.path.join(QBRAID_ENVS_PATH, slug)
    local_resource_dir = os.path.join(slug_path, "kernels", f"python3_{slug}")
    os.makedirs(local_resource_dir, exist_ok=True)

    # create state.json
    update_install_status(slug_path, 0, 0)

    # create kernel.json
    kernel_json_path = os.path.join(local_resource_dir, "kernel.json")
    kernel_spec_manager = KernelSpecManager()
    kernelspec_dict = kernel_spec_manager.get_all_specs()
    kernel_data = kernelspec_dict["python3"]["spec"]
    kernel_data["argv"][0] = os.path.join(slug_path, "pyenv", "bin", "python")
    kernel_data["display_name"] = display_name
    with open(kernel_json_path, "w", encoding="utf-8") as file:
        json.dump(kernel_data, file, indent=4)

    # copy logo files
    sys_resource_dir = kernelspec_dict["python3"]["resource_dir"]
    logo_files = ["logo-32x32.png", "logo-64x64.png", "logo-svg.svg"]

    for file in logo_files:
        sys_path = os.path.join(sys_resource_dir, file)
        loc_path = os.path.join(local_resource_dir, file)
        if os.path.isfile(sys_path):
            shutil.copy(sys_path, loc_path)

    # create python venv
    create_venv(slug_path, prompt)


# pylint: disable-next=too-many-arguments,too-many-locals
def create(
    name: str,
    description: Optional[str] = None,
    tags: Optional[List[str]] = None,
    code: Optional[str] = None,
    visibility: Optional[str] = None,
    kernel_name: Optional[str] = None,
    prompt: Optional[str] = None,
) -> None:
    """
    Create a new qBraid environment.

    Args:
        name (str): Name of the environment.
        description (Optional[str]): Description of the environment.
        tags (Optional[List[str]]): List of tags associated with the environment.
        code (Optional[str]): package list in requirements.txt format.
        visibility (Optional[str]): Visibility status (e.g., 'private').
        kernel_name (Optional[str]): Name of the kernel.
        prompt (Optional[str]): Prompt for the environment.

    Returns:
        None
    """
    req_body = {
        "name": name,
        "description": description or "",
        "tags": tags or "",  # comma separated list of tags
        "code": code or "",  # newline separated list of packages
        "visibility": visibility or DEFAULT_VISIBILITY,
        "kernelName": kernel_name or "",
        "prompt": prompt or "",
    }

    session = QbraidSession()

    try:
        resp = session.post("/environments/create", json=req_body).json()
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Failed to create environment: {e}")
        return

    slug = resp.get("slug")
    if slug is None:
        print("Failed to create environment: no slug returned")
        return

    alias = create_alias(slug)
    kernel_name = kernel_name if kernel_name else f"Python 3 [{alias}]"
    prompt = prompt if prompt else alias

    stop_event = threading.Event()
    message = "Creating qBraid environment"
    interval = 0.5

    # Start the progress bar in a separate thread
    progress_thread = threading.Thread(
        target=print_progress_cycle,
        args=(
            stop_event,
            message,
            interval,
        ),
    )
    progress_thread.start()
    create_qbraid_env(slug, prompt, kernel_name)
    stop_event.set()
    progress_thread.join()

    print(f"\nSuccessfully created qBraid environment: {slug}\n")
