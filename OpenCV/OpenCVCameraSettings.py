import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT),' - ' ,cap.get(cv.CAP_PROP_FRAME_WIDTH))

cap.set(3, 1980)
cap.set(4,1080)

print(cap.get(cv.CAP_PROP_FRAME_HEIGHT),' - ' ,cap.get(cv.CAP_PROP_FRAME_WIDTH))
while(cap.isOpened()):
    ret, frame = cap.read()
    cv.imshow('CAPTURE', frame)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()