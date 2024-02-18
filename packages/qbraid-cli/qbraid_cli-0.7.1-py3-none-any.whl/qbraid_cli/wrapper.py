"""
Module to run the qbraid command line interface.

Lazy loading is used to avoid loading the qbraid package until it is needed.

"""

import os
import subprocess
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# pylint: disable=import-outside-toplevel


def flag_help_command():
    """Check if the help command should be triggered."""
    if len(sys.argv) > 0:
        last_arg = sys.argv[-1]
        if last_arg in ["-h", "--help", "help"]:
            return True
    return False


def is_help_command(arg_index):
    """Check if the help command should be triggered for the given argument index"""
    if flag_help_command() and arg_index == len(sys.argv) - 1:
        return True
    return False


def get_credits():
    """Get the number of credits available to the user."""
    from qbraid.api import QbraidSession

    session = QbraidSession()
    res = session.get("/billing/credits/get-user-credits").json()
    qbraid_credits = res["qbraidCredits"]
    print(qbraid_credits)


def main():
    """The subprocess.run function is used to run the script and pass arguments."""
    if len(sys.argv) == 2 and sys.argv[1] == "configure":
        from .configure import configure

        configure()
    if len(sys.argv) == 5 and sys.argv[1:3] == ["configure", "set"]:
        from .configure import configure_set

        configure_set(sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 2 and sys.argv[1] == "credits":
        get_credits()
    elif sys.argv[1:] == ["--version"] or sys.argv[1:] == ["-V"]:
        from ._version import __version__

        print(f"qbraid-cli/{__version__}")
    elif len(sys.argv) == 3 and sys.argv[1:] == ["jobs", "list"]:
        from qbraid import get_jobs

        get_jobs()
    elif len(sys.argv) == 3 and sys.argv[1:] == ["devices", "list"]:
        from qbraid import get_devices

        get_devices()
    elif (
        len(sys.argv) == 5
        and sys.argv[1:3] == ["envs", "create"]
        and sys.argv[3] in ["-n", "--name"]
    ):
        from .envs import create

        create(sys.argv[4])
    else:
        result = subprocess.run(
            [os.path.join(PROJECT_ROOT, "bin", "qbraid.sh")] + sys.argv[1:],
            text=True,
            capture_output=True,
            check=False,
        )

        if result.stdout:
            if len(sys.argv) == 4 and sys.argv[2] == "activate":
                line_lst = result.stdout.split("\n")
                line_lst = line_lst[:-1]  # remove trailing blank line
                bin_path = line_lst.pop()  # last line contains bin_path
                std_out = "\n".join(line_lst)  # all other lines are regular stdout
                print(std_out)
                # activate python environment using bin_path
                os.system(
                    f"cat ~/.bashrc {bin_path}/activate > {bin_path}/activate2 && "
                    rf"sed -i 's/echo -e/\# echo -e/' {bin_path}/activate2 && "
                    f"/bin/bash --rcfile {bin_path}/activate2"
                )
            else:
                print(result.stdout)
        if result.stderr:
            print(result.stderr)


if __name__ == "__main__":
    main()
