"""Module containing utils for sys_info."""

import os
import time
import platform
import subprocess
import urllib.request

from syinfo.constants import UNKNOWN, NEED_SUDO

__author__ = "Mohit Rajput"
__copyright__ = "Copyright (c)"
__version__ = "${VERSION}"
__email__ = "mohitrajput901@gmail.com"


class HumanReadable:
    """Convery some information to the format that is easy to interpret."""

    @staticmethod
    def size_to_bytes(size):
        """Convert size with units to number of bytes.

        eg.
            "32 MB", "32MB", "32mB", "100 kB", "123 B", "123"
        """
        multipliers = {
            'kb': 1024,
            'mb': 1024 * 1024,
            'gb': 1024 * 1024 * 1024,
            'tb': 1024 * 1024 * 1024 * 1024
            # 'pb': 1024*1024*1024*1024*1024
            # 'eb': 1024*1024*1024*1024*1024*1024
            # 'zb': 1024*1024*1024*1024*1024*1024*1024
        }
        size = str(size)
        for suffix in multipliers:
            if size.lower().endswith(suffix):
                return int(size[0:-len(suffix)]) * multipliers[suffix]
        else:
            if size.lower().endswith('b'):
                return int(size[0:-1])

        try:
            return int(size)
        except ValueError:  # for example "1024x"
            raise Exception("Malformed input!")

    @staticmethod
    def bytes_to_size(num_bytes, suffix='B'):
        """Convert the bytes to a easy readable format.

        for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        """
        for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
            if abs(num_bytes) < 1024.0:
                return "%3.1f %s%s" % (num_bytes, unit, suffix)
            num_bytes /= 1024.0
        return "%.1f %s%s" % (num_bytes, 'Yi', suffix)

    @staticmethod
    def time_spend(time_in_sec):
        """Convert time in second to human readable time.

        Args:
            time_in_sec: time in seconds
        Return:
            Human readable time
        """
        day = int(time_in_sec // (24 * 3600))
        time_in_sec = time_in_sec % (24 * 3600)
        hour = int(time_in_sec // 3600)
        time_in_sec %= 3600
        minutes = int(time_in_sec // 60)
        time_in_sec %= 60
        seconds = int(time_in_sec)
        msec = round((time_in_sec % 1) * 1000, 2)

        if day != 0:
            return f'{day} day, {hour} hr, {minutes} min, {seconds} sec, {msec} ms'
        elif hour != 0:
            return f'{hour} hr, {minutes} min, {seconds} sec, {msec} ms'
        elif minutes != 0:
            return f'{minutes} min, {seconds} sec, {msec} ms'
        else:
            return f'{seconds} sec, {msec} ms'


class Execute:
    """Execute command on shell or api."""

    @staticmethod
    def on_shell(cmd, line_no=None):
        """Run command on shell.

        Args:
            cmd: command to run on shell
            line_no: index or None. If None return whole result
        """
        result = UNKNOWN
        try:
            out = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE,  #stderr=subprocess.STDOUT
                stderr=subprocess.PIPE
            )
            if line_no is not None:
                lines = out.stdout.readlines()
                if len(lines) != 0:
                    result = lines[line_no].decode("utf-8").replace("\n", "").strip()
            else:
                # result = out.stdout.read()
                stdout, stderr = out.communicate()
                _error_msg = stderr.decode("utf-8").strip()
                if len(_error_msg) != 0:
                    print(_error_msg)
                result = stdout.decode("utf-8").strip()
        except Exception as e:
            print(e)
        finally:
            if (
                (platform.system() in ["Linux", "Darwin"]) and
                ('sudo ' in cmd.lower()) and
                (os.getuid() == 1000)  # runtime is non-sudo
            ):
                print(f"Please run the code in sudo for better result with '{cmd}'")
                return NEED_SUDO
            return result

    @staticmethod
    def api(url, line_no=None):
        """Run API."""
        result = UNKNOWN
        try:
            out = urllib.request.urlopen(url)
            response = out.read().decode("utf-8")
            if line_no is not None:
                response = response.split('\n')
                if len(response) != 0:
                    result = response[line_no].strip()
            else:
                result = response.strip()
        except Exception as e:
            print(e)
        finally:
            return result
