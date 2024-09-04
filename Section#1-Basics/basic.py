import cv2 as cv

img = cv.imread("../Resources/Photos/cats 2.jpg")

#cv.imshow('Cat', img)


#Converting to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
# cv.waitKey(0)

# capture = cv.VideoCapture(0)
# while True:
#     isframe, frame = capture.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #Converting to grayscale
#     cv.imshow('GreyScale', gray)
#     cv.imshow('Video', frame)
#     if isframe:
#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break
#     else:
#         break



# Blur
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) #Kernel size should be odd numbers and higher the number, more the blur
# cv.imshow('Blur', blur)
# cv.waitKey(0)




# Edge Cascade

# cany = cv.Canny(img, 125, 175) #Threshold values
# cv.imshow('Canny', cany)
# cv.waitKey(0)

# capture = cv.VideoCapture(0)
# while True:
#     isframe, frame = capture.read()
#     cv.imshow('Color', frame)
#     cany = cv.Canny(frame, 125, 175) #Threshold values
#     cv.imshow('Canny', cany)
#     if isframe:
#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break
#     else:
#         break
# capture.release()
# cv.destroyAllWindows()



# Dilate
# cany = cv.Canny(img, 125, 175) #Threshold values
# dilated = cv.dilate(cany, (7,7), iterations=3) #Kernel size should be odd numbers and higher the number, more the blur and iterations is the thickness of the edges
# cv.imshow('Dilated', dilated)
# cv.waitKey(0)



# Erode
# eroded = cv.erode(cany, (3,3), iterations=2) #Kernel size should be odd numbers and higher the number, more the blur and iterations is the thickness of the edges
# cv.imshow('Eroded', eroded)
# cv.waitKey(0)


# Resize
# resized = cv.resize(img, (700, 700), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)
# cv.waitKey(0)

# Crop
# cropped = img[50:200, 200:400]
# cv.imshow('Orginal', img)
# cv.imshow("Cropped",cropped)
# cv.waitKey(0)

