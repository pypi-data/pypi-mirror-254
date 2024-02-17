"""This file is to be run with Sudo."""
import os
import platform
import urllib.request
# import sys
# sys.path.append('/home/mohit/Documents/_Github/gg-plugins/notebook/src/')

import getmac
from scapy.all import ARP, Ether, srp

from syinfo.constants import UNKNOWN, NEED_SUDO
from syinfo.utils import Execute

__author__ = "Mohit Rajput"
__copyright__ = "Copyright (c)"
__version__ = "${VERSION}"
__email__ = "mohitrajput901@gmail.com"


def get_vendor(mac_address):
    """Search for the vendor based on the mac address."""
    # print('mac address:', mac_address, flush=True)
    try:
        device = urllib.request.urlopen(f"http://api.macvendors.com/{mac_address}")
        device = device.read().decode("utf-8")
        # print('1', device, flush=True)

    except:
        # urllib.error.HTTPError: HTTP Error 429: Too Many Requests
        try:
            device = urllib.request.urlopen(f"https://api.maclookup.app/v2/macs/{mac_address}")
            device = (device.read().decode("utf-8")).split(",")
            device = (device[3]).replace('company":', "").replace('"', "")
            # print('2', device, flush=True)
        except:
            device = UNKNOWN
    if len(device) == 0:
        device = UNKNOWN
    # print('3', device, flush=True)
    return device


def search_devices_on_network(time=10, seach_device_vendor_too=True):
    """Search the network for the presence of other devices."""
    debug = False

    # Check for the run environment
    plat = platform.system()
    if ((plat == "Linux") or (plat == "Darwin")) and (os.getuid() == 1000):
        print("Please run search_devices_on_network() with sudo access!")
        return NEED_SUDO

    # get needed infomation
    current_ip_on_network = Execute.on_shell("hostname -I")
    interface_mac_address = getmac.get_mac_address()
    gateway = Execute.on_shell("ip route | grep default | awk '{print $3}'")
    device_name = Execute.on_shell("sudo dmidecode | grep 'SKU Number' | head -1")
    device_name = device_name.split('SKU Number:')[-1].strip()

    # Get the conected device info
    start, connected_devices = 0, {}

    # appending the original execution device information
    connected_devices[current_ip_on_network] = {
        'mac_address': interface_mac_address,
        'device_name': device_name,
        'identifier': 'current device',
    }
    if seach_device_vendor_too:
        connected_devices[current_ip_on_network]['vendor'] = get_vendor(
            interface_mac_address)

    if debug: print('Searching Network', end='', flush=True)
    while start <= time:
        start += 1
        devided = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=gateway + "/24")
        packets = srp(devided, timeout=0.5, verbose=False)[0]  # '0.5' because of double attempts per second

        for result in packets:
            network_ip = result[1].psrc
            mac = result[1].hwsrc

            if (
                (network_ip in connected_devices)
                and (
                    (seach_device_vendor_too is False)
                    or ('device_vendor' not in connected_devices[network_ip])
                    or (connected_devices[network_ip]['device_vendor']!=UNKNOWN)
                )
            ):
                continue

            connected_devices[network_ip] = {}
            connected_devices[network_ip]['mac_address'] = mac
            connected_devices[network_ip]['identifier'] = (
                "router" if network_ip == gateway else UNKNOWN
            )

            if seach_device_vendor_too:
                connected_devices[network_ip]['device_vendor'] = get_vendor(mac)
        if debug: print('.', end='', flush=True)
    if debug: print(' complete.')

    return connected_devices

if __name__ == "__main__":
    connected_devices = search_devices_on_network(time=10, seach_device_vendor_too=True)
    print('\nconnected_devices:', connected_devices)
