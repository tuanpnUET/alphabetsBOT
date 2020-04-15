import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('socuat2.jpg',0)
cv2.line(img,(24,11),(24,11),(255,0,0),1)
cv2.imwrite('socuat2.png',img)
