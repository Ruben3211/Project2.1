# #!/usr/bin/python
# import sys
# import usb
# # find USB devices
# dev = usb.core.find(find_all=True)
# # loop through devices, printing vendor and product ids in decimal and hex
# for cfg in dev:
#     a = 0
#     #sys.stdout.write('Decimal VendorID=' + str(cfg.port_number) + ' & ProductID=' + str(cfg.idProduct) + '\n')
#     #sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
#     if(a == 0):
#         sys.stdout.write(str(cfg))

import os
from glob import glob
from subprocess import check_output, CalledProcessError

def get_usb_devices():
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices
        if 'usb' in dev.split('/')[5])
    return dict((os.path.basename(dev), dev) for dev in usb_devices)

def get_mount_points(devices=None):
    devices = devices or get_usb_devices() # if devices are None: get_usb_devices
    output = check_output(['mount']).splitlines()
    is_usb = lambda path: any(dev in path for dev in devices)
    usb_info = (line for line in output if is_usb(line.split()[0]))
    return [(info.split()[0], info.split()[2]) for info in usb_info]

if __name__ == '__main__':
    print(get_mount_points())