import numpy as np
import cv2
import random

img = cv2.imread('Python Libraries Practice/opencv/assets/kite.jpg')
# img = cv2.resize(img, (0, 0), fx = 0.75, fy = 0.75)  # resize the image to 600x600 pixels
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert BGR to Grayscale

# Max corners: maximum best corners to return
# Quality level: parameter characterizing the minimal accepted quality of image corners, range 0 to 1
# Min distance: minimum possible Euclidean distance between the returned corners
corners = cv2.goodFeaturesToTrack(gray, maxCorners=50, qualityLevel=0.01, minDistance=10)

# corners returns floating point values, we need to convert them to integer
corners = corners.astype(int) # int0 is deprecated

# since noiw every corner is inside two lists, we need to iterate through them, [[-109   57]]
for corner in corners:
    # ravel() flattens the array, example: [[-109   57]] becomes [-109, 57], example2: [[1,2], [3,4]] becomes [1,2,3,4]
    x, y = corner.ravel()  
    cv2.circle(img, (x, y), 3, (255,0,0), -1)  # draw a circle at each corner with radius 3 and color blue (255,0,0) and thickness -1 means filled circle

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        x1, y1 = corners[i].ravel()
        x2, y2 = corners[j].ravel()
        # draw a line between every pair of corners
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # alternate color for each line using numpy random
        # color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, (x1, y1), (x2, y2), color, 1)  # draw a green line with thickness 1


cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()