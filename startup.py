#!/usr/bin/python

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

lcd.set_color(1.0, 1.0, 1.0)
lcd.clear()
lcd.message('Fen Flash 1.0\nStarting...')
