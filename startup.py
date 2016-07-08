#!/usr/bin/python

# Raspberry Pi ST-Link JTAG appliance.
# Copyright Fen Consultants Ltd 2016
#
# License: Freeware
#          This software is free to distribute and use as you wish.


import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
lcd.message('Pi Flash 1.0\nStarting...')
