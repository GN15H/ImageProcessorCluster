import socket
import pickle
import image_handler
import numpy as np
import threading
import matplotlib.pyplot as plt

NODES_AMOUNT = 2
BUFF_SIZE = 1024

class Connection_Handler:
    def __init__(self, nodes_amount):
        self.connections = []
        self.threads = []
        self.raw_img_segments = []
        self.nodes_amount = nodes_amount
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("0.0.0.0", 5000))
        
    def get_nodes(self):
        self.socket.listen()
        index=0
        while len(self.connections) < self.nodes_amount:
            acceptance = self.socket.accept()
            self.connections.append(acceptance)
            self.threads.append(threading.Thread(target=self._receive_segment_from_node, args=(acceptance[0],index)))
            self.raw_img_segments.append(0)
            index+=1
    
    def send_data(self, img):
        for index, sck in enumerate(self.connections):
            sck[0].sendall(pickle.dumps(img[index]))
            sck[0].shutdown(socket.SHUT_WR)

    def receive_segments(self):
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()

    def join_img(self,img_arr):
        new_img_segments =[]
        for segment in self.raw_img_segments:
            new_img_segments.append(pickle.loads(segment))
        image_handler.join_image_segments(img_arr,new_img_segments,self.nodes_amount)
        plt.imshow(img_arr)
        plt.show()

    
    def _receive_segment_from_node(self, conn, index):
        data = [1]
        full_data = b''
        while data:
            data = conn.recv(BUFF_SIZE)
            full_data += data
        self.raw_img_segments[index]=full_data

        