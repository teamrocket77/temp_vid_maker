import cv2, os
import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc, imread
import os

width = 1920
height = 1080

center_w = width/2
center_h = height/2

#this one creates the black mask
def create_blank(width, height, rgb_color=(0,0,0)):
    image = np.zeros((height, width, 3), np.uint8)

    color = tuple(reversed(rgb_color))

    image[:] = color

    return image

#this calculates where the picture will start and end
def img_start():
    top_left = 1960- c//2
    left_edge = 540 -  r//2

    return [left_edge, top_left]


im_1 = cv2.imread('black.jpg')



im_2 = cv2.imread('first.jpg')

r, c, ch = im_2.shape
row, col = img_start()
dst = cv2.add(im_1, im_2)
roi = im_1[row:row+center_w, col:col+center_h]

cv2.imshow('res', im)


print os.getcwd()
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
Trying to remove the bits out of the background picture that consitutes 
the ROI


"""