import cv2
import numpy as np
import glob
import os


fil_dir = 'C://users/cathx/repos/argoverse-api/val/00c561b9-2057-358d-82c6-5b06d76cebcf/ring_front_center/'
img_dir = 'C://users/cathx/repos/argoverse-api/val/00c561b9-2057-358d-82c6-5b06d76cebcf/ring_front_center/*.jpg'

img_array = []

img =  cv2.imread(os.path.join(fil_dir, 'ring_front_center_315969629921612120.jpg'))
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
