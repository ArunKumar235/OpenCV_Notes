import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isframe, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video", gray)

    haar_cascade = cv.CascadeClassifier("./haar_face.xml")
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        print(x, y, w, h)
    cv.imshow("Detected Faces", gray)

    if isframe:
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()