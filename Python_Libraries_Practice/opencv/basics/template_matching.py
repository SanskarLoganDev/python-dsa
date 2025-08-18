import cv2

# we extract the images in grayscale for algorithms to use them properly
img = cv2.resize(cv2.imread('Python_Libraries_Practice/opencv/basics/assets/soccer_practice.jpg', 0), (0,0), fx=0.75, fy=0.75)  # resize the image to half its size
template = cv2.resize(cv2.imread('Python_Libraries_Practice/opencv/basics/assets/shoe.PNG', 0), (0,0), fx=0.75, fy=0.75)  # resize the template image to half its size

h, w = template.shape # get the height and width of the template image

# Acccording to the OpenCV documentation, try different methods for template matching
# and see which one works best for your case
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    # Apply template Matching
    img2 = img.copy()  # create a copy of the original image to draw on
    result = cv2.matchTemplate(img2, template, method)
    
    # min_val: minimum value in the result, max_val: maximum value in the result
    # min_loc: location of the minimum value, max_loc: location of the maximum value
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, we take the minimum value
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location_top_left= min_loc
    else:
        location_top_left = max_loc

    # Draw a rectangle around the matched region, 
    # we add the width and height of the template to get the bottom right corner
    bottom_right = (location_top_left[0] + w, location_top_left[1] + h)

    # Draw a rectangle around the matched region
    cv2.rectangle(img2, location_top_left, bottom_right, 255, 2) # 255 is a black rectangle color, 2 is the thickness of the rectangle
    
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()