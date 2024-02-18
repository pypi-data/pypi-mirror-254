"""
qBraid-CLI setup file

"""
import os

from setuptools import find_packages, setup


def read_version(file_path):
    """
    Extracts the version from a Python file containing a version variable.

    Args:
        file_path (str): Path to the Python file with the version variable.

    Returns:
        str: Version string, if found; otherwise, None.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return next(
            (
                line.split("=")[-1].strip().strip("\"'")
                for line in file
                if line.startswith("__version__")
            ),
            None,
        )


here = os.path.abspath(os.path.dirname(__file__))
version = read_version(os.path.join(here, "qbraid_cli", "_version.py"))

setup(
    name="qbraid-cli",
    version=version,
    license="Proprietary",
    description="Command Line Interface for interacting with all parts of the qBraid platform.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="qBraid Development Team",
    author_email="contact@qbraid.com",
    keywords="qbraid, cli, quantum, wrapper",
    url="https://www.qbraid.com/",
    project_urls={
        "Documentation": "https://docs.qbraid.com/projects/cli/en/latest/cli/qbraid.html",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">= 3.8",
    install_requires=["qbraid>=0.5.0", "ipykernel", "requests"],
    extras_require={
        "jobs": ["amazon-braket-sdk>=1.48.1", "awscli"],
        "dev": ["black", "isort", "pylint"],
        "docs": ["sphinx~=5.3.0", "sphinx-rtd-theme~=1.3.0", "docutils~=0.18.1"],
    },
    scripts=["qbraid_cli/bin/qbraid.sh"],
    entry_points={
        "console_scripts": [
            "qbraid=qbraid_cli.wrapper:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
