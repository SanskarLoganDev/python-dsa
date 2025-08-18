import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# in the brackets we give the path to the haarcascade file
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the frame to grayscale
    
    # README for detectMultiScale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5) # draw rectangle around the face
        roi_gray = gray[y:y + h, x:x + w] 
        # here we are extracting the region of interest (ROI) from the grayscale image and y is ahead of x because in images the first dimension is height and the second dimension is width
        roi_color = frame[y:y + h, x:x + w] 
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)  # draw rectangle around the eyes. Here we use roi_color as it gives the eye location relative to the face rectangle
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    if cv2.waitKey(1)== ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()