from datetime import datetime
from platform import node
from cpuinfo import get_cpu_info
from psutil import cpu_freq, cpu_count, virtual_memory, disk_usage, boot_time
from json import dumps


def bytes_to_megabytes(bytes):
    return f"{round(bytes/1024/1024, 2)} MB"


cpu_info = get_cpu_info()
cpu_freq_info = cpu_freq()
virtual_memory_info = virtual_memory()
disk_usage_info = disk_usage("/")
pc_info = {
    "PCName": node(),
    "CPU": {
        "Brand": cpu_info["brand_raw"],
        "Arch": cpu_info["arch"],
        "Bits": cpu_info["bits"],
        "CurrentFreq": cpu_freq_info.current,
        "MaxFreq": cpu_freq_info.max,
        "Cores": cpu_count(),
    },
    "RAM": {
        "Free": bytes_to_megabytes(virtual_memory_info.available),
        "Total": bytes_to_megabytes(virtual_memory_info.total),
    },
    "Disk": {
        "Free": bytes_to_megabytes(disk_usage_info.free),
        "Total": bytes_to_megabytes(disk_usage_info.total),
    },
    "BootTime": datetime.fromtimestamp(boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
}
print(dumps(pc_info, indent=4))
