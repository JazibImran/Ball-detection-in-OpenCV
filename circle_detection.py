import numpy as np
import cv2

capture=cv2.VideoCapture(1,cv2.CAP_DSHOW)

while True:
    ret,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    circle=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.2,400)
    if circle is not None:
        circle=np.round(circle[0,:].astype("int"))
        for (x,y,r) in circle:
            cv2.circle(frame,(x,y),r,(255,0,0),4)

    cv2.imshow("window",frame)
    if cv2.waitKey(1) == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()

