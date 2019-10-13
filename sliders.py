import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("cell.png") # your image path
tmp = image # for drawing a rectangle
stepSize = 50
(w_width, w_height) = (50, 50) # window size
for x in range(0, image.shape[1] - w_width , stepSize):
   for y in range(0, image.shape[0] - w_height, stepSize):
      window = image[x:x + w_width, y:y + w_height, :]
