import cv2

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter("video.avi",codec,20.0,(int(cap.get(3)),int(cap.get(4))))


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    resize_gray = cv2.resize(gray,(640,480))
    width = cap.get(3)
    print("width: ",width)
    height = cap.get(4)
    print("height: ",height)


    cv2.imshow("Gray",gray)
    # cv2.imshow("Frame",frame)
    out.write(gray)

    if cv2.waitKey(25) and 0xFF == ord('q'):
        break


cv2.release()
out.release()

cv2.destroyAllWindows()