import cv2
import numpy as np
import datetime
import time
#run cascade_training.py to write neg.txt file, then import to terminal and run



# Highlight target objects using function below
# C:\Users\jazib\Desktop\Aerospace\Python\Giraffe\opencv\build\x64\vc15\bin\opencv_annotation.exe -annotations=pos.txt --images=positive/
#
# create pos.vec
# C:\Users\jazib\Desktop\Aerospace\Python\Giraffe\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
#
# train
# C:\Users\jazib\Desktop\Aerospace\Python\Giraffe\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 24 -numPos 300 -numNeg 800 -numStages 10
#
# C:\Users\jazib\Desktop\Aerospace\Python\Giraffe\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade2/ -vec pos2.vec -bg neg.txt -w 24 -h 24 -numPos 300 -numNeg 800 -numStages 10




capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)
ball_cascade=cv2.CascadeClassifier("cascade/cascade.xml")

height=int(capture.get(4))
file=open("ball_detection_data.txt", "w")
while True:
    ret,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ball=ball_cascade.detectMultiScale(gray,5,7)
    if len(ball) == 0:
        file.write(str(time.ctime()) + "...\n")

    for (x,y,h,w) in ball:
        #print(sum(frame[y:y+h][x+x+w]))
        #colour=(sum(frame[y:y+h][x+x+w]))/(len(frame[y:y+h][x+x+w]))

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)

        font = cv2.FONT_ITALIC
        cv2.putText(frame, "x= " + str(x + 0.5 * w) + " y= " + str(height-(y + 0.5 * h)) + " colour is" + str(frame[round(y + 0.5 * h)][round(x + 0.5 * w)]), (10, height - 10), font, 0.5, (0, 0, 255), 1)
        file.write(str(time.ctime())+" x= " + str(x + 0.5 * w) + " y= " + str(height-(y + 0.5 * h)) + " colour is" + str(frame[round(y + 0.5 * h)][round(x + 0.5 * w)])+"\n")
    cv2.imshow("frame",frame)
    if cv2.waitKey(1)==ord("q"):
        break
file.close()
capture.release()
cv2.destroyAllWindows()