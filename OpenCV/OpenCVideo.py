import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),"-",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('VIDEO CAPTURE', gray)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
