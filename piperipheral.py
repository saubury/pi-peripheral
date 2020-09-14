#!/usr/bin/env python3

from gpiozero import Button
from signal import pause

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def keyboard_do(letter):
    write_report(NULL_CHAR*2+chr(letter)+NULL_CHAR*5)
    # Release keys
    write_report(NULL_CHAR*8)

def button04_down():
    keyboard_do(4) # a

def switch04_on():
    keyboard_do(5) # b

def switch04_off():
    keyboard_do(6) # c

button04 = Button(2)
switch04 = Button(3)

button04.when_pressed = button04_down

switch04.when_pressed = switch04_on
switch04.when_released = switch04_off

pause()
