#!/usr/bin/python

# Raspberry Pi ST-Link JTAG appliance.
# Copyright Fen Consultants Ltd 2016
#
# License: Freeware
#          This software is free to distribute and use as you wish.

import Adafruit_CharLCD as LCD
import subprocess
import time
import os

HEXDIR = '/mnt/usb'

menu = ['[ Program ]', '[ Erase ]', '[ Shutdown ]']
files = []
index = 0
findex = 0
quit = False

# Draw menu
def refresh():
    global index
    lcd.clear()
    lcd.set_color(1.0, 1.0, 1.0)
    lcd.message(menu[index] + '\n')
    if index == 0 and len(files) > 0:
        lcd.message(files[findex])

# Test for any button pressed
def is_pressed():
    if (lcd.is_pressed(LCD.SELECT) or
        lcd.is_pressed(LCD.LEFT) or
        lcd.is_pressed(LCD.RIGHT) or
        lcd.is_pressed(LCD.UP) or
        lcd.is_pressed(LCD.DOWN)):
        return True
    else:
        return False

# Wait for any key to be pressed and released
def anykey():
    while is_pressed(): pass
    while True:
        if is_pressed() == True: break;
    while is_pressed(): pass

# Execute JTAG program operation
def program():
    lcd.clear()
    lcd.set_color(0.0, 0.0, 1.0)
    lcd.message('Programming..\n')
    proc = subprocess.Popen(['/usr/local/bin/st-flash', 'write', HEXDIR + '/' + files[findex], '0x8000000'])
    proc.wait()
    if proc.returncode == 0:
        lcd.set_color(0.0, 1.0, 0.0)
        lcd.message('Successful')
    else:
        lcd.set_color(1.0, 0.0, 0.0)
        lcd.message('Failed!')
    anykey()

# Execute JTAG erase operation
def erase():
    lcd.clear()
    lcd.set_color(0.0, 0.0, 1.0)
    lcd.message('Erasing..\n')
    proc = subprocess.Popen(['/usr/local/bin/st-flash', 'erase'])
    proc.wait()
    if proc.returncode == 0:
        lcd.set_color(0.0, 1.0, 0.0)
        lcd.message('Successful')
    else:
        lcd.set_color(1.0, 0.0, 0.0)
        lcd.message('Failed!')
    anykey()

# Execute shutdown operation
def shutdown():
    global quit
    lcd.clear()
    lcd.message('Shutting down..')
    lcd.set_color(1.0, 0.0, 1.0)
    os.system("sudo shutdown -h now")
    quit = True

action = { 0 : program,
           1 : erase,
           2 : shutdown,
}

lcd = LCD.Adafruit_CharLCDPlate()

for file in os.listdir(HEXDIR):
    if file.endswith('.hex'):
        files.append(file)

refresh()

while quit == False:
    if lcd.is_pressed(LCD.LEFT):
        if index == 0:
            index = len(menu) - 1
        else:
            index = index - 1
        refresh()
        while lcd.is_pressed(LCD.LEFT): pass

    if lcd.is_pressed(LCD.RIGHT):
        if index == len(menu) - 1:
            index = 0
        else:
            index = index + 1
        refresh()
        while lcd.is_pressed(LCD.RIGHT): pass

    if lcd.is_pressed(LCD.UP):
        if findex == 0:
            findex = len(files) - 1
        else:
            findex = findex - 1
        refresh()
        while lcd.is_pressed(LCD.UP): pass

    if lcd.is_pressed(LCD.DOWN):
        if findex == len(files) - 1:
            findex = 0
        else:
            findex = findex + 1
        refresh()
        while lcd.is_pressed(LCD.DOWN): pass

    if lcd.is_pressed(LCD.SELECT):
        action[index]()
        while lcd.is_pressed(LCD.SELECT): pass
        if quit == False:
            refresh()
