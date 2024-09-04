import cv2 as cv

img = cv.imread("../Resources/Photos/group 2.jpg")
cv.imshow("Group of 5 people", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


haar_cascade = cv.CascadeClassifier("./haar_face.xml") # Load the cascade


faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6) # Detect the faces , scaleFactor is the factor by which the image is reduced.
# minNeoghbors is the number of neighbors each candidate rectangle should have to retain it, higher value results in less detections but with higher quality.

print(f"Number of faces found = {len(faces_rect)}")


for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    print(x, y, w, h)

cv.imshow("Detected Faces", img)

cv.waitKey(0)