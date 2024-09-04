import cv2 as cv

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("Cats", img)


# Averaging
average = cv.blur(img, (7,7)) # (7,7) is the kernel size the value of any pixel is the average of the pixel values in the kernel, the bigger the kernel the more blur, the kernel must be odd
cv.imshow("Average Blur", average)


# Gaussian Blur # It produces less blur than averaging, but is more natural
gauss = cv.GaussianBlur(img, (7,7), 0) # (7,7) is the kernel size, 0 is the standard deviation, the pixel value is the weighted sum of the pixel values in the kernel
cv.imshow("Gaussian Blur", gauss)


# Median Blur # It is used to remove salt and pepper noise
median = cv.medianBlur(img, 3) # 3 is the kernel size, the pixel value is the median of the pixel values in the kernel, similar to averaging but, instead of taking average value of kernel, it takes the median value
cv.imshow("Median Blur", median)


# Bilateral # It is used to keep the edges sharp
bilateral = cv.bilateralFilter(img, 10, 15, 15) # 10 is the diameter of each pixel neighborhood, 15 is the sigma color, 15 is the sigma space , diameter of each pixel neighborhood can be thought of as the size of the filter, sigma color is the color space, sigma space is the coordinate space
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)