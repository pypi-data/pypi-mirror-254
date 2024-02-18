"""
Module defining exceptions raised by the qBraid CLI.

"""


class QbraidCLIException(Exception):
    """Base class for exceptions raised by the qBraid CLI."""


class QuantumJobsException(QbraidCLIException):
    """Class for exceptions raised by qBraid Quantum Jobs."""
