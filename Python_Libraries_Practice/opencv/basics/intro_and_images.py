import cv2

# by default cv2 will read the image in BGR format
# we have 3 options for reading the image: grayscale, color, and unchanged

'''
-1, cv2.IMREAD_COLOR: Loads a color image. Any transparency of image will be neglected. It is the default flag.
0, cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode.
1, cv2.IMREAD_UNCHANGED: Loads image as such including alpha channel.
'''

img = cv2.imread('Python_Libraries_Practice/opencv/basics/assets/semantic-tags.png', -1)

# img = cv2.resize(img, (400, 400)) # resizing the image to 400x400 pixels

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) # resizing the image to 50% of its original size

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # rotating the image 90 degrees clockwise

cv2.imwrite('Python_Libraries_Practice/opencv/basics/assets/semantic-tags-resized.jpg', img) # saving the resized image

cv2.imshow('image', img) # here image is the name of the window
cv2.waitKey(0) # waits for a key press indefinitely (usually takes value in milliseconds)
cv2.destroyAllWindows() # closes all the windows opened by OpenCV