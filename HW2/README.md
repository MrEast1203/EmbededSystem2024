# HW-2 Socket Programming and Data Visualization
We read the 3D Accelerator sensor value on stm32 and send it to a Linux host and visualize it with matplotlib using 3D plotting
## How to use
1. Run the server.py on a Linux host.
2. Run the mbed program and connect it with your wifi
    the wifi configuration should edit in mbed_app.json
```
            "nsapi.default-wifi-ssid": "\"TP-Link_98B0\"",
            "nsapi.default-wifi-password": "\"aaaassss\"",
```
3. Connect the device to the Linux host
4. Pass the data to the host through the socket
5. Plot the graph using matplotlib