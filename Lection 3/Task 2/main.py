import psutil
import platform
import cpuinfo
computer_info = {
    'Main': {
        'System': '',
        'Hostname': '',
        'Machine': '',
    },
    'CPU': {
        'Processor': '',
        'Architecture': '',
        'Cores': ''

    },
    'RAM': {
        'Total': 0,
        'Used': 0,
        'Free': 0,
    },
    'Disks': {


    }
}
# Main
computer_info["Main"]["System"] = str((platform.system() + ' ' + platform.release()))
computer_info["Main"]["Hostname"] = platform.node()
computer_info["Main"]["Machine"] = platform.machine()
# CPU
cpu_info = cpuinfo.get_cpu_info()
computer_info['CPU']['Processor'] = cpu_info['brand_raw']
computer_info['CPU']['Architecture'] = cpu_info['arch']
computer_info['CPU']['Cores'] = cpu_info['count']
# RAM
ram_info = psutil.virtual_memory()
computer_info['RAM']['Total'] = round((ram_info.total/(1024**3)), 2)
computer_info['RAM']['Used'] = round((ram_info.used/(1024**3)), 2)
computer_info['RAM']['Free'] = round((ram_info.free/(1024**3)), 2)
# Disks
disks_info = psutil.disk_partitions(all=True)
for disk in disks_info:
    disk_usage = psutil.disk_usage(disk.mountpoint)
    computer_info['Disks'][disk.device] = {'Total': round(disk_usage.total/(1024**3), 2), 'Used': round(disk_usage.used/(1024**3), 2), 'Free': round(disk_usage.free/(1024**3), 2)}
for key in computer_info.keys():
    print(f"{key}\n{computer_info[key]}")

