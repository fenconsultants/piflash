Raspberry Pi ST-Link JTAG appliance.

Copyright Fen Consultants Ltd 2016

License: Freeware
         This software is free to distribute and use as you wish.

Self contained JTAG flashing appliance for ST microcontrollers.

Hardware configuration:

Raspberry Pi (tested with model 3-B, should work with others)
Adafruit RGB LCD Plate w/ Keypad
ST ST-Link V2

Depends on st-link tool and ADAFruit LCD Python library:

https://github.com/texane/stlink
https://github.com/adafruit/Adafruit_Python_CharLCD

Mount USB memory key containing hex files at /mnt/usb or change HEXDIR
in the script.

Call startup.py early in boot sequence if you want a loading message,
e.g. from cron @reboot. Call piflash.py later after USB devices are
enumerated and external filesystem is mounted, e.g. late in runlevel 5.

Use left/right buttons to cycle through menu options. On Program option,
up/down buttons cycle through available hex files. Press Select to
activate the current option.
