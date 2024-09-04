import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../Resources/Photos/cats 2.jpg")
cv.imshow("Cats", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


blank = np.zeros(img.shape[:2], dtype="uint8")
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)


#Grey Scale histogram

# mask = cv.bitwise_and(gray, gray, mask = circle)
# cv.imshow("Mask", mask)
#
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256]) # calcHist expects a list of images, a list of channels, a mask, a list of the number of bins, a list of the range of the bins and returns a histogram for each channel in the image
# # x-axis is going to be the bins, y-axis is going to be the number of pixels in each bin
# # bins are the number of buckets we want to divide the range of the pixel values into
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()



# Color Histogram

mask = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow("Mask", mask)

plt.figure() # create a new figure
plt.title("Color Histogram") # title of the figure
plt.xlabel("Bins") # x-axis label
plt.ylabel("# of Pixels") # y-axis label
colors = ("b", "g", "r") # colors we want to plot
for i,col in enumerate(colors): # enumerate returns the index and the value of the colors
    hist = cv.calcHist([img], [i], mask, [256], [0, 256]) # calculate the histogram for each channel
    plt.plot(hist, color = col) # plot the histogram
    plt.xlim([0, 256]) # set the x-axis limits
plt.show() # show the plot


cv.waitKey(0)