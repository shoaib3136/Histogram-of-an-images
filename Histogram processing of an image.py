#!/usr/bin/env python
# coding: utf-8

# In[1]:Write your code to find the histogram of gray scale image and color image channels


import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2
Gray_image = cv2.imread("gray.jpeg")
Color_image = cv2.imread("rose.jpg")
plt.imshow(Gray_image)
plt.show()
plt.imshow(Color_image)
plt.show()


# In[2]:Display the histogram of gray scale image and any one channel histogram from color image


plt.imshow(Gray_image)
plt.show()
hist =cv2.calcHist([Gray_image], [0], None, [256],[0,256])
plt.figure()
plt.title("Histogram")
plt.xlabel('grayscale value')
plt.ylabel('pixel count')
plt.stem (hist)
plt.show()
plt.imshow(Color_image)
plt.show()
hist1=cv2.calcHist([Color_image], [1], None, [256], [0,256])
plt.figure()
plt.title("Histogram of Color Image - Green Channel")
plt.xlabel("Intensity Value")
plt.ylabel("Pixel Count")
plt.stem (hist1)
plt.show()



# In[3]:Write the code to perform histogram equalization of the image. 



plt.imshow(Color_image)
plt.show()
hist1=cv2.calcHist([Color_image], [1], None, [256], [0,256])
plt.figure()
plt.title("Histogram of Color Image - Green Channel")
plt.xlabel("Intensity Value")
plt.ylabel("Pixel Count")
plt.stem (hist1)
plt.show()







