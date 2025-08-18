import numpy as np
import cv2 

cap = cv2.VideoCapture(0)  # 0 is the default camera, change to 1 or 2 for external cameras
# here instead of 0 we can also use the path to a video file to read from it

while True:
    ret, frame = cap.read()  # read a frame from the camera
    # here frame is a numpy array of shape (height, width, channels) (discussed in the previous file)
    
    if not ret:
        break  # if no frame is captured, exit the loop
    
    width = int(cap.get(3))  # get the width of the frame
    height = int(cap.get(4))  # get the height of the frame
    
    image = np.zeros(frame.shape, dtype=np.uint8)  # create a black image with the same shape as the frame
    # np.uint8 is NumPy’s unsigned 8-bit integer type. It allows values from 0 to 255.
    
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)  # resize the frame to half its size
    # since we are reducing both length and width by half, the area is reduced to 1/4th of the original size, therefore we can fit 4 images in the black image
    
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # place the resized frame in the top-left corner of the black image
    image[height//2:, :width//2] = smaller_frame # place the resized frame in the bottom-left corner of the black image
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # place the resized frame in the top-right corner of the black image
    image[height//2:, width//2:] = smaller_frame # place the resized frame in the bottom-right corner of the black image
    
    cv2.imshow('frame', image)  # display the grayscale frame

    if cv2.waitKey(1) == ord('q'):  # wait for 'q' key to exit
        break

'''
cv2.waitKey(1) waits for 1 ms each loop, then continues.

The loop only breaks if 'q' is pressed during one of those 1 ms checks—but since the check happens in every frame, it will catch your keypress very quickly in practice.
'''

cap.release()  # release the camera
cv2.destroyAllWindows()  # close all OpenCV windows