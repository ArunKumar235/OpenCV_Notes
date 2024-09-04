import cv2 as cv

img = cv.imread("../Resources/Photos/cats 2.jpg")
cv.imshow("Cats", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # threshold is the same value passed as parameter, thresh is the image
cv.imshow("Simple Threshold", thresh)

threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) # threshold is the same value passed as parameter, thresh is the image
cv.imshow("Simple Threshold Inverse", thresh_inv)


# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)