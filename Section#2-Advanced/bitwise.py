import cv2 as cv
import numpy as np

blank = np.zeros([400, 400], dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1) # 30, 30 is the top left corner, 370, 370 is the bottom right corner,-1 to fill the rectangle, 255 is the color
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1) # 200, 200 is the center of the circle, 200 is the radius, -1 to fill the circle, 255 is the color

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


# Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)


# Bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)


# Bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)


# Bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)