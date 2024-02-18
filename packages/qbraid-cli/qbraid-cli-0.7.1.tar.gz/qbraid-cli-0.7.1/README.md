<img width="full" alt="qbraid_cli" src="https://qbraid-static.s3.amazonaws.com/logos/qbraid-cli-banner.png">

[![Documentation](https://img.shields.io/badge/Documentation-DF0982)](https://docs.qbraid.com/projects/cli/en/latest/cli/qbraid.html)
[![PyPI version](https://img.shields.io/pypi/v/qbraid-cli.svg?color=blue)](https://pypi.org/project/qbraid-cli/)
[![Discord](https://img.shields.io/discord/771898982564626445.svg?color=pink)](https://discord.gg/TPBU2sa8Et)

Command Line Interface for interacting with all parts of the qBraid platform.

The **qBraid CLI** is a specialized command-line interface tool designed *exclusively* for use within the [qBraid Lab](https://docs.qbraid.com/projects/lab/en/latest/lab/overview.html) platform. It is not intended for local installations or use outside the qBraid Lab environment. This tool ensures seamless integration and optimized performance specifically tailored for qBraid Lab's unique cloud-based quantum computing ecosystem.


## Getting Started

To use the qBraid CLI, login to qBraid (or create an account), launch Lab, and then open Terminal. You can also access the CLI directly from within [Notebooks](https://docs.qbraid.com/projects/lab/en/latest/lab/notebooks.html) using the ``!`` operator. See [quantum jobs example](https://github.com/qBraid/qbraid-lab-demo/blob/045c7a8fbdcae66a7e64533dd9fe0e981dc02cf4/qbraid_lab/quantum_jobs/aws_quantum_jobs.ipynb).

- [Launch qBraid Lab &rarr;](https://lab.qbraid.com/)
- [Make an account &rarr;](https://account.qbraid.com/)

For help, see qBraid Lab User Guide: [Getting Started](https://docs.qbraid.com/projects/lab/en/latest/lab/getting_started.html).

## Basic Commands

```bash
$ qbraid
-------------------------------
* Welcome to the qBraid CLI! *
-------------------------------

  - Use `qbraid -h` to see available commands.

  - Use `qbraid --version` to display the current version.

Reference Docs: https://docs.qbraid.com/projects/cli/en/latest/cli/qbraid.html
```

A qBraid CLI command has the following structure:

```bash
$ qbraid <command> <subcommand> [options and parameters]
```

For example, to list installed environments, the command would be:

```bash
$ qbraid envs list
```

To view help documentation, use one of the following:

```bash
$ qbraid help
$ qbraid <command> help
$ qbraid <command> <subcommand> help
```

For example:

```bash
$ qbraid help

Group
    qbraid

Subgroups
    envs             : Manage qBraid environments.
    kernels          : Manage qBraid kernels.
    jobs             : Manage qBraid Quantum Jobs.

Arguments
    -V, --version    : Show version and exit

Global Arguments
    -h, --help       : Show this help message and exit.

Reference Docs: https://docs.qbraid.com/en/latest/cli/qbraid.html
```

To get the version of the qBraid CLI:

```bash
$ qbraid --version
```
