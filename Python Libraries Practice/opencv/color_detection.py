import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # get the width of the frame
    height = int(cap.get(4))  # get the height of the frame
    
    if not ret:
        break  # if no frame is captured, exit the loop
    
    # HSV = Hue, Saturation, Value (Lightness/Brightness)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert the frame to HSV color space becaus HSV is better for color detection/extraction
    # define range of blue color in HSV
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    
    # Mask will tell us which areas of the image to keep
    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # create a mask for blue color
    
    result = cv2.bitwise_and(frame, frame, mask=mask)  # apply the mask to the original frame
    
    cv2.imshow('frame', result)  # display the original frame
    cv2.imshow('mask', mask)  # display the mask
    
    if cv2.waitKey(1) == ord('q'):  # wait for 'q' key to exit
        break
    
cap.release()  # release the camera
cv2.destroyAllWindows()  # close all OpenCV windows

# THE BELOW CODE IS FOR CONVERTING A BGR COLOR TO HSV COLOR SPACE

# here we pass a 3D array to cvtColor, which is a single pixel in BGR format, to convert it to HSV format. Use this code convert your on colors from BGR to HSV.
# This is useful for color detection in OpenCV.
# BGR_color = np.array([[[255, 0, 0]]])
# x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
# x[0][0]  # this will give you the HSV value of the BGR color