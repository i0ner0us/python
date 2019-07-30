#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# Netmiko is the same as ConnectHandler
from netmiko import Netmiko
from getpass import getpass

my_device = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": getpass(),
    "device_type": "cisco_ios",
    "port": "8181",
}

net_connect = Netmiko(**my_device)

# Make configuration changes using an external file
output = net_connect.send_config_from_file("change_file.txt")
print(output)

net_connect.disconnect()
