import cv2 as cv
import numpy as np


img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Grey", grey)

blur = cv.GaussianBlur(grey, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny1 = cv.Canny(img, 125, 175) # Canny edge detection is a popular edge detection algorithm. It was developed by John F. Canny in 1986.
canny2 = cv.Canny(blur, 125, 175)

cv.imshow("Canny1", canny1)
cv.imshow("Canny2", canny2)

contours1, hierarchies1 = cv.findContours(canny1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity. Contours are used for shape analysis and object detection and recognition
contours2, hierarchies2 = cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.RETR_EXTERNAL for external contours,
# cv.RETR_LIST for all contours,
# cv.RETR_CCOMP for all contours in 2-level hierarchy,
# cv.RETR_TREE for all contours in full hierarchy
# and
# cv.CHAIN_APPROX_SIMPLE for simple contours,
# cv.CHAIN_APPROX_NONE for all contours

print(f'{len(contours1)} contours found in normal image')
print(f'{len(contours2)} contours found in blurred image')

ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY) # cv.THRESH_BINARY for binary thresholding, it is used to convert the image to binary form (black and white), if the pixel value is greater than the threshold value, it is assigned the maximum value, else it is assigned the minimum value

cv.imshow("Thresh", thresh)


contours3, hierarchies3 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours3, -1, (0, 0, 255), 1) # -1 to draw all contours
cv.imshow("Contours Drawn For Thresh", blank)

contours4, hierarchies4 = cv.findContours(canny1, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours4, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn For Canny1", blank)


cv.waitKey(0)