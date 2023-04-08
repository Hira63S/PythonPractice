import cv2
import numpy as np
import glob
import os


fil_dir = 'C://users/cathx/repos/nerf-pytorch/vid_images'
img_dir = 'C://users/cathx/repos/nerf-pytorch/vid_images/*.jpg'

img_array = []

img =  cv2.imread(os.path.join(fil_dir, 'ring_front_right_315969630254611840.jpg'))
h, w, l = img.shape
size = (w, h)
# print(img_size)

for filename in glob.glob(img_dir):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    # size = (width, height)
    img_array.append(img)
# print(img_array)

out = cv2.VideoWriter('NERF1.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()
