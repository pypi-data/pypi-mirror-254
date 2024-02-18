"""
Module for utility functions used in displaying data to user

"""

import sys
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import threading


def print_progress_linear(
    stop_event: "threading.Event", message: str, interval: float
) -> None:
    """Prints progressing dots on the same line to indicate a process is running."""
    sys.stdout.write(message)
    while not stop_event.is_set():
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write(" done.\n\n")


def print_progress_cycle(
    stop_event: "threading.Event", message: str, interval: float
) -> None:
    """Prints progressing dots on the same line to indicate a process is running,
    cycling from 1 to 4 dots and resetting to 0. Ends with exactly four dots before 'done'.
    """
    dot_count = 0

    while not stop_event.is_set():
        sys.stdout.write("\r" + message + "." * dot_count)
        sys.stdout.flush()
        dot_count = (dot_count + 1) % 5
        if dot_count == 0:
            sys.stdout.write("\r" + message + "    ")
            sys.stdout.flush()
            dot_count = 1
        time.sleep(interval)

    sys.stdout.write("\r" + message + "...." + " done.\n\n")
