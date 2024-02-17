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

"""Network information of the system."""
from collections import namedtuple
from psutil import (
    net_if_stats,
    net_if_addrs,
    NIC_DUPLEX_FULL,
    NIC_DUPLEX_HALF,
    NIC_DUPLEX_UNKNOWN,
)


class NetworkInterfaceAddress:
    """
    A class wrapping network interface address information.
    """

    def __init__(self, snicaddr: namedtuple):
        """

        :param snicaddr: a named tuple as passed from psutil.net_if_addrs()
        :type snicaddr: namedtuple
        """
        if snicaddr.family == 2:
            self.__family__ = "IPv4"
        elif snicaddr.family == 10:
            self.__family__ = "IPv6"
        self.__address__ = snicaddr.address
        self.__netmask__ = snicaddr.netmask
        self.__broadcast__ = snicaddr.broadcast
        self.__point_to_point__ = snicaddr.ptp

    @property
    def family(self) -> str:
        """
        Return the type of address.

        :return: type of address
        :rtype: str
        """
        return self.__family__

    @property
    def address(self) -> str:
        """
        Return the allocated address.

        :return: the address
        :rtype: str
        """
        return self.__address__

    @property
    def netmask(self) -> str:
        """
        Return the allocated netmask.

        :return: the netmask
        :rtype: str
        """
        return self.__netmask__

    @property
    def broadcast(self) -> str:
        """
        Return the allocated broadcast address.

        :return: the broadcast address
        :rtype: str
        """
        return self.__broadcast__

    @property
    def point_to_point(self) -> str:
        """
        Return the address of the ptp link.

        :return: address of the ptp
        :rtype: str
        """
        return self.__point_to_point__


class NetworkInterface:
    """
    A class wrapping network interface information.
    """

    def __init__(self, iface_name: str, snicstats: namedtuple, snicaddr: namedtuple):
        """

        :param iface_name: the name of the interface.
        :type iface_name: str
        :param snicstats: a named tuple as return by psutil.net_if_stats()
        :type snicstats:  namedtuple
        :param snicaddr: a named tuple as return by psutil.net_if_addrs()
        :type snicaddr: namedtuple
        """
        self.__nic_name__ = iface_name
        self.__up__ = snicstats.isup
        if snicstats.duplex == NIC_DUPLEX_FULL:
            self.__duplex__ = "full"
        elif snicstats.duplex == NIC_DUPLEX_HALF:
            self.__duplex__ = "half"
        elif snicstats.duplex == NIC_DUPLEX_UNKNOWN:
            self.__duplex__ = "unknown"
        self.__speed__ = snicstats.speed
        self.__mtu__ = snicstats.mtu
        self.__flags__ = snicstats.flags
        self.__allocated_resources__ = []
        for allocated_resource in snicaddr:
            if allocated_resource.family == 17:
                self.__mac__ = allocated_resource.address
            else:
                self.__allocated_resources__.append(
                    NetworkInterfaceAddress(allocated_resource)
                )

    @property
    def name(self) -> str:
        """
        Return the name of the interface.

        :return: the name of the interface
        :rtype: str
        """
        return self.__nic_name__

    @property
    def is_up(self) -> bool:
        """
        Return whether the NIC is up.

        :return: True if the NIC if up, False otherwise.
        :rtype: bool
        """
        return self.__up__

    @property
    def duplex(self) -> str:
        """
        Return the duplex mode of the interface.

        :return: full/half/unknown
        :rtype: str
        """
        return self.__duplex__

    @property
    def speed(self) -> int:
        """
        Return the speed of the interface.

        :return: 0 if unknown, > 0 otherwise.
        :rtype: int
        """
        return self.__speed__

    @property
    def mtu(self) -> int:
        """
        Return the MTU of the interface.

        :return: the MTU in bytes
        :rtype: int
        """
        return self.__mtu__

    @property
    def mac(self) -> str:
        """
        Return the physical address of the interface.

        :return: the mac address
        :rtype: str
        """
        return self.__mac__

    @property
    def allocated_resources(self) -> list[NetworkInterfaceAddress]:
        """
        Return a list of NetworkInterfaceAddress objects.

        :return: a list of NetworkInterfaceAddress
        :rtype: list[NetworkInterfaceAddress]
        """
        return self.__allocated_resources__

    @property
    def loopback(self) -> bool:
        """
        Is the interface is a loopback interface.
        """
        return "loopback" in self.__flags__

    @property
    def broadcast(self) -> bool:
        """

        :return:
        :rtype: bool
        """
        return "broadcast" in self.__flags__

    @property
    def debug(self) -> bool:
        """
        Is the internal debugging flag is set.
        """
        return "debug" in self.__flags__

    @property
    def pointopoint(self) -> bool:
        """
        Is the interface is a point-to-point link.
        """
        return "pointopoint" in self.__flags__

    @property
    def notrailers(self) -> bool:
        """
        Is the 'Avoid use of trailers' flag is set.
        """
        return "notrailers" in self.__flags__

    @property
    def is_running(self) -> bool:
        """
        Have resources been allocated.
        """
        return "running" in self.__flags__

    @property
    def noarp(self) -> bool:
        """
        Is the 'No arp protocol' flag is set.
        L2 destination address not set.
        """
        return "noarp" in self.__flags__

    @property
    def promisc(self) -> bool:
        """
        Is the interface is in promiscuous mode.
        """
        return "promisc" in self.__flags__

    @property
    def allmulti(self) -> bool:
        """
        Can the interface receive all multicast packets.
        """
        return "allmulti" in self.__flags__

    @property
    def master(self) -> bool:
        """
        Is the interface the master of a load balancing bundle.
        """
        return "master" in self.__flags__

    @property
    def slave(self) -> bool:
        """
        Is the interface a slave of a load balancing bundle.
        """
        return "slave" in self.__flags__

    @property
    def multicast(self) -> bool:
        """
        Supports multicast
        """
        return "multicast" in self.__flags__

    @property
    def portsel(self) -> bool:
        """
        Is able to select media type via ifmap.
        """
        return "portsel" in self.__flags__

    @property
    def dynamic(self) -> bool:
        """
        Are the addresses lost when the interface goes down?
        """
        return "dynamic" in self.__flags__

    @property
    def oactive(self) -> bool:
        """

        :return:
        :rtype: bool
        """
        return "oactive" in self.__flags__

    @property
    def simplex(self) -> bool:
        """

        :return:
        :rtype: bool
        """
        return "simplex" in self.__flags__


def get_network_interfaces() -> list[NetworkInterface]:
    """Detect all network interfaces and their properties as well as their addresses.

    :return: A list of network interfaces in this computer
    :rtype: list[NetworkInterface]
    """
    results = []
    for iface_name, snicstats in net_if_stats().items():
        results.append(
            NetworkInterface(iface_name, snicstats, net_if_addrs()[iface_name])
        )
    return results


class NetworkInformation:
    """A class wrapping network information about this system."""

    @property
    def interfaces(self) -> list[NetworkInterface]:
        """Return all network interfaces, their properties and their addresses.

        :return: a list of network interfaces detected in this system
        :rtype: list[NetworkInterface]
        """
        return get_network_interfaces()

    @property
    def is_connected(self) -> bool:
        """Check if there is at least one network interface up that is not the loopback
        interface and has resources allocated.

        :return: True if at least one network interface is up, False otherwise
        :rtype: bool
        """
        for net_if in self.interfaces:
            if not net_if.loopback and net_if.is_running:
                return True
        return False
