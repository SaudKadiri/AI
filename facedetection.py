# OpenCV-Python is a library of Python bindings designed to solve computer vision problems.
# Face detection comes under the Computer Vision itself.
# pip install opencv-python

import cv2

# Get the image by using the imread() method
img = cv2.imread("/path/to/image/file")

# Grayscaling is the process of converting an image from other color spaces e.g. RGB, CMYK, HSV, etc. to shades of gray.
# Using the cvtColor method to grayscale the image using the COLOR_BGR2GRAY color space
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get the face_cascade using the CascadeClassified the method asks for the file path which we can get using
# cv2.data.haarcascades which gives out the path to various cascade files is concatenated with the required xml file name
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Get the frame vectors
# gray_img - The grayscaled image
# scaleFactor – Parameter specifying how much the image size is reduced at each image scale; we specify 1.1; higher the value higher the speed lower the accuracy
# minNeighbors – Parameter specifying how many neighbors each candidate rectangle should have to retain it. Higher values give fewer detection
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5)
# Additionally following can be specified:
# minSize – Minimum possible object size. Objects smaller than that are ignored.
# maxSize – Maximum possible object size. Objects bigger than this are ignored.

# Iterate over the image and plot and plot a green colored box as given in the faces vector
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x + w, y + h), (0, 255, 0), 3)

# Display the image using the imshow() method with two parameters: Window name, image_variable
cv2.imshow('Image', img)

# Use the below to wait for the window unless hit the exit button
cv2.waitKey(0)

# Destroy the windows on completion; as a good practice.
cv2.destroyAllWindows
