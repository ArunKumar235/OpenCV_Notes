import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("Park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F) # cv.CV_64F is a data type that can store negative values, cv.Laplacian is a function that takes in an image and returns the laplacian of the image
lap = np.uint8(np.absolute(lap)) # np.absolute returns the absolute value of the laplacian, np.unti8 converts the laplacian to a data type that can be displayed
cv.imshow("Laplacian", lap)


# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # cv.Sobel is a function that takes in an image, a data type, and the x and y derivatives
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # cv.Sobel gives the derivative of the image in the x and y directions
combined_sobel = cv.bitwise_and(sobelx, sobely)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)