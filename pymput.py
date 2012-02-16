"""
pymput
Version:    0.1.0
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
"""
from subprocess import call
from subprocess import check_output

device_name = "ImPS/2 ALPS GlidePoint"


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

p = check_output(["xinput", "list-props", elid])
f = p.split('\n')
for elem in f:
    if "Device Enabled" in elem:
        if elem.strip() == "Device Enabled (126):	0":
            call(["xinput", "set-prop", elid, "Device Enabled", "1"])
        else:
            call(["xinput", "set-prop", elid, "Device Enabled", "0"])