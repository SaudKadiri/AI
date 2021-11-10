# In this python project we'll be detection the human emotions by their face 

import cv2

# This will return video from the first webcam on your computer. If needed a secondary camera, use '1'
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Infinite loop (run until the user presses the esc key)
while True:
    # tuple to get the frame
    #   ret is a boolean regarding whether or not there was a return at all
    #   frame stores the current video frame; None is returned if no frame is found
    ret, frame = cap.read()

    # Show the frame
    cv2.imshow('Live video cam', frame)

    # The function waitKey waits for a key event infinitely (when \texttt{delay}\leq 0 ) or for delay milliseconds, when it is positive
    c = cv2.waitKey(1)
    if c == 27:
        # if esc key pressed exit the loop
        break

# Relese the hardware and software resources occupied including closing the camera
cap.release()
# As a good programming practice closing all the windows
cv2.destroyAllWindows()
