#!/usr/bin/python3

from keras.models import load_model
import socket

print("content-type:text/plain")
print("Access-Control-Allow-Origin: *")
print()

# IP of the system
UDP_IP = ""

"""
Use port number higher than 1024,
as httpd is an unprivileged user
"""
UDP_PORT = 2001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

model = load_model("model-3.h5")

# Buffer size is 1024 bytes
data, address = sock.recvfrom(1024)
data = str(data).split(",")

z_rotation_vector = float(data[-1].replace(" ", "").replace("'", ""))
y_rotation_vector = float(data[-2])
x_rotation_vector = float(data[-3])

face_dir = model.predict([
               [z_rotation_vector, y_rotation_vector, x_rotation_vector]
           ])[0][0]

dir = "up" if face_dir > 0.5 else "down"

print(dir)
