import numpy as np
import matplotlib.pyplot as plt
import math


def read_image(image_path):
    image_arr = np.array(plt.imread(image_path))
    return image_arr
    
def get_image_segments(img_arr, segments):
    image_segments = []
    img_height = img_arr[:,0,0].size
    img_width = img_arr[0,:,0].size
    division = math.floor(img_height/segments)
    for i in range(segments):
        img_segment_arr=np.array(img_arr[i*division:(i+1)*division,:,:])
        image_segments.append(img_segment_arr)
    return image_segments

def join_image_segments(img_arr, img_segments, segments):
    img_height = img_arr[:,0,0].size
    division = math.floor(img_height/segments)
    for i in range(segments):
        img_arr[i*division:(i+1)*division,:,:] = img_segments[i]
    

def show_segments(img_segments):
    for segment in img_segments:
        plt.imshow(segment)
        plt.show()
