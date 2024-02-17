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
"""Classes and functions to retrieve platform specific information."""

import sys

from platform import (
    system,
    system_alias,
    architecture,
    machine,
    platform,
    release,
    version,
    uname_result,
    uname,
    java_ver,
    win32_ver,
    win32_edition,
    win32_is_iot,
    mac_ver,
    libc_ver,
    freedesktop_os_release,
)

from this_system.python import PythonInformation
from this_system.browser import detect_installed_browsers, Browser


class PlatformInformation:
    """A class that wraps platform specific information."""

    @property
    def system(self) -> str:
        """Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'. An
        empty string is returned if the value cannot be determined.

        :return: the system/OS name
        :rtype: str
        """
        return system()

    @property
    def system_alias(self) -> tuple[str, str, str]:
        """Returns (system, release, version) aliased to common marketing names used for
        some systems. It also does some reordering of the information in some cases
        where it would otherwise cause confusion.

        :return: (system, release, version) aliased to common marketing names
        :rtype: tuple[str, str, str]
        """
        # platform.version(),
        return system_alias(
            system=self.system, release=self.release, version=self.version
        )

    def architecture(
        self, executable: str = sys.executable, bits: str = "", linkage: str = ""
    ) -> tuple[str, str]:
        """Queries the given executable (defaults to the Python interpreter binary) for
        various architecture information.

        Queries the given executable (defaults to the Python interpreter binary) for
        various architecture information.

        Returns a tuple (bits, linkage) which contain information about the bit
        architecture and the linkage format used for the executable. Both values are
        returned as strings.

        Values that cannot be determined are returned as given by the parameter presets.
        If bits is given as '', the sizeof(pointer) (or sizeof(long) on Python version <
        1.5.2) is used as indicator for the supported pointer size.

        The function relies on the system’s file command to do the actual work. This is
        available on most if not all Unix platforms and some non-Unix platforms and then
        only if the executable points to the Python interpreter. Reasonable defaults are
        used when the above needs are not met.

        Note:

        On macOS (and perhaps other platforms), executable files may be universal files
        containing multiple architectures. To get at the “64-bitness” of the current
        interpreter, it is more reliable to query the sys.maxsize attribute:

        is_64bits = sys.maxsize > 2**32

        :param executable: the executable to be queried
        :type executable: str
        :param bits:
        :type bits: str
        :param linkage:
        :type linkage: str
        :return:
        :rtype: tuple[str, str]
        """
        return architecture(executable=executable, bits=bits, linkage=linkage)

    @property
    def machine(self) -> str:
        """Returns the machine type, e.g. 'AMD64'. An empty string is returned if the
        value cannot be determined.

        :return: the machine type
        :rtype: str
        """
        return machine()

    def platform(self, aliased=False, terse=False) -> str:
        """Returns a single string identifying the underlying platform with as much
        useful information as possible.

        The output is intended to be human-readable rather than machine parseable. It
        may look different on different platforms and this is intended.

        :param aliased: If aliased is true, the function will use aliases for various
            platforms that report system names which differ from their common names
        :type aliased: bool
        :param terse: Setting terse to true causes the function to return only the
            absolute minimum information needed to identify the platform.
        :type terse: bool
        :return: a human-readable string identifying the underlying platform
        :rtype: str
        """
        return platform(aliased=aliased, terse=terse)

    @property
    def python(self) -> PythonInformation:
        """Python specific information.

        :return: a Python object
        :rtype: PythonInfo
        """
        return PythonInformation()

    @property
    def release(self) -> str:
        """Returns the system’s release, e.g. '2.2.0' or 'NT'. An empty string is
        returned if the value cannot be determined.

        :return: the system’s release
        :rtype: str
        """
        return release()

    @property
    def version(self) -> str:
        """Returns the system’s release version, e.g. '#3 on degas'. An empty string is
        returned if the value cannot be determined.

        :return: the system’s release version
        :rtype: str
        """
        return version()

    @property
    def uname(self) -> uname_result:
        """Returns a namedtuple() containing six attributes:

        system node release version machine processor

        processor is resolved late, on demand.

        Note: the first two attribute names differ from the names presented by
        os.uname(), where they are named sysname and nodename.

        Entries which cannot be determined are set to ''.

        :return: Fairly portable uname interface.
        :rtype: uname_result
        """
        return uname()

    @property
    def jython(self) -> tuple[str, str, tuple[str, str, str], tuple[str, str, str]]:
        """Version interface for Jython.

        Returns a tuple (release, vendor, vminfo, osinfo) with

        vminfo being a tuple (vm_name, vm_release, vm_vendor)

        and

        osinfo being a tuple (os_name, os_version, os_arch).

        Values which cannot be determined are set to the defaults given as parameters
        (which all default to '').

        :return: (release, vendor, vminfo, osinfo)
        :rtype: tuple[str, str, tuple[str, str, str], tuple[str, str, str]]
        """
        return java_ver(release="", vendor="", vminfo=("", "", ""), osinfo=("", "", ""))

    @property
    def win32_ver(self) -> tuple[str, str, str, str]:
        """Get additional version information from the Windows Registry and return a
        tuple (release, version, csd, ptype) referring to OS release, version number,
        CSD level (service pack) and OS type (multi/single processor).

        Values which cannot be determined are set to the defaults given as parameters
        (which all default to an empty string).

        As a hint:

        ptype is 'Uniprocessor Free' on single processor NT machines 'Multiprocessor
        Free' on multiprocessor machines.

        The ‘Free’ refers to the OS version being free of debugging code. It could also
        state ‘Checked’ which means the OS version uses debugging code, i.e. code that
        checks arguments, ranges, etc.

        :return: additional version information from the Windows Registry
        :rtype: tuple[str, str, str, str]
        """
        return win32_ver(release="", version="", csd="", ptype="")

    @property
    def win32_edition(self) -> str:
        """Returns a string representing the current Windows edition, or None if the
        value cannot be determined. Possible values include but are not limited to
        'Enterprise', 'IoTUAP', 'ServerStandard', and 'nanoserver'.

        :return: the current Windows edition
        :rtype: str
        """
        return win32_edition()

    @property
    def win32_is_iot(self) -> bool:
        """Return True if the Windows edition returned by win32_edition() is recognized
        as an IoT edition.

        :return: True if recognized as an IoT edition, False otherwise
        :rtype: bool
        """
        return win32_is_iot()

    # psutil.win_service_iter()
    # psutil.win_service_get(name)

    @property
    def mac_ver(self) -> tuple[str, tuple[str, str, str], str]:
        """Get macOS version information and return it as tuple (release, versioninfo,
        machine) with versioninfo being a tuple (version, dev_stage,
        non_release_version).

        Entries which cannot be determined are set to ''. All tuple entries are strings.

        :return:
        :rtype: tuple[str, tuple[str, str, str], str]
        """
        return mac_ver(release="", versioninfo=("", "", ""), machine="")

    @property
    def libc_ver(self) -> tuple[str, str]:
        """Tries to determine the libc version against which the file executable
        (defaults to the Python interpreter) is linked. Returns a tuple of strings (lib,
        version) which default to the given parameters in case the lookup fails.

        Note that this function has intimate knowledge of how different libc versions
        add symbols to the executable is probably only usable for executables compiled
        using gcc.

        The file is read and scanned in chunks of chunksize bytes.

        :return: (lib, version)
        :rtype: tuple[str, str]
        """
        return libc_ver(executable=sys.executable, lib="", version="", chunksize=16384)

    @property
    def freedesktop_os_release(self) -> dict[str, str]:
        """Get operating system identification from os-release file and return it as a
        dict. The os-release file is a freedesktop.org standard and is available in most
        Linux distributions. A noticeable exception is Android and Android-based
        distributions.

        Raises OSError or subclass when neither /etc/os-release nor /usr/lib/os-release
        can be read.

        On success, the function returns a dictionary where keys and values are strings.
        Values have their special characters like " and $ unquoted.

        The fields NAME, ID, and PRETTY_NAME are always defined according to the
        standard. All other fields are optional. Vendors may include additional fields.
        Note that fields like NAME, VERSION, and VARIANT are strings suitable for
        presentation to users.

        Programs should use fields like ID, ID_LIKE, VERSION_ID, or VARIANT_ID to
        identify Linux distributions.

        :return: operating system identification from os-release file
        :rtype: dict[str, str]
        """
        return freedesktop_os_release()

    @property
    def browsers(self) -> list[Browser]:
        """
        Return a list of installed browsers.

        :return: a list of installed browsers
        :rtype: list[Browser]
        """
        return detect_installed_browsers()
