#!/usr/bin/env python3

from signal import pause
from time import sleep
import RPi.GPIO as GPIO 

NULL_CHAR = chr(0)

# Byte 0 is for a modifier key, or combination thereof. It is used as a bitmap, each bit mapped to a modifier:
# bit 0: left control
# bit 1: left shift
# bit 2: left alt
# bit 3: left GUI (Win/Apple/Meta key)
# bit 4: right control
# bit 5: right shift
# bit 6: right alt
# bit 7: right GUI
MOD_NONE = NULL_CHAR
MOD_L_CNTR = chr(int('000000001', 2))
MOD_SHFT   = chr(int('000000010', 2))
MOD_ALT    = chr(int('000000100', 2))
MOD_R_CNTR = chr(int('000010000', 2))
KEY_NONE = 0

KEY_S = 22
KEY_L = 15
KEY_N = 17
KEY_R = 21
KEY_F = 9
KEY_A = 4
KEY_NUMPAD_DEL = 99


# Key mapping in the form
# (GPIO_ID, (press-key,press-key-modifier, release-key,release-key-modifier)) 

gpio_button_map = dict([
    (5, (KEY_R,MOD_SHFT, KEY_NONE,MOD_NONE))    # Button 1
  , (27, (KEY_F, MOD_L_CNTR, KEY_NONE,MOD_NONE))  # Button 2
  , (4, (KEY_A, MOD_ALT, KEY_NONE,MOD_NONE))  # Button 3
  , (2, (KEY_NUMPAD_DEL, MOD_L_CNTR, KEY_NONE,MOD_NONE))  # Button 4
  , (6, (KEY_S,MOD_ALT, KEY_S,MOD_L_CNTR))  # Switch 1
  , (22, (KEY_L, MOD_ALT, KEY_L,MOD_L_CNTR))          # Switch 2
  , (17, (KEY_L, MOD_R_CNTR, KEY_L,MOD_SHFT))          # Switch 3
  , (3, (KEY_N, MOD_ALT, KEY_N,MOD_L_CNTR))          # Switch 4
  ])


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def keyboard_release():
    # Release keys
    write_report(NULL_CHAR*8)

def keyboard_do(letter, mod):
    write_report(mod + NULL_CHAR + chr(letter) + NULL_CHAR*5)
    sleep(0.05)
    keyboard_release()

def gpio_callback(channel):
    if GPIO.input(channel):     
        # Button-RELEASE / Switch:DOWN
        key_id, mod_id = gpio_button_map[channel][2], gpio_button_map[channel][3]
    else:                 
        # Button-PRESS / Switch:UP
        key_id, mod_id = gpio_button_map[channel][0], gpio_button_map[channel][1]

    if (key_id != KEY_NONE):
        print('Key:{} Mod:{}'.format(key_id, mod_id))
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
