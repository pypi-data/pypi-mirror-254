Opinionated version numbering CLIs, and library

--------------------------------------------------------------------------------

This project aims at easing the burden of computing and managing a project's
version numbers by leveraging `git` tags and commit trailers.

`simple-git-versioning` provides two CLIs: `semver2` and `pep440`, one for each
supported versioning sheme of the same name: [`SemVer2`](https://semver.org) and 
[`PEP440`](https://peps.python.org/pep-0440/).

Integration with [`setuptools`](#setuptools) is supported.

Snippets to expose your project's version number programatically are provided in
the [`Libraries`](#libraries) section.

# Installation

With `pip`:

```python
pip install simple-git-versioning
```

# Usage

By default, `pep440` and `semver2` will compute a version number of the form
`X.Y.Z`. Every project starts at `0.0.0` on their initial commit, and each
commit after that increments the number `Z` by one, unless they include a
`Version-Bump` trailer (case-insensitive) with a value of:
- `major`: `X` is incremented;
- `minor`: `Y` is incremented;
- `patch`: `Z` is incremented (same as the default).

Each tool then provides the ability to _switch_ to a pre-release mode; or
post-release, and/or dev release, etc. in the case of `pep440`.

## CLIs

All CLIs provide comprehensive help messages, available via the `--help` option.

## Libraries

Libraries that wish to expose their version number programatically may do so by
including the following snippet:

### `PEP440`

```python
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from versioning.pep440 import NoVersion, Project

try:
    __version__ = version("<your python package's name>")
except PackageNotFoundError:
    # package is not installed
    with Project(path=Path(__file__).parent) as project:
        try:
            __version__ = str(project.version())
        except NoVersion:
            __version__ = str(project.release(dev=0))
```

### `SemVer2`

```python
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path

from versioning.semver2 import NoVersion, Project

try:
    __version__ = version("<your python package's name>")
except PackageNotFoundError:
    # package is not installed
    with Project(path=Path(__file__).parent) as project:
        try:
            __version__ = str(project.version())
        except NoVersion:
            __version__ = str(project.release(pre=("dev", 0))
```

## `poetry`

If you use `poetry` as a build frontend and backend for your project, you can
configure `simple-git-versioning` to derive a version automatically as follows:

Install `simple-git-versioning` alongside `poetry`:

```bash
poetry self add "simple-git-versioning>=0.2"
```

Enable the `poetry` integration in your `pyproject.toml`, and pick the
versioning scheme you wish to apply:

```toml
[tool.poetry]
...

[tool.simple-git-versioning]
poetry = "pep440"  # or "semver2"
```

> Note that `poetry` mandates a `version` always be set in `pyproject.toml`, so
> you will have to keep a placeholder there (e.g. `version: "0.0.0"`).

## `setuptools`

If you use `setuptools` as a build backend for your project, you can configure
`simple-git-versioning` to derive a version automatically as follows:

In your `pyproject.toml`:
  - declare `version` as a dynamic metadata field;
  - add `simple-git-versioning` to your project's `build-system.requires`;
  - enable the `setuptools` integration in your `pyproject.toml`, and pick the
    versioning scheme you wish to apply.

```toml
[project]
name = ...
dynamic = ["version"]

[build-system]
requires = ["setuptools>=63", "simple-git-versioning"]
build-backend = "setuptools.build_meta"

[tool.simple-git-versioning]
setuptools = "pep440"  # or "semver2"
```

> I recommend checking out [`setuptools-scm`](https://pypi.org/project/setuptools-scm/)
  and [`setuptools-pipfile`](https://pypi.org/project/setuptools-pipfile/), two
  other `setuptools` extensions I find greatly helpful.
