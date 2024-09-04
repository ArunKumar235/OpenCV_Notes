import cv2 as cv


# Read image using OpenCV

# img = cv.imread('../Resources/Photos/cat.jpg') #Reads the image
# cv.imshow('Cat', img) #Shows the image in a window
# cv.waitKey(0) #Waits for any key press to close the window


#Read Video using OpenCV
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read() #Reads the video frame by frame, isTrue is a boolean value which tells if the frame is read or not, frame is the data in frame itself
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'): #Waits 20 ms for any key press and if 'd' is pressed, it breaks the loop
        break
capture.release() #Releases the video capture
cv.destroyAllWindows() #Closes all the windows