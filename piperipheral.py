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


def button01_down():
    print('button01_down')
    keyboard_do(4) # a

def switch01_on():
    print('switch01_on')
    keyboard_do(5) # b

def switch01_off():
    print('switch01_off')
    keyboard_do(6) # c

def button02_down():
    print('button02_down')
    keyboard_do(7) # d

def switch02_on():
    print('switch02_on')
    keyboard_do(8) # e

def switch02_off():
    print('switch02_off')
    keyboard_do(9) # f

def button03_down():
    print('button03_down')
    keyboard_do(10) # g

def switch03_on():
    print('switch03_on')
    keyboard_do(11) # h

def switch03_off():
    print('switch03_off')
    keyboard_do(12) # i

def button04_down():
    print('button04_down')
    keyboard_do(13) # j

def switch04_on():
    print('switch04_on')
    keyboard_do(14) # k

def switch04_off():
    print('switch04_off')
    keyboard_do(15) # l


button01 = Button(5)
switch01 = Button(6)
button02 = Button(27)
switch02 = Button(22)
button03 = Button(4)
switch03 = Button(17)
button04 = Button(2)
switch04 = Button(3)

button01.when_pressed = button01_down
switch01.when_pressed = switch01_on
switch01.when_released = switch01_off

button02.when_pressed = button02_down
switch02.when_pressed = switch02_on
switch02.when_released = switch02_off

button03.when_pressed = button03_down
switch03.when_pressed = switch03_on
switch03.when_released = switch03_off

button04.when_pressed = button04_down
switch04.when_pressed = switch04_on
switch04.when_released = switch04_off

pause()
