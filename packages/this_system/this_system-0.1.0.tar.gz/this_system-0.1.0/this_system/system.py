# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License  along with this
# program. If not, see <https://www.gnu.org/licenses/>

#  Copyright © 2024. anonymous.

"""Information of this system."""
from dataclasses import dataclass

from this_system.network import NetworkInformation
from this_system.platform import PlatformInformation


@dataclass
class SystemInformation:
    """A class wrapping all available system information."""

    @property
    def platform(self) -> PlatformInformation:
        """
        Return available platform information.

        :return: available platform information
        :rtype: PlatformInformation
        """
        return PlatformInformation()

    @property
    def network(self) -> NetworkInformation:
        """
        Return available network information about this system.

        :return: available network information
        :rtype: NetworkInformation
        """
        return NetworkInformation()
