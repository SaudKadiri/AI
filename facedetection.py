# OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
# Face detection comes under the Computer Vision itself.
# pip install opencv-python

import cv2

# Get the image by using the imread() method
img = cv2.imread("/path/to/image/file")

# Display the image using the imshow() method with two parameters: Window name, image_variable
cv2.imshow('Image', img)

# Use the below to wait for the window unless hit the exit button
cv2.waitKey(0)
