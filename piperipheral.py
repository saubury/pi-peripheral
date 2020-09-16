#!/usr/bin/env python3

from gpiozero import Button
from signal import pause
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

NULL_CHAR = chr(0)
MOD_NONE = NULL_CHAR

gpio_button_map = dict([(5, (4,MOD_NONE)), (6, (5, MOD_NONE)), (27, (6, MOD_NONE))])


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def keyboard_release():
    # Release keys
    write_report(NULL_CHAR*8)

def keyboard_do(letter):
    write_report(NULL_CHAR*2+chr(letter)+NULL_CHAR*5)
    keyboard_release()

def button_callback(channel):
    print('Channel {}'.format(channel))  
    key_id, mod_id = gpio_button_map[channel][0], gpio_button_map[channel][1]
    print('Key:{} Mod:{}'.format(key_id, mod_id))
    if GPIO.input(channel):     
        print('Button UP {}'.format(channel))  
    else:                 
        print('Button DOWN {}'.format(channel))  
        keyboard_do(key_id)
        


def main_key_loop():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) 

    for k, v in gpio_button_map.items():
        print('Setup GPIO {}'.format(k))
        GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.add_event_detect(k ,GPIO.BOTH,callback=button_callback, bouncetime=200) 
    pause()

if __name__ == '__main__':
    try:
        main_key_loop()
    finally:
        keyboard_release()
        GPIO.cleanup()
