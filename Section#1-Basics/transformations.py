from token import LEFTSHIFT

import cv2 as cv
import numpy as np
img = cv.imread("../Resources/Photos/park.jpg")

cv.imshow("Orginal", img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # Translation matrix for x and y axis, float32 is the datatype of the matrix
    dimensions = (img.shape[1], img.shape[0]) # Width and height of the image
    return cv.warpAffine(img, transMat, dimensions) # Applying the transformation to the image using warpAffine function

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# translated = translate(img, 100, 100)
# cv.imshow("Translated", translated)


# Rotation
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2] # Getting the height and width of the image
    if rotPoint is None:
        rotPoint = (width//2, height//2) # If the rotation point is not provided, then the rotation point will be the center of the image
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # Getting the rotation matrix
    dimensions = (width, height) # Width and height of the image
    return cv.warpAffine(img, rotMat, dimensions) # Applying the transformation to the image using warpAffine function

# roateted = rotation(img, 45)
# cv.imshow("Rotated", roateted)



# Resizing
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # Resizing the image to 500x500
# cv.imshow("Resized", resized)


# Flipping
# flip = cv.flip(img, 0) # 0 - Flip vertically, 1 - Flip horizontally, -1 - Flip both vertically and horizontally
# cv.imshow("Flipped", flip)


# Cropping
# cropped = img[100:200, 200:400] # Cropping the image from 200 to 400 pixels in height and 300 to 400 pixels in width
# cv.imshow("Cropped", cropped)




cv.waitKey(0)