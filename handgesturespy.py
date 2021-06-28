import cv2
cap = cv2.VideoCapture(0)
while True:
    r,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (45,45), 0 )
    print(r)
    cv2.imshow("frame", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Blur", blur)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


