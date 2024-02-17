import warnings
warnings.filterwarnings("ignore")
import sys
import json
import argparse
import textwrap
import platform

from syinfo.device_info import DeviceInfo
from syinfo.network_info import NetworkInfo
from syinfo.syinfo import SysInfo


def contact():
    """contact links."""
    print("\n-- Gmail: <mohitrajput901@gmail.com> \n-- GitHub: <https://github.com/MR901/>\n")


# def help():
#     """Help."""
#     if platform.system() == "Linux":
#         PURPLE, CYAN, DARKCYAN, BLUE, GREEN, YELLOW, RED, BOLD, UNDER, END = '\033[95m', '\033[96m', '\033[36m', '\033[94m', '\033[92m', '\033[93m', '\033[91m', '\033[1m', '\033[4m', '\033[0m'
#     else:
#         PURPLE, CYAN, DARKCYAN, BLUE, GREEN, YELLOW, RED, BOLD, UNDER, END = '', '', '', '', '', '', '', '', '', ''

#     print(f"""
# syinfo v0.0.0

# {UNDER}{BOLD}Usage:{END}
#     {RED}>>> {YELLOW}import {CYAN}who_is_on_my_wifi{END} as wiom

#     {RED}>>> {CYAN}wiom{END}.{GREEN}help(){END} {BOLD}{RED}    # show this help page{END}
#     {RED}>>> {CYAN}wiom{END}.{GREEN}contact(){END} {BOLD}{RED} # show contact{END}
#     {RED}>>> {CYAN}wiom{END}.{GREEN}license(){END} {BOLD}{RED} # show license{END}

#     {RED}>>> {CYAN}wiom{END}.{GREEN}who(n){END}  {BOLD}{RED}   # scan wifi (n : optional integer, means scanning time in seconds; default 10){END}
#     {RED}>>> {CYAN}wiom{END}.{GREEN}device(){END} {BOLD}{RED}  # see information about your device{END}
#     """)


def main():
    """Main function

    Return:
        json or print (default)
        device info
        network info
        sys info
    """
    wrapper = textwrap.TextWrapper(width=50)
    description = wrapper.fill(text="Sys-Info")

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter, description=description,
        epilog=textwrap.dedent("""GitHub: https://github.com/MR901/sys_info\n""")
    )

    parser.add_argument(
        '-c', '--contact', action='store_true', help='show contact'
    )
    parser.add_argument(
        '-v', '--version', action='version', version='0.0.0', help='show current version'
    )
    parser.add_argument(
        '-d', '--device', action="store_true", help='show information about your device.'
    )
    parser.add_argument(
        '-n', '--network', action="store_true", help='show information about your network.'
    )
    parser.add_argument(
        '-s', '--system', action="store_true", help='show combined information about your device and network.'
    )
    parser.add_argument(
        "-t", "--time", type=int, metavar="", required=False, default=10,
        help="int supplement for '-n' or '-s' command (scanning '-t' seconds)"
    )
    parser.add_argument(
        '-o', '--disable-vendor-search', action="store_false",
        help="supplement for '-n' or '-s' command to stop searching for vendor for the device (mac)"
    )

    parser.add_argument(
        '-p', '--disable-print', action="store_true", help='disable printing of the information.'
    )
    parser.add_argument(
        '-j', '--return-json', action="store_true", help='return output as json'
    )

    # Get the args
    args = parser.parse_args()

    instance = None
    if args.contact:
        contact()
    elif args.device:
        instance = DeviceInfo
        info = instance.get_all()
    elif args.network:
        instance = NetworkInfo
        info = instance.get_all(
            search_period=args.time,
            search_device_vendor_too=args.disable_vendor_search
        )
    elif args.system:
        instance = SysInfo
        info = instance.get_all(
            search_period=args.time,
            search_device_vendor_too=args.disable_vendor_search
        )
    elif len(sys.argv) == 1:
        parser.print_help()
        # help()
    else:
        parser.print_help()
        # help()

    if instance:
        if args.disable_print is False:
            instance.print(info)

        if args.return_json:
            print(json.dumps(info))


if __name__ == "__main__":
    main()
