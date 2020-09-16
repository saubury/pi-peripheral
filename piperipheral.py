#!/usr/bin/env python3

from signal import pause
import RPi.GPIO as GPIO 

NULL_CHAR = chr(0)
MOD_NONE = NULL_CHAR
MOD_CNTR = chr(1)
MOD_SHFT = chr(2)
KEY_NONE = 0


gpio_button_map = dict([
    (5, (4,MOD_NONE, KEY_NONE,MOD_NONE))    # Button 1
  , (6, (5, MOD_NONE, 6,MOD_NONE))          # Switch 1
  , (27, (7, MOD_SHFT, KEY_NONE,MOD_NONE))  # Button 2
  , (22, (8, MOD_NONE, 9,MOD_NONE))          # Switch 2
  , (4, (10, MOD_SHFT, KEY_NONE,MOD_NONE))  # Button 3
  , (17, (11, MOD_NONE, 12,MOD_NONE))          # Switch 3
  , (2, (6, MOD_CNTR, KEY_NONE,MOD_NONE))  # Button 4
  , (3, (14, MOD_NONE, 15,MOD_NONE))          # Switch 4
  ])


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def keyboard_release():
    # Release keys
    write_report(NULL_CHAR*8)

def keyboard_do(letter, mod):
    write_report(mod + NULL_CHAR + chr(letter) + NULL_CHAR*5)
    keyboard_release()

def gpio_callback(channel):
    if GPIO.input(channel):     
        key_id, mod_id = gpio_button_map[channel][2], gpio_button_map[channel][3]
    else:                 
        key_id, mod_id = gpio_button_map[channel][0], gpio_button_map[channel][1]

    if (key_id != KEY_NONE):
        keyboard_do(key_id, mod_id)
        


def main_key_loop():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    for k, v in gpio_button_map.items():
        GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.add_event_detect(k ,GPIO.BOTH,callback=gpio_callback, bouncetime=200) 
    pause()

if __name__ == '__main__':
    try:
        main_key_loop()
    finally:
        keyboard_release()
        GPIO.cleanup()
