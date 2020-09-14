

## Python 3


```
sudo pip install virtualenv
which python3


virtualenv -p `which python3` venv
source venv/bin/activate
python --version
pip --version
pip install -r requirements.txt 
```

# Configure Raspberry Pi Zero as a USB Keyboard (HID)
Steps from https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

```
pi@raspberrypi:~ $ echo "dtoverlay=dwc2" | sudo tee -a /boot/config.txt
pi@raspberrypi:~ $ echo "dwc2" | sudo tee -a /etc/modules
pi@raspberrypi:~ $ sudo echo "libcomposite" | sudo tee -a /etc/modules
```

sudo chmod a+wr /dev/hidg0


# Installing a service

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



