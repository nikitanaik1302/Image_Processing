import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
imggray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
B,G,R = cv2.split(img)
imgM = cv2.merge([B*0,G*255,R*0])
imgM = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img0 = cv2.merge([np.ones_like(B),G*255,R])
img0 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
H,S,V = cv2.split(img)
img1= cv2.merge([np.ones_like(H)*10,S+10,V-10])
#img1 = cv2.cvtColor(img,cv2.COLOR_HSV2GRAY)

cv2.imshow('Image',img)
cv2.imshow('Imagegray',imggray)
cv2.imshow('Imagemerge',imgM)
cv2.imshow('Image0',img0)
cv2.imshow('hsv',img1)
cv2.waitKey()

