# How to use

1. Start Advertising on App using BLE TOOL
2. run `ble_scan_connect.py` on rpi
   When you run `pip install` without `sudo`, the package may not be accessible system-wide.
   Since it is not recommended to do `sudo pip install`, we need to set up a virtual environment.

```
# create the virtual environment
$ python3 -m venv env-ftp

# install the package into it
$ env-ftp/bin/python -m pip install bluepy

# run a script using the Python installation contained within the virtual environment
$ sudo env-ftp/bin/python -m ble_scan_connect
```

[reference: Stackoverflow](https://stackoverflow.com/questions/66410127/python-on-raspi-cant-find-installed-module)
As we write data`65 66 67` on characteristics `0xfff1`, so we can read `efg` on console. (65 66 67 is the ascii code for e f g)
Then after the console print `Notify`, it start waiting for notification 3. Write something on characteristics `0xfff2`
After the write, it will notify the console and end the program.
