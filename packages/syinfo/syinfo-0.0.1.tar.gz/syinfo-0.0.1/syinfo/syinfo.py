from syinfo.device_info import DeviceInfo
from syinfo.network_info import NetworkInfo


class SysInfo:
    """Get the system (hardware+software+network) related information."""

    @staticmethod
    def print(info, return_msg=False):
        """Print system information."""
        _msg = DeviceInfo.print(info, True)
        _msg += NetworkInfo.print(info, True)
        if return_msg:
            return _msg
        else:
            print(_msg)

    @staticmethod
    def get_all(search_period=10, search_device_vendor_too=True):
        """Aggregate all the information related to the device and network."""
        device_info = DeviceInfo.get_all()
        network_info = NetworkInfo.get_all(search_period, search_device_vendor_too)
        device_info['network_info'] = network_info['network_info']
        return device_info
