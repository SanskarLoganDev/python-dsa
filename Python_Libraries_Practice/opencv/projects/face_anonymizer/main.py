import cv2
import mediapipe as mp
# read image

img = cv2.imread('Python_Libraries_Practice/opencv/projects/face_anonymizer/assets/stock.jpg')
# img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
print(img.shape)  # print the shape of the image to get height and width
H, W = img.shape[:2]  # unpack the height and width

# detect faces
mp_face_detection = mp.solutions.face_detection

# below model_selection can be 0 or 1. 0 is the short range model and 1 is the full range model
# min_detection_confidence is the minimum confidence value for face detection
with mp_face_detection.FaceDetection(model_selection = 0, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # convert the image to RGB as mediapipe works with RGB images
    out = face_detection.process(img_rgb)  # process the image to detect faces
    
    # print(out.detections)  # print the detected faces, see the data structure to extract
    
    if out.detections is not None: # out.detections will be None if no human faces are detected
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            
            x1 = int(x1 * W) # convert relative x1 to absolute x1
            y1 = int(y1 * H) 
            w = int(w * W)   
            h = int(h * H)
            
            # img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (255, 0, 0), 10)
      
# blur faces      
      
            img[y1:y1+h, x1:x1+w, :] = cv2.blur(img[y1:y1+h, x1:x1+w, :], (50, 50)) # apply a blur effect to the detected face region, and replace the original face region with the blurred one
            
    cv2.imshow('Face Detection', img)  # display the image with detected faces
    cv2.waitKey(0) # waits for a key press indefinitely (usually takes value in milliseconds)
    cv2.destroyAllWindows()

# save image

cv2.imwrite('Python_Libraries_Practice/opencv/projects/face_anonymizer/assets/blurred_faces.jpg', img)