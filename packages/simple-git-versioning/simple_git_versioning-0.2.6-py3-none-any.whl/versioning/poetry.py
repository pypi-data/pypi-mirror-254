from __future__ import annotations

from typing import TYPE_CHECKING

from versioning import pep440, semver2
from versioning.project import NoVersion

if TYPE_CHECKING:
    from cleo.io.io import IO

    from poetry.poetry import Poetry

try:
    from cleo.io.outputs.output import Verbosity

    from poetry.plugins.plugin import Plugin
except ImportError:
    pass
else:

    class SimpleGitVersioning(Plugin):  # pragma: no cover
        def activate(self, poetry: Poetry, io: IO):
            try:
                flavor = poetry.pyproject.data["tool"]["simple-git-versioning"]["poetry"]
            except KeyError:
                io.write_line("simple-git-versioning is not enabled", verbosity=Verbosity.DEBUG)
                return

            if not isinstance(flavor, str):
                raise TypeError(
                    "unexpected value for `tool.simple-git-versioning.poetry`:"
                    f" '{poetry.pyproject.data['tool']['simple-git-versioning']['poetry']}', expected 'pep440' or"
                    " 'semver2'"
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
                    f"unexpected value for `tool.simple-git-versioning.poetry`: '{flavor}', expected 'pep440' or"
                    " 'semver2'"
                )

            with Project(path=poetry.pyproject.path.parent) as proj:
                try:
                    poetry.package._set_version(str(proj.version()))
                except NoVersion:
                    poetry.package._set_version(str(proj.release(**options)))
