# HW-2 Socket Programming and Data Visualization
We read the 3D Accelerator sensor value on stm32 and send it to a Linux host and visualize it with matplotlib
## How to use
### Linux Host
1. Open the server.py code and change the host and port with your own setting
```
HOST = '192.168.0.106' # IP address
PORT = 5000 # Port to listen on (use ports > 1023)
```
2. Run the server.py on a Linux host.
### Stm32
1. Import `mbed-os-example-sockets` into MBED Studio
2. Add the `BSP_B-L475E-IOT01` libary into mbed stuio
3. Replace the `main.cc` and `mbed_app.json` with our code
4. Run the mbed program and connect it with your wifi
    the wifi configuration should edit in mbed_app.json
```
            "nsapi.default-wifi-ssid": "\"ssid-here\"",
            "nsapi.default-wifi-password": "\"pw-here\"",
```
Then the the device will...
1. Connect to the Linux host
2. Pass the data to the host through the socket
3. Plot the graph using matplotlib