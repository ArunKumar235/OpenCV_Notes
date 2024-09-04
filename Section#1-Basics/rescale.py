import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #Works for images, video and live
    #print(frame.shape) #Prints the shape of the frame which is a tuple of height, width and number of channels
    height = int(frame.shape[0] * scale) #frame.shape[0] gives the height of the frame
    width = int(frame.shape[1] * scale) #frame.shape[1] gives the width of the frame
    dimensions = (width, height) #dimensions is a tuple of width and height
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #Resizes the frame to the given dimensions using INTER_AREA interpolation  method  which is used when we need to shrink an image or when we need to downscale an image


def changeRes(width, height):
    #Works for live video only
    capture.set(3, width) 
    capture.set(4, height) 
    


# img = cv.imread('../Resources/Photos/cat_large.jpg') #Reads the image
# resized = rescaleFrame(img, scale=0.75)
# cv.imshow('Cat', img)
# cv.imshow('Cat', resized)
# cv.waitKey(0)



# capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
# while True:
#     isframe, frame = capture.read()
#     resized = rescaleFrame(frame, scale=0.2)
#     if isframe:
#         #cv.imshow('Video', frame)
#         cv.imshow('Video', resized)
#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break
#     else:
#         break

# capture.release()
# cv.destroyAllWindows()


# capture = cv.VideoCapture(0) #0 is the default camera
# while True:
#     isframe, frame = capture.read()
#     #changeRes(640, 480)
#     if isframe:
#         cv.imshow('Video', frame)
#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break
#     else:
#         break
# capture.release()
# cv.destroyAllWindows()