import cv2
import numpy as np
import imutils
import time
capture=cv2.VideoCapture(1,cv2.CAP_DSHOW)
height=int(capture.get(4))
width=int(capture.get(3))
while True:

    ret,frame=capture.read()
    #test result with gaussian blur
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower=np.array([35,70,50])
    upper=np.array([80,255,255])

    mask=cv2.cv2.inRange(hsv,lower,upper)
    #test with erode and dilate

    contours=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(contours)  #test with grab countour function
    centre=None
    file = open("ball_detection_data.txt", "w")

    if len(contours)>0:
        c=max(contours,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


        if radius>5:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)
            font = cv2.FONT_ITALIC
            cv2.putText(frame, "x= " + str(int(x)) + " y= " + str(height-int(y)) + " colour is" + str(frame[round(y)][round(x)]), (10, height - 10), font, 0.5, (0, 0, 255), 1)
            file.write(str(time.ctime()) + " x= " + str(int(x)) + " y= " + str(int(height - y)) + " colour is" + str(frame[round(y)][round(y)]) + "\n")

    cv2.imshow("u", frame)

    if cv2.waitKey(1) == ord("q"):
        break
file.close()
capture.release()
cv2.destroyAllWindows()