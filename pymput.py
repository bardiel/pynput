#!/usr/bin/python
"""
pymput
Version:    0.1.1
Author:     Bardiel
License:    Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

Enables or disables a device (given it's name) through xinput. 
Made in Python 2.7

This program was made because of the lack for certain notebooks to disable touchpad through the built-in keyboard key. 
It's recommended to use this program as a keyboard shortcut.

Features: 
-Enables or disables a certain device depending on the current state.

TODO: 
-Accept parameters (such as "Device Name")
-Fix elem.strip on line 49 (read comment)

Changelog:
v0.1.1
+If device_name is not found on xinput list, exit(1) and print message

v0.1.0
Initial Release
"""
from subprocess import call
from subprocess import check_output

device_name = "SynPS/2 Synaptics TouchPad"
elid = ""

p = check_output(["xinput", "list"])
f = p.split('\n')
for elem in f:
    if device_name in elem:
        try:
            int(elem[elem.find("id=")+4])
            elid = elem[elem.find("id=")+3]
            elid += elem[elem.find("id=")+4]
        except:
            elid = elem[elem.find("id=")+3]

if elid == "":
    print "Deivce %s not found" % (device_name)
    exit(1)

p = check_output(["xinput", "list-props", elid])
f = p.split('\n')
for elem in f:
    if "Device Enabled" in elem:
        if elem.strip() == "Device Enabled (152):	0": #"(152)" is not always the same number in every machine. 
            call(["xinput", "set-prop", elid, "Device Enabled", "1"])
            print "Device ENABLED"
        else:
            call(["xinput", "set-prop", elid, "Device Enabled", "0"])
            print "Device DISABLED"
