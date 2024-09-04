import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cats", img)


blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank Image", blank)


# circle = cv.circle(blank, (img.shape[1]//2 -150, img.shape[0]//2 - 50), 100, 255, -1)
# rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2-75, img.shape[0]//2 - 100), (img.shape[1]//2 + 200, img.shape[0]//2 + 100), 255, -1)
# mask = cv.bitwise_or(circle, rectangle)


# fix the errors in the next line
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Circle", circle)
mask = circle
cv.imshow("Mask", mask)


masked = cv.bitwise_and(img, img, mask=mask) # mask is the circle we created, img is the image we want to apply the mask to
cv.imshow("Masked Image", masked)

cv.waitKey(0)