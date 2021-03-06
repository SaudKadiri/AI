# In this python project we'll be detection the human emotions by their face 

import cv2


# Download the dataset from: https://www.kaggle.com/deadskull7/fer2013 and then open it
with open("fer2013.json", "r") as json_file:
    data = json.loads(json_file.read())
    json_file = str(data).replace("\'", "\"")
    # as JSON only allows enclosing strings with double quotes
    model = model_from_json(json_file)
    model.load_weights('model.h5')

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

    # Required parameters for put text
    # image: The image on which the text is to be displayed. Remember each frame is an image!
    # text: String(text) that is to be written on the image.
    # org: Coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
    # font: Font type of the text. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
    # fontScale: Font scale factor that is multiplied by the font-specific base size.
    # color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
    # thickness: It is the thickness of the line in px.
    #           Image,   Text,        Org,         Font type,      font scale,  color,    thickness
    cv2.putText(frame, "Emotion", (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
    
    
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
