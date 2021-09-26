"""
App used - IMU+GPS-Stream
This Script is for capturing the sensor values and storing them in CSV file for model training
"""

import socket
import csv

UDP_IP = ""
UDP_PORT = 339

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))

# Use '1' for face up and '0' for face down
face_dir = 1

# Number of readings to take for each face condition
NUMBER_OF_READINGS = 1000

# Name of csv file where readings to be saved
FILE_NAME = "rotation_vector_readings.csv"

counter = 0

with open(FILE_NAME, "a", newline="") as file :

    while counter < NUMBER_OF_READINGS:

        # buffer size is 1024 bytes 
        data, address = sock.recvfrom(1024)
        data = str(data).split(",")

        z_rotation_vector = float(data[-1].replace(" ","").replace("'",""))
        y_rotation_vector = float(data[-2])
        x_rotation_vector = float(data[-3])

        print(x_rotation_vector, y_rotation_vector, z_rotation_vector, sep = "  ")

        writer = csv.writer(file)
        writer.writerow([z_rotation_vector, y_rotation_vector, x_rotation_vector, face_dir])

        counter += 1

    file.close()

print("Data saved")    