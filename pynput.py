#!/usr/bin/python2.7
"""
pynput
Version:    0.2.0
Author:     Bardiel
License:    Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

Enables or disables a device (given it's name or ID) through xinput.
Made in Python 2.7

This program was made because of the lack for certain notebooks to disable touchpad through the built-in keyboard key. 
It's recommended to use this program as a keyboard shortcut.

usage: pymput.py [-h] [-d DEVICE] [-i] [-I ID] [-l] [--enable] [--disable]

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE, --device DEVICE
                        Specify device name (default is "SynPS/2 Synaptics
                        TouchPad")
  -i, --interactive     Prints "xinput list" output and asks for ID.
  -I ID, --id ID        Specify device ID.
  -l, --list            Similar to -i, but only lists.
  --enable              Override default behavior by only enabling the device
  --disable             Override default behavior by only disabling the device

TODO: 
-Fix elem.strip on line 139 (read comment)
-Migrate to Python3
-Per user configuration file under ~/.config/pynput/pynput.conf for default device name

Changelog:
v0.2.0
+Optional arguments using builtin lib argparse
+find_elem_by_id(id)
+enable_device(id)
+disable_device(id)
*Change first line "#!/usr/bin/python" to "#!/usr/bin/python2.7" for newer systems compatibility
*Changed name from pymput to pynput

v0.1.1
+If args.device is not found on xinput list, exit(1) and print message

v0.1.0
Initial Release
"""
from subprocess import call
from subprocess import check_output
import argparse

def find_elem_by_id(id):
    """
    Returns True if ID is in the list
    """
    for elem in f:
            if id in elem:
                return True
    return False

def enable_device(id):
    """
    Enables the device given it's ID.
    Echoes the user
    """
    call(["xinput", "set-prop", id, "Device Enabled", "1"])
    print "Device ENABLED"

def disable_device(id):
    """
    Disables the device given it's ID.
    Echoes the user
    """
    call(["xinput", "set-prop", id, "Device Enabled", "0"])
    print "Device DISABLED"

parser = argparse.ArgumentParser(
    description='Enables or disables a device (given it\'s name or id) through xinput. ',
)

parser.add_argument('-d', '--device', help='Specify device name (default is "SynPS/2 Synaptics TouchPad")', default='SynPS/2 Synaptics TouchPad') #Specified here is the default device to enable or disable
parser.add_argument('-i', '--interactive', action='store_true', help='Prints "xinput list" output and asks for ID.')
parser.add_argument('-I', '--id', help='Specify device ID.')
parser.add_argument('-l', '--list', action='store_true', help='Similar to -i, but only lists.')
parser.add_argument('--toggle', action='store_true', help='Default behavior: if device is enabled, pynput disables it. Otherwise, it enables it')
parser.add_argument('--enable', action='store_true', help='Override default behavior by only enabling the device')
parser.add_argument('--disable', action='store_true', help='Override default behavior by only disabling the device')


found = False #Used to know whether args.device was found on xinput list or not
p = check_output(["xinput", "list"])
f = p.split('\n')

args = parser.parse_args() #Parsing arguments

if args.enable & args.disable:
    args.enable = False
    args.disable = False

if args.list: #List only prints xinput list output and exits
    print p
    exit(0)

if args.id: #If ID is specified check whether it exists in xinput list
    found = find_elem_by_id(args.id)
    elid = args.id
else: #Else check if interactive mode:
    if args.interactive: # Interactive: asks for elid
        print p
        elid = str(input("Select specified ID: "))
        found = find_elem_by_id(elid)
    else: #Fallback to default mode (device name specified at args.device)
        for elem in f:
            if args.device in elem:
                try:
                    int(elem[elem.find("id=")+4])
                    elid = elem[elem.find("id=")+3]
                    elid += elem[elem.find("id=")+4]
                except:
                    elid = elem[elem.find("id=")+3]
                found = True

if found == False: #If device is not found, exit(1) and alert user
    print "Deivce not found"
    exit(1)

#Enables or disables device given it's ID:
p = check_output(["xinput", "list-props", elid])
f = p.split('\n')

if args.enable:
    enable_device(elid)
    exit(0)
elif args.disable:
    disable_device(elid)
    exit(0)
else:
    for elem in f:
        if "Device Enabled" in elem:
            if elem.strip() == "Device Enabled (152):	0": #"(152)" is not always the same number in every machine. 
                enable_device(elid)
            else:
                disable_device(elid)
    exit(0)