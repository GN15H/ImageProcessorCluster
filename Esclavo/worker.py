import socket
import image_processor
import pickle
import matplotlib.pyplot as plt
import numpy as np

IP_ADDR = "127.0.0.1"
PORT = 5000

a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a.connect((IP_ADDR,PORT))
data = [1]
full_data=b''
while data:
    data = a.recv(1024)
    full_data+=data
parsed_data = pickle.loads(full_data)

img_processor = image_processor.Image_Processor()
img_processor.blur(parsed_data,13)
# img_processor.to_grayscale(parsed_data)
a.sendall(pickle.dumps(parsed_data))