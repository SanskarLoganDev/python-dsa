import cv2
import argparse
import mediapipe as mp

args = argparse.ArgumentParser()
args.add_argument("--mode", default='video')
args.add_argument("--filePath", default='Python_Libraries_Practice/opencv/projects/face_anonymizer/assets/stock_vid.mp4') # comment this line if you want to use webcam
args = args.parse_args()

def image_processing(img, face_detection):
    
    H, W = img.shape[:2]  # unpack the height and width
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
      
            img[y1:y1+h, x1:x1+w, :] = cv2.blur(img[y1:y1+h, x1:x1+w, :], (100, 100)) # apply a blur effect to the detected face region, and replace the original face region with the blurred one
            
    return img


# detect faces
mp_face_detection = mp.solutions.face_detection

# below model_selection can be 0 or 1. 0 is the short range model and 1 is the full range model
# min_detection_confidence is the minimum confidence value for face detection
with mp_face_detection.FaceDetection(model_selection = 0, min_detection_confidence=0.5) as face_detection:
    
    if args.mode in ["image"]:
        # read image
        img = cv2.imread(args.filePath)
        # img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
        # print(img.shape)  # print the shape of the image to get height and width
        
    
        img = image_processing(img, face_detection)  # process the image to detect faces
                
        cv2.imshow('Face Detection', img)  # display the image with detected faces
        cv2.waitKey(0) # waits for a key press indefinitely (usually takes value in milliseconds)
        cv2.destroyAllWindows()
        
        # save image
        cv2.imwrite('Python_Libraries_Practice/opencv/projects/face_anonymizer/assets/blurred_faces.jpg', img)

    elif args.mode in ["video"]:
        
        cap = cv2.VideoCapture(args.filePath)
        if not cap.isOpened():
            raise FileNotFoundError(f"Could not open video: {args.filePath}")

        # Read one frame to get size/FPS
        ret, frame = cap.read()
        if not ret:
            cap.release()
            raise RuntimeError("Failed to read the first frame.")

        H, W = frame.shape[:2]
        fps = cap.get(cv2.CAP_PROP_FPS)
        if not fps or fps != fps:  # handle NaN/0
            fps = 30.0

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(
            "Python_Libraries_Practice/opencv/projects/face_anonymizer/assets/blurred_faces.mp4",
            fourcc, fps, (W, H)
        )

        while ret:
            processed = image_processing(frame, face_detection)
            writer.write(processed)

            cv2.imshow("Face Anonymizer (press q to quit)", processed)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            ret, frame = cap.read()

        cap.release()
        writer.release()
        cv2.destroyAllWindows()
        
    elif args.mode in ["webcam"]:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Could not open webcam.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            processed = image_processing(frame, face_detection)
            cv2.imshow("Face Anonymizer (press q to quit)", processed)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


