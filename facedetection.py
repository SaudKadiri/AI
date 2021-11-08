# OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
# Face detection comes under the Computer Vision itself.
# pip install opencv-python

import cv2

# Get the image by using the imread() method
img = cv2.imread("/path/to/image/file")

# Get the face_cascade using the CascadeClassified the method asks for the file path which we can get using
# cv2.data.haarcascades which gives out the path to various cascade files is concatenated with the required xml file name
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray.
# Using the cvtColor method to grayscale the image using the COLOR_BGR2GRAY color space
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the image using the imshow() method with two parameters: Window name, image_variable
cv2.imshow('Image', img)

# Use the below to wait for the window unless hit the exit button
cv2.waitKey(0)
