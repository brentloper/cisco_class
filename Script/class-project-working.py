#! /usr/bin/env python

import xmltodict
import json
from device import Device

def show_dev_version(sw):
    getdata = sw.show('show version')

    show_dev_version_dict = xmltodict.parse(getdata[1])

    ver_data = show_dev_version_dict['ins_api']['outputs']['output']['body']

    dev_ver = ver_data['kickstart_ver_str']
    dev_mod = ver_data['chassis_id']
    dev_boot_file = ver_data['kick_file_name']

    dev_ver_dict = { 'Version': dev_ver, 'Model': dev_mod, 'Bootfile': dev_boot_file }

    return dev_ver_dict

def check_version(sw):
    desired_ver = 'nxos.7.1.3.1.bin'
    current_ver_data = show_dev_version(sw)
    current_ver = current_ver_data['Bootfile']

#    print current_ver

    if desired_ver == current_ver:
        print 'Version is acceptable, moving to next step.'

    print 'Version requires upgrading, beginning version upgrade process.'

def main():

    switch = Device(ip='172.31.217.133', username='admin', password='cisco123')
    switch.open()

    ver = show_dev_version(switch)

    print json.dumps(ver, indent=4)

    ver_check = check_version(switch)

    print json.dumps(ver_check, indent=4)



if __name__ == "__main__":
    main()
