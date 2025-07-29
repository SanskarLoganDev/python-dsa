import numpy as np
import cv2 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # if no frame is captured, exit the loop
    
    width = int(cap.get(3))  # get the width of the frame
    height = int(cap.get(4))  # get the height of the frame
    
    image = np.zeros(frame.shape, dtype=np.uint8)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)  # draw a blue diagonal line from top-left to bottom-right
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)  # draw a green diagonal line from bottom-left to top-right
    img = cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), 5)  # draw a red rectangle around the frame, here (100, 100) is the top-left and (200, 200) is the bottom-right
    img = cv2.circle(img, (width // 2, height // 2), 50, (255, 255, 0), 5)  # draw a cyan circle in the center of the frame with radius 50, here 5 is the thickness of the circle, if we use -1 instead of 5, it will fill the circle with color
    
    font = cv2.FONT_HERSHEY_SIMPLEX  # define the font for text
    img = cv2.putText(img, 'OpenCV Drawing', (50, 50), font, 2, (255, 255, 255), 2, cv2.LINE_AA)  # add white text to the image, here cv2.LINE_AA is used for anti-aliased lines. Here (50, 50) is the bottom left. Here 2 is the font scale, 2 is the thickness of the text
    
    cv2.imshow('frame', img)  # display the grayscale frame

    if cv2.waitKey(1) == ord('q'):  # wait for 'q' key to exit
        break

cap.release()  # release the camera
cv2.destroyAllWindows()  # close all OpenCV windows