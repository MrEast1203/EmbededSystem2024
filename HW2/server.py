import socket
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
HOST = '192.168.0.106' # IP address
PORT = 5000 # Port to listen on (use ports > 1023)

# Prepare the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.ion()  # Turn on interactive mode
plt.show()

# Define limits for the axes
ax.set_xlim([-1000, 1000])
ax.set_ylim([-1000, 1000])
ax.set_zlim([-1000, 1000])

# Axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server started. Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('Received from socket server : ', data)
            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
            obj = json.loads(data)
            t = obj['s']
            #plot.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
            #plot.xlabel("sample num")
            #plot.pause(0.0001)
            # Extract accelerometer data
            ACCELERO_X = float(obj['x'])
            ACCELERO_Y = float(obj['y'])
            ACCELERO_Z = float(obj['z'])
            ax.scatter(ACCELERO_X, ACCELERO_Y, ACCELERO_Z, c='blue')
            plt.draw()
            plt.pause(0.0001)
