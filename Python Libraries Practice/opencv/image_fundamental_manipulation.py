import cv2
import random

img = cv2.imread('Python Libraries Practice/opencv/assets/semantic-tags.png', -1)

# print(img) # it is in the format of a numpy array and in opencv the orfer is BGR (Blue, Green, Red)
'''
[
    [[0, 0, 0], [255, 255, 255], [255, 255, 255]],
    [[0, 0, 0], [255, 255, 255], [255, 255, 255]]
]
'''

print(f"Original Image Shape: {img.shape}") # format is (height, width, channels), here height is the number of rows, width is the number of columns, and channels is the number of color channels (3 for RGB or BGR)

# accessing pixel values
print(img[0]) # firs row of our image

print(img[257][900]) # accessing the pixel value at row 257 and column 900

for i in range(100, 200):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

img = cv2.resize(img, (500, 500))

tag = img[120: 170, 50: 200] # extracting a region of interest (ROI) from the image
img[120: 170, 300: 450] = tag # copying a region of interest (ROI) from one part of the image to another
# in the aimage it copies div tag from left to header tag on the right side

cv2.imshow('image', img) # displaying the image with the modified pixels
cv2.waitKey(0) # waits for a key press indefinitely (usually takes value in milliseconds)
cv2.destroyAllWindows() # closes all the windows opened by OpenCV
