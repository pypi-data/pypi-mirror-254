# -*- coding: utf-8 -*-

#  Copyright © 2024. anonymous.

# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License  along with this
# program. If not, see <https://www.gnu.org/licenses/>.
"""Classes and function to retrieve Python specific information."""

from platform import (
    python_build,
    python_compiler,
    python_branch,
    python_implementation,
    python_revision,
    python_version,
    python_version_tuple,
)


class PythonInformation:
    """A class that wraps python information retrieved using the platform module."""

    @property
    def build(self) -> tuple[str, str]:
        """Returns a tuple (buildno, builddate) stating the Python build number and date
        as strings.

        :return: (buildno, builddate)
        :rtype: tuple[str, str]
        """
        return python_build()

    @property
    def compiler(self) -> str:
        """Returns a string identifying the compiler used for compiling Python.

        :return: the compiler used for compiling Python
        :rtype: str
        """
        return python_compiler()

    @property
    def branch(self) -> str:
        """Returns a string identifying the Python implementation SCM branch.

        :return: the Python implementation SCM branch
        :rtype: str
        """
        return python_branch()

    @property
    def implementation(self) -> str:
        """Returns a string identifying the Python implementation. Possible return
        values are:

        ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.

        :return: the Python implementation
        :rtype: str
        """
        return python_implementation()

    @property
    def revision(self) -> str:
        """Returns a string identifying the Python implementation SCM revision.

        :return: the Python implementation SCM revision
        :rtype: str
        """
        return python_revision()

    @property
    def version(self) -> str:
        """Returns the Python version as string 'major.minor.patch'.

        Note that unlike the Python sys.version, the returned value will always include
        the patch (it defaults to 0).

        :return: the Python version
        :rtype: str
        """
        return python_version()

    @property
    def version_tuple(self) -> tuple[str, str, str]:
        """Returns the Python version as tuple (major, minor, patch) of strings.

        Note that unlike the Python sys.version, the returned value will always include
        the patchlevel (it defaults to '0').

        :return: (major, minor, patch)
        :rtype: tuple[str, str, str]
        """
        return python_version_tuple()
