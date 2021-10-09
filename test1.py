import cv2
import numpy as numpy
import os



#this one creates the black mask
# the purpose of this file is to detect the dominate color in an image 
# and use it to create a back ground
def create_blank(width, height, rgb_color=(0,0,0)):
    image = np.zeros((height, width, 3), np.uint8)

    color = tuple(reversed(rgb_color))

    image[:] = color

    return image