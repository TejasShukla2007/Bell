import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

cap = cv2.VideoCapture(0)

while cap.isOpened():
    r,frame = cap.read()
    cv2.rectangle(frame,(300,300),(100,100),(255,255,0),2)
    cropped_frame = frame[100:300,100:300]
    gray_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray_frame, (35,35), 0)
    t,thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contour,_ = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    maxcontour = max(contour,key = lambda x: cv2.contourArea(x))
    for c in contour:
        area = cv2.contourArea(c)
        print(area)
    print(maxcontour)
    x,y,w,h = cv2.boundingRect(maxcontour)
    cv2.rectangle(cropped_frame,(x,y),(x+w,y+h),(255,0,0),2)
    hull = cv2.convexHull(maxcontour)
    i = np.zeros(cropped_frame.shape,np.uint8)
    cv2.drawContours(i,[maxcontour],0,(0,255,255),2)
    cv2.drawContours(i,[hull],0,(0,0,255),2)
    hull = cv2.convexHull(maxcontour,returnPoints=False)
    defects = cv2.convexityDefects(maxcontour,hull)
    print(defects)
    cv2.drawContours(thresh,contour,-1,(255,0,0),2)
    countdefects = 0
    for j in range(defects.shape[0]):
        s,e,f,d = defects[j,0]
        start = tuple(maxcontour[s][0])
        end = tuple(maxcontour[e][0])
        far = tuple(maxcontour[f][0])

    a = math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
    b = math.sqrt((far[0]-start[0])**2 + (far[1]-start[1])**2)
    c = math.sqrt((end[0]-far[0])**2 + (end[1]-far[1])**2)
    angle = (math.acos((b**2 + c**2 - a**2)/(2*b*c))*180)/3.14
    if angle <= 90:
        countdefects += 1
        cv2.circle(cropped_frame,far,1,[0,0,245],-1)
    cv2.line(cropped_frame,start,end,[0,255,0],2)
    if area>1300:
        cv2.putText(frame,"Put your hand in the frame",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
    else:

        if countdefects == 0:
            cv2.putText(frame,"Best of luck",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        elif countdefects == 1:
            cv2.putText(frame,"Peace",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        elif countdefects == 2:
            cv2.putText(frame,"Nice",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        elif countdefects == 3:
            cv2.putText(frame,"Four",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
        else:
            cv2.putText(frame,"Wait",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),5)
    print(a)
    print(i.shape)
    print(cropped_frame.shape)
    cv2.imshow("frame",frame)
    allimage = np.hstack((i,cropped_frame))
    cv2.imshow("Final",allimage)

    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
