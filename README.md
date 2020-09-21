
_Pi Peripheral_ allows physical buttons, switches and dials to control computer actions. Designed to add additional controls to games like _Microsoft Flight Simulator 2020_ - but can be used to control close to any keyboard activated activity. This can be used for gaming and simulations, home studios, video streaming - or anywhere where physical controls are preferable to using a keyboard.

A Raspberry Pi Zero board acts as a HID (Human Interface Device) device - pretending to be a USB keyboard. Python code generates key-presses when GPIO events are triggered. With basic wiring, the Raspberry Pi has 28 GPIO pins suitable for controlling actions.

![Animated GIF showing box in usage](./docs/pi-demo.gif)


The Raspberry Pi Zero is identified as an external keyboard and plugs in as a standard USB device (which also provides power to the Raspberry Pi Zero). 

# Pi Peripheral - Hardware

## Wiring
The Raspberry Pi is very easy to wire up to switches and push buttons. Each only requires a single connection to a spare GPIO pin, and a common ground. Software will configure the GPIO pin as an input. There is no need to a physical pull up resistor - this can be configured in software.

![Wiring of GPIO](./docs/schematic.png)


### Power
Both power and USB host (USB OTG) are provided by a single  micro-USB port. Use the port labeled "USB" (_not_ the one labeled "Power").

![Wiring of GPIO](./docs/wiring.jpg)

## Box Enclosure
You can be creative here - I just picked a generic project box which was easy mount the switches and push buttons.

![Outside view of box](./docs/box-outside.jpg)


# Pi Peripheral - Software


## Configure Raspberry Pi Zero as a USB Keyboard
The first software task is configure the Raspberry Pi Zero to act as a USB Keyboard (HID input device.) These steps have largely been inspired from [randomnerdtutorials](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/) which has more detailed steps should you run into problems.

```
echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
echo "dwc2" | sudo tee -a /etc/modules
echo "libcomposite" | sudo tee -a /etc/modules

sudo cp scripts/isticktoit_usb /usr/bin
sudo chmod +x /usr/bin/isticktoit_usb
```

Add this line to the second-last line of `/etc/rc.local` (just before the line containing `exit 0`)

```
/usr/bin/isticktoit_usb # This line new
exit 0 
```
## Installing the Pi Peripheral on your PC
All going well, you can not connect the _Pi Peripheral_ and it should be identified as a keyboard. This will work for Windows, Mac or Linux.  Here's what it looks like in Windows 10.

![Windows 10 Pop up message](./docs/win10-usb-msg.png)



## Installing the Pi Peripheral Service
Now the Raspberry Pi is acting like a USB Keyboard, we need to send some key commands. The _Pi Peripheral_ is a Python programmed installed as a service

```
sudo cp piperipheral.service /lib/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable piperipheral.service
sudo systemctl start piperipheral.service
```

## Configuring Key Pressess

```python
# Key mapping in the form
# (GPIO_ID, (press-key,press-key-modifier, release-key,release-key-modifier)) 

gpio_button_map = dict([
    (6, (KEY_S,MOD_ALT, KEY_S,MOD_L_CNTR))  
  ])
```

## Game control binding

![Windows 10 Pop up message](./docs/msfs-keyboard-binding.png)



# Miscellaneous 
General checks
```
sudo systemctl status piperipheral.service
sudo journalctl -u piperipheral.service -b
ps -ef | grep piperipheral | grep -v grep
```



