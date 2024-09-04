import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("Park", img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b,g,r = cv.split(img)
# Darker the color, the more the concentration of that color
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)


blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue picture", blue)
cv.imshow("Green picture", green)
cv.imshow("Red picture", red)


print(img.shape) # 3 channels (BGR)
print(b.shape) # 1 channel (B)
print(g.shape) # 1 channel (G)
print(r.shape) # 1 channel (R)

merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

print(merged.shape) # 3 channels (BGR)

cv.waitKey(0)