# pynput

Version:    0.2.0  
Author:     Bardiel  
License:    Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.  

Enables or disables a device (given it's name or ID) through xinput.
Made in Python 2.7

This program was made because of the lack for certain notebooks to disable touchpad through the built-in keyboard key. 
It's recommended to use this program as a keyboard shortcut.

## Usage

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

## TODO:

* Fix elem.strip on line 139 (read comment)
* Migrate to Python3
* Per user configuration file under ~/.config/pynput/pynput.conf for default device name

## Changelog:

### v0.2.0

* Optional arguments using builtin lib argparse
* find_elem_by_id(id)
* enable_device(id)
* disable_device(id)
* Change first line "#!/usr/bin/python" to "#!/usr/bin/python2.7" for newer systems compatibility
* Changed name from pymput to pynput

### v0.1.1

* If args.device is not found on xinput list, exit(1) and print message

### v0.1.0

* Initial Release