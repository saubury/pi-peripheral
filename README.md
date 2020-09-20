
_Pi Peripheral_ allows pysical buttons, switches and dials to control computer actions. Designed to add additional controls to games like _Microsoft Flight Simulator 2020_ - but can be used to control close to any keyboard activated activity. 

A Raspberry Pi Zero board acts as a HID (Human Interface Device) device - prentending to be a USB keyboard. Python code generates keypresses when GPIO events are triggered when buttons are activated. 

The Raspberry Pi Zero is identifed as an external keyboard and plugs in as a standard USB device (which also provides power to the Raspberry Pi Zero). 

# Box Enclosure

![Outside view of box](./docs/box-outside.jpg)

# Wiring

![Wiring of GPIO](./docs/wiring.jpg)


# Installing USB Peripheral

![Windows 10 Pop up message](./docs/win10-usb-msg.png)

# Game control binding

![Windows 10 Pop up message](./docs/msfs-keyboard-binding.png)




# Configure Raspberry Pi Zero as a USB Keyboard (HID)
Steps from https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

http://wiki.micropython.org/USB-HID-Keyboard-mode-example-a-password-dongle

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

After the file has been modified reboot the Pi

```
sudo chmod a+wr /dev/hidg0
```

# Installing the Pi Peripheral Service

```
sudo cp piperipheral.service /lib/systemd/system

sudo systemctl daemon-reload
sudo systemctl enable piperipheral.service
sudo systemctl start piperipheral.service
```

General checks
```
sudo systemctl status piperipheral.service
sudo journalctl -u piperipheral.service -b
ps -ef | grep piperipheral | grep -v grep
```



