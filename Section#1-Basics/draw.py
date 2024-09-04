import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #Creates a blank image of 500x500 pixels with black background uint8 is the data type of the image 3 is the number of channels which is BGR


#cv.imshow('Blank', blank) #Shows the blank image


#1. Paint the image a certain color
# blank[:] = 0,0,255 #Paints the image red
# cv.imshow('Red', blank)

# blank[200:300, 300:400] = 0,0,255 #Paints a rectangle in the image red
# cv.imshow('Red', blank)

# cv.waitKey(0) #Waits for any key press to close the window


#2. Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2) #Draws a rectangle on the image from (0,0) to (250,250) with green color and thickness 2
##cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED) #Draws a filled rectangle on the image from (0,0) to (250,250) with green color #-1 can also be used instead of cv.FILLED
# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=2) #Draws a filled circle on the image at the center with radius 40 and red color
# cv.imshow('Circle', blank)
# cv.waitKey(0) 

#4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3) #Draws a line on the image from (0,0) to (250,250) with white color and thickness 3
# cv.imshow('Circle', blank)
# cv.waitKey(0) 

#5. Write text
cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2) #Writes the text on the image at the given position with the given font and thickness
# cv.imshow('Text', blank)
# cv.waitKey(0)