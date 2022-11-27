import numpy as np
import cv2
import time
capture=cv2.VideoCapture(1,cv2.CAP_DSHOW)

while True:


    ret, img = capture.read()
    cv2.imshow("unprocessed",img)

    cv2.imwrite('positive/{}.jpg'.format(time.time()), img)
    time.sleep(0.4)
    if cv2.waitKey(1)==ord("q"):
        cv2.destroyAllWindows()
        break




capture.release()
