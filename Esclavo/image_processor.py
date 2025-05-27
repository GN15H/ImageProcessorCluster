import math
import numpy as np

class Image_Processor:
    def __init__(self):
        pass
    
    def to_grayscale(self,img_segment):
        for row in img_segment:
            for pixel in row:
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                average = math.floor((r/3))+math.floor((g/3))+math.floor((b/3))
                pixel[:] = average
    
    def inverse(self,img_segment):
        img_segment = 255-img_segment

    def red(self,img_segment):
        img_segment[:,:,1:3] = 0
    
    def green(self, img_segment):
        img_segment[:,:,0] = 0
        img_segment[:,:,2] = 0

    def blue(self, img_segment):
        img_segment[:,:,0:2] = 0

    def blur(self,img,blur_amount):
        for row_i in range(img[:,0,0].size):
            for pixel_i in range(img[0,:,0].size-blur_amount):
                extension = math.floor(blur_amount/2)
                img[row_i,pixel_i+extension,0] = self._average_color_in_row(img,row_i,pixel_i,blur_amount,0)
                img[row_i,pixel_i+extension,1] = self._average_color_in_row(img,row_i,pixel_i,blur_amount,1)
                img[row_i,pixel_i+extension,2] = self._average_color_in_row(img,row_i,pixel_i,blur_amount,2)

    def _average_color_in_row(self,img,row,pixel,range_area,color):
        average=0
        for pixel_i in range(range_area):
            average+=math.floor(img[row,pixel_i+pixel,color]/range_area)
        return average