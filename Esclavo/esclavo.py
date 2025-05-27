import socket
import image_processor
import pickle
import matplotlib.pyplot as plt
import numpy as np

a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a.connect(("127.0.0.1",5000))
data = [1]
full_data=b''
while data:
    data = a.recv(1024)
    full_data+=data
parsed_data = pickle.loads(full_data)

img_processor = image_processor.Image_Processor()
img_processor.blur(parsed_data,51)
a.sendall(pickle.dumps(parsed_data))