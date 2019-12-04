import cv2
import numpy as np
import glob

file = []
for filename in glob.glob('img/*.png'):
    file.append(filename)

file.sort()

img_array = []
for filename in file:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()