"""Get Device info.

https://www.thepythoncode.com/article/get-hardware-system-information-python
"""

import os
import re
import sys
import time
import glob
import platform
import uuid
from datetime import datetime

import psutil
import getmac
from tabulate import tabulate
import yaml
import GPUtil

from syinfo.utils import Execute, HumanReadable

__author__ = "Mohit Rajput"
__copyright__ = "Copyright (c)"
__version__ = "${VERSION}"
__email__ = "mohitrajput901@gmail.com"


class DeviceInfo:
    """Get the Device (hardware+software) related information."""

    def _get_device_info():
        """Get device manufacture and device related inforation.

        dmicode info is available at /sys/devices/virtual/dmi/id.
        cmds:
            - "cat /sys/devices/virtual/dmi/id/sys_vendor"
            - "sudo dmidecode -s system-manufacturer"
            - "sudo dmidecode -s baseboard-product-name"
        """
        files = [
            path
            for path in glob.glob('/sys/devices/virtual/dmi/id/*')
            # for path in glob.glob('/sys/devices/virtual/dmi/id/**/*', recursive=True)
            # if (os.path.isfile(path)) and ('subsystem' not in path)
        ]
        info = {}
        for path in files:
            try:
                with open(path) as f:
                    txt = f.read()
                info[os.path.split(path)[-1]] = txt.replace('\n', '').strip()
            except:
                pass
        info = {k: v for k, v in sorted(info.items(), key=lambda item: item[0])}

        # create proper dict
        d = {}
        for k, val in info.items():
            category, name = k.split('_', 1) if len(k.split('_', 1)) == 2 else (k, None)
            if name is None:
                d[category] = val
            else:
                if category not in d:
                    d[category] = {}
                d[category][name] = val

        return d

    def _get_cpu_info():
        """ /proc/cpuinfo """
        cores = [
            yaml.load(e.replace('\t', ''), Loader=yaml.FullLoader)
            for e in Execute.on_shell('cat /proc/cpuinfo').split('\n\n')
        ]

        # consolidate the details
        di = {}
        for d in cores:
            for k, val in d.items():
                if k not in di:
                    di[k] = []
                di[k].append(val)

        for k, val in di.items():
            di[k] = (
                ' / '.join([str(e) for e in val])
                if len(set(val)) == len(val) else list(set(val))[0]
            )
        return di

    def _get_ram_info():
        """ /proc/meminfo or /sys/system/node/node0/meminfo """
        ram = [
            yaml.load(e.replace('\t', ''), Loader=yaml.FullLoader)
            for e in Execute.on_shell('cat /proc/meminfo').split('\n\n')
        ]
        if len(ram) != 1:
            raise Exception('Length of RAM here isn\'t 1; this is unexpected case')
        ram = ram[0]
        d = {}
        for k, val in ram.items():
            bytes = HumanReadable.size_to_bytes(val)
            d[k] = {
                'bytes': bytes,
                'human_readable': HumanReadable.bytes_to_size(bytes)
            }
        # sort by size
        d = {
            k: val
            for k, val in sorted(d.items(), key=lambda item: item[1]['bytes'], reverse=True)
        }
        return d

    @staticmethod
    def print(info, return_msg=False):
        """Print system information."""
        _msg = "=" * 40 + " System Information " + "=" * 40
        _msg += '\n.'
        _msg += '\n├── Device Information'
        _msg += '\n│   ├── {:.<20} {}'.format('Mac Address ', info['dev_info']['mac_address'])
        _msg += '\n│   ├── {:.<20} {}'.format('System Type', info['dev_info']['chassis'])
        _msg += '\n│   ├── {:.<20} {}'.format('Static Hostname ', info['dev_info']['static_hostname'])
        _msg += '\n│   ├── {:.<20} {}'.format('Icon Name ', info['dev_info']['icon_name'])
        _msg += '\n│   ├── Operating Software'
        for category, val in info['dev_info']['operating_system'].items():
            _msg += '\n│   │   {}── {:.<20} {}'.format(
                '└' if category == list(info['dev_info']['operating_system'].keys())[-1] else '├',
                ' '.join(category.split('_')).capitalize(), val
            )
        _msg += '\n│   ├── Device Manufacturer'
        for category, val in info['dev_info']['device'].items():
            if isinstance(val, dict) is False:
                _msg += '\n│   │   {}── {:.<16} {}'.format(
                    '└' if category == list(info['dev_info']['device'].keys())[-1] else '├', category, val
                )
                continue
            _msg += '\n│   │   {}── {}'.format(
                '└' if category == list(info['dev_info']['device'].keys())[-1] else '├', category
            )
            for name, sub_val in val.items():
                _msg += '\n│   │   {}   {}── {:.<16} {}'.format(
                    ' ' if name == list(info['dev_info']['device'].keys())[-1] else '│',
                    '└' if name == list(info['dev_info']['device'][category].keys())[-1] else '├',
                    name, sub_val
                )
        _msg += '\n│   └── {:.<16} {}'.format('Py Version ', info['dev_info']['python_version'])
        _msg += '\n├── Time'
        _msg += '\n│   ├── Current Time'
        _msg += '\n│   │   ├── {:.<16} {}'.format('Timestamp ', info['time']['current']['timestamp'])
        _msg += '\n│   │   └── {:.<16} {}'.format('Date/Time ', info['time']['current']['readable'])
        _msg += '\n│   ├── Boot Time'
        _msg += '\n│   │   ├── {:.<16} {}'.format('Timestamp ', info['time']['boot_time']['timestamp'])
        _msg += '\n│   │   └── {:.<16} {}'.format('Date/Time ', info['time']['boot_time']['readable'])
        _msg += '\n│   └── Uptime Time'
        _msg += '\n│       ├── {:.<16} {}'.format('Seconds ', info['time']['uptime']['in_seconds'])
        _msg += '\n│       └── {:.<16} {}'.format('Date/Time ', info['time']['uptime']['readable'])
        _msg += '\n├── CPU'
        _msg += '\n│   ├── Cores'
        _msg += '\n│   │   ├── {:.<16} {}'.format('Physical ', info['cpu_info']['cores']['physical'])
        _msg += '\n│   │   └── {:.<16} {}'.format('Total ', info['cpu_info']['cores']['total'])
        _msg += '\n│   ├── Frequency'
        try:
            _msg += '\n│   │   ├── {:.<16} {:.2f} Mhz'.format('Min ', info['cpu_info']['frequency_Mhz']['min'])
            _msg += '\n│   │   ├── {:.<16} {:.2f} Mhz'.format('Max ', info['cpu_info']['frequency_Mhz']['max'])
            _msg += '\n│   │   └── {:.<16} {:.2f} Mhz'.format('Current ', info['cpu_info']['frequency_Mhz']['current'])
        except:
            pass
        _msg += '\n│   ├── CPU Usage'
        _msg += '\n│   │   ├── {:.<16} {:.1f} %'.format('Total', info['cpu_info']['percentage_used']['total'])
        _msg += '\n│   │   └── CPU Usage Per Core'
        _msg += '\n' + '\n'.join([
            '│   │       {}── {:.<16} {:4.1f} %'.format(  # padding with <blankspace>
                '└' if c == list(info['cpu_info']['percentage_used']['per_core'].keys())[-1] else '├',
                c + ' ', pct
            )
            for c, pct in info['cpu_info']['percentage_used']['per_core'].items()
        ])
        _msg += '\n│   └── CPU Design'
        for name, val in info['cpu_info']['design'].items():
            _msg += '\n│       {}── {:.<16} {}'.format(
                '└' if name == list(info['cpu_info']['design'].keys())[-1] else '├',
                name, val
            )
        _msg += '\n├── Memory'
        _msg += '\n│   ├── Virtual'
        _msg += '\n│   │   ├── {:.<16} {}'.format('Used ', info['memory_info']['virtual']['readable']['used'])
        _msg += '\n│   │   ├── {:.<16} {}'.format('Free ', info['memory_info']['virtual']['readable']['available'])
        _msg += '\n│   │   ├── {:.<16} {}'.format('Total ', info['memory_info']['virtual']['readable']['total'])
        _msg += '\n│   │   └── {:.<16} {} %'.format('Percentage ', info['memory_info']['virtual']['percent'])
        _msg += '\n│   ├── Swap'
        _msg += '\n│   │   ├── {:.<16} {}'.format('Used ', info['memory_info']['swap']['readable']['used'])
        _msg += '\n│   │   ├── {:.<16} {}'.format('Free ', info['memory_info']['swap']['readable']['available'])
        _msg += '\n│   │   ├── {:.<16} {}'.format('Total ', info['memory_info']['swap']['readable']['total'])
        _msg += '\n│   │   └── {:.<16} {} %'.format('Percentage ', info['memory_info']['swap']['percent'])
        _msg += '\n│   └── Design'
        for category, val in info['memory_info']['design'].items():
            _msg += '\n│       {}── {}'.format(
                '└' if category == list(info['memory_info']['design'].keys())[-1] else '├', category
            )
            for name, sub_val in val.items():
                _msg += '\n│       {}   {}── {:.<16} {}'.format(
                    ' ' if category == list(info['memory_info']['design'].keys())[-1] else '│',
                    '└' if name == list(info['memory_info']['design'][category].keys())[-1] else '├',
                    name, sub_val
                )
        _msg += '\n├── Disk'
        _msg += '\n│   ├── Since Boot'
        _msg += '\n│   │   ├── {:.<16} {}'.format('Total Read ', info['disk_info']['since_boot']['total_read'])
        _msg += '\n│   │   └── {:.<16} {}'.format('Total Write ', info['disk_info']['since_boot']['total_write'])
        _msg += '\n│   └── Drives'
        _msg += '\n' + '\n'.join([
            '│       {}── {}\n│       {}   ├── {:.<16} {}\n│       {}   ├── {:.<16} {}\n│       {}   └── Space{}'.format(
                '└' if k == list(info['disk_info']['disks'].keys())[-1] else '├', k,
                ' ' if k == list(info['disk_info']['disks'].keys())[-1] else '│', 'Mountpoint ', disk['mountpoint'],
                ' ' if k == list(info['disk_info']['disks'].keys())[-1] else '│', 'File System ', disk['file_system_type'],
                ' ' if k == list(info['disk_info']['disks'].keys())[-1] else '│',
                ' .. NA' if 'space' not in info['disk_info']['disks'][k].keys() else (
                    '{0}{2:.<15} {3}{0}{4:.<15} {5}{0}{6:.<15} {7}{1}{8:.<15} {9} %'.format(
                        '\n│       {}       ├── '.format(' ' if k==list(info['disk_info']['disks'].keys())[-1] else '│'),
                        '\n│       {}       └── '.format(' ' if k==list(info['disk_info']['disks'].keys())[-1] else '│'),
                        'Used ', info['disk_info']['disks'][k]['space']['used'],
                        'Free ', info['disk_info']['disks'][k]['space']['free'],
                        'Total ', info['disk_info']['disks'][k]['space']['total'],
                        'Percent ', info['disk_info']['disks'][k]['space']['percent'],
                    )
                )
            )
            for k, disk in info['disk_info']['disks'].items()
        ])

        # Creating GPU Table
        _msg += "\n" + "=" * 40 + " GPU Details " + "=" * 40

        if len(info['gpu_info']) != 0:
            rows = [[k] + [val for kk, val in item.items()] for k, item in info['gpu_info'].items() ]
            header = ['gpu'] + list(info['gpu_info'][list(info['gpu_info'].keys())[0]].keys())
            _msg += tabulate(rows, headers=header)
        else:
            _msg += '\nNo GPU Detected\n'

        if return_msg:
            return _msg
        else:
            print(_msg)

    @staticmethod
    def get_all():
        """Get all system information.

        Return
            Infomation
        """
        # txt = Execute.on_shell('lsb_release -a')
        txt = Execute.on_shell('cat /etc/*release').replace('=', ': ')
        sys_d1 = yaml.load(txt, Loader=yaml.FullLoader)  # contains more information than utilized
        txt = '\n'.join([e.strip() for e in Execute.on_shell('hostnamectl').split('\n')])
        sys_d2 = yaml.load(txt, Loader=yaml.FullLoader)  # contains more information than utilized

        get_size = HumanReadable.bytes_to_size
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        curt_timestamp = round(time.time(), 1)
        curt = datetime.now()
        try:
            cpufreq = psutil.cpu_freq()
        except Exception as e:
            print('[Error] Unable to get output when running "psutil.cpu_freq()"')
            cpufreq = None

        # GPU information
        gpus = GPUtil.getGPUs()
        gpu_info = {}
        for i, gpu in enumerate(gpus):
            gpu_id = f'gpu_{i}'
            gpu_info[gpu_id] = {}
            # General Info
            gpu_info[gpu_id]['id'] = gpu.id
            gpu_info[gpu_id]['name'] = gpu.name
            gpu_info[gpu_id]['uuid'] = gpu.uuid
            # Usage
            gpu_info[gpu_id]['used_memory'] = gpu.memoryUsed * 1048576  # 1024x1024 (MB-->Bytes)
            gpu_info[gpu_id]['free_memory'] = gpu.memoryFree * 1048576
            gpu_info[gpu_id]['total_memory'] = gpu.memoryTotal * 1048576
            gpu_info[gpu_id]['temperature'] = gpu.temperature*100  # in °C
            gpu_info[gpu_id]['load_pct'] = gpu.load*100

        # get the memory details
        svmem = psutil.virtual_memory()
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()

        # Generating Disk Info
        disk_di = {}
        disk_di['device'] = {
            dpart.device: {
                'mountpoint': dpart.mountpoint,
                'file_system_type': dpart.fstype,
            }
            for dpart in psutil.disk_partitions()
        }
        for dpart in psutil.disk_partitions():
            try:
                partition_usage = psutil.disk_usage(dpart.mountpoint)
                disk_di['device'][dpart.device]['space'] = {
                    'used': get_size(partition_usage.used),
                    'free': get_size(partition_usage.free),
                    'total': get_size(partition_usage.total),
                    'percent': partition_usage.percent
                }
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue

        # ----------------------------------< Dict Creation >---------------------------------- #
        info = {
            'dev_info': {
                'mac_address': getmac.get_mac_address(),  # mac address of the wifi card
                # 'mac_address_2': f'{":".join(re.findall("..", "%012x" % uuid.getnode()))}', # https://stackoverflow.com/a/37775731
                'chassis': sys_d2['Chassis'],
                'static_hostname': platform.node(),  # sys_d2['Static hostname'] or uname.node
                'icon_name': sys_d2['Icon name'],
                'operating_system': {
                    'full_name': sys_d2['Operating System'],
                    'distribution': sys_d1['NAME'],
                    'platform': platform.platform(),
                    'version': sys_d1['VERSION'],
                    'update_history': uname.version,
                    'id_like': sys_d1['ID_LIKE'],
                    'system': uname.system,
                    'kernel': sys_d2['Kernel'],
                    'architecture': sys_d2['Architecture'],  # uname.machine or uname.processor,  # cpuinfo.get_cpu_info()['brand_raw']
                    'release': uname.release,
                    'machine_id': sys_d2['Machine ID'],
                    'boot_id': sys_d2['Boot ID'],
                },
                'device': DeviceInfo._get_device_info(),
                'python_version': f'{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}',
            },
            'time': {
                'current': {
                    'timestamp': curt_timestamp,
                    'readable': f'{curt.year}/{curt.month}/{curt.day} {curt.hour}:{curt.minute}:{curt.second}'
                },
                'boot_time': {
                    'timestamp': boot_time_timestamp,
                    'readable': f'{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}'
                },
                'uptime': {
                    'in_seconds': round(curt_timestamp - boot_time_timestamp, 1),
                    'readable': HumanReadable.time_spend(curt_timestamp - boot_time_timestamp)
                }
            },
            'cpu_info': {
                'cores': {
                    'physical': psutil.cpu_count(logical=False),
                    'total': psutil.cpu_count(logical=True)
                },
                'frequency_Mhz': {
                    'min': cpufreq.min if cpufreq is not None else 'Unable to Get Value',
                    'max': cpufreq.max if cpufreq is not None else 'Unable to Get Value',
                    'current': cpufreq.current if cpufreq is not None else 'Unable to Get Value'
                },
                'percentage_used': {
                    'total': psutil.cpu_percent(),
                    'per_core': {
                        # f'Core {i+1:02d}': percentage
                        f'Core {i+1: >2}': percentage
                        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1))
                    }
                },
                'design': DeviceInfo._get_cpu_info()
            },
            'gpu_info': gpu_info,
            'memory_info': {
                'virtual': {
                    'percent': svmem.percent,
                    'in_bytes': {
                        'used': svmem.used,
                        'available': svmem.available,
                        'total': svmem.total
                    },
                    'readable': {
                        'used': get_size(svmem.used),
                        'available': get_size(svmem.available),
                        'total': get_size(svmem.total)
                    }
                },
                'swap': {
                    'percent': swap.percent,
                    'in_bytes': {
                        'used': swap.used,
                        'available': swap.free,
                        'total': swap.total
                    },
                    'readable': {
                        'used': get_size(swap.used),
                        'available': get_size(swap.free),
                        'total': get_size(swap.total)
                    }
                },
                'design': DeviceInfo._get_ram_info()
            },
            'disk_info': {
                'disks': disk_di['device'],
                'since_boot': {
                    'total_read': get_size(disk_io.read_bytes),
                    'total_write': get_size(disk_io.write_bytes)
                }
            }
        }

        return info

    @staticmethod
    def get_process_details():
        '''
        Desc:
            get all the process details
        Input: None
        Return: DataFrame Containing the details on process
        '''
        # process.pid, process.name(), process.cpu_percent(), process.create_time(), process.is_running()
        # # process.memory_full_info()
        # process.memory_info(), process.status(), process.nice()
        # process.memory_percent()
        # process.cpu_times()
        # # process.threads()
        all_process = []
        for process in psutil.process_iter():
            # get all process info in one shot
            # with process.oneshot():
            #     pid = process.pid
            try:
                key_to_drop = ['cmdline', 'environ', 'uids', 'memory_full_info', 'open_files', 'gids', 'cpu_times']
                temp_di = {k:item for k, item in process.as_dict().items() if k not in key_to_drop }
                all_process.append(temp_di)
            except Exception as e:
                print(f'[Exception] in "" func. Unable to get details on process "{process}" b/c {e}')

        return all_process
