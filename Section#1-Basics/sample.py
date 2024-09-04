import cv2 as cv
import numpy as np

# capture = cv.VideoCapture(0)
#
# blank = np.zeros((500,500,3), dtype='uint8')
#
# while True:
#     blank = np.zeros((500, 500, 3), dtype='uint8')
#     isframe, frame = capture.read()
#     # cv.imshow("Video", frame)
#     canny = cv.Canny(frame, 125, 175)
#     cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#     cv.imshow("Canny", canny)
#     contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#     cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
#     cv.imshow("Contours Drawn", blank)
#     if isframe:
#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break
#     else:
#         break



capture = cv.VideoCapture(0)
while True:
    isframe, frame = capture.read()
    b,g,r = cv.split(frame)
    blank = np.zeros(frame.shape[:2], dtype='uint8')
    blue = cv.merge([b, blank, blank])
    green = cv.merge([blank, g, blank])
    red = cv.merge([blank, blank, r])
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Blue picture", blue)
    cv.imshow("Green picture", green)
    cv.imshow("Red picture", red)
    cv.imshow("Grey picture", grey)
    cv.imshow("Color picture", frame)
    if isframe:
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break



cv.destroyAllWindows()