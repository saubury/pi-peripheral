#!/usr/bin/env python3

from gpiozero import Button
from signal import pause

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

# Press a


def say_hello():
    write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
    # Release keys
    write_report(NULL_CHAR*8)

    print("Hello!")

def say_goodbye():
    print("Goodbye!")

button = Button(2)

button.when_pressed = say_hello
button.when_released = say_goodbye

pause()
