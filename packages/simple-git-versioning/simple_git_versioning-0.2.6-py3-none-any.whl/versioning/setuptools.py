import logging
from io import TextIOWrapper
from pathlib import Path

try:
    import tomllib
except ImportError:
    import toml

from setuptools import Distribution
from versioning import pep440, semver2
from versioning.project import NotAGitWorkTree, NoVersion

LOGGER = logging.getLogger(__name__)


def finalize_distribution_options(distribution: Distribution) -> None:  # pragma: no cover
    if distribution.metadata.version is not None:
        LOGGER.debug(f"version is set already to: {distribution.metadata.version}")
        return

    try:
        with open("pyproject.toml", mode="rb") as stream:
            try:
                pyproject = tomllib.load(stream)
            except NameError:
                pyproject = toml.load(TextIOWrapper(stream))  # toml.load expects a TextIO
    except FileNotFoundError:
        LOGGER.debug("pyproject.toml not found: bailing out")
        return

    if (
        "project" not in pyproject
        or "dynamic" not in pyproject["project"]
        or "version" not in pyproject["project"]["dynamic"]
    ):
        LOGGER.debug("'version' is not set to be dynamic in pyproject.toml")
        return

    try:
        flavor = pyproject["tool"]["simple-git-versioning"]["setuptools"]
    except KeyError:
        LOGGER.debug("simple-git-versioning is not enabled")
        return

    if not isinstance(flavor, str):
        raise TypeError(
            "unexpected value for `tool.simple-git-versioning.setuptools`:"
            f" '{pyproject['tool']['simple-git-versioning']['setuptools']}', expected 'pep440' or 'semver2'"
        )

    flavor = flavor.casefold()
    if flavor == "pep440":
        Project = pep440.Project
        options = dict(dev=0)
    elif flavor == "semver2":
        Project = semver2.Project
        options = dict()
    else:
        raise ValueError(
            f"unexpected value for `tool.simple-git-versioning.setuptools`: '{flavor}', expected 'pep440' or 'semver2'"
        )

    if distribution.metadata.name is None:
        distribution.metadata.name = pyproject["project"]["name"]

    try:
        with Project(path=Path(".")) as proj:
            try:
                distribution.metadata.version = str(proj.version())
            except NoVersion:
                distribution.metadata.version = str(proj.release(**options))
    except NotAGitWorkTree:
        with open("PKG-INFO") as stream:
            for line in stream:
                key, value = line.split(": ", maxsplit=1)
                if key == "Version":
                    distribution.metadata.version = value
                    break
