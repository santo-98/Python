import cv2 as cv
import numpy as np


cap = cv.VideoCapture("Sample2.avi")
human_cascade = cv.CascadeClassifier("haarcascade_upperbody.xml")
 
for i in range(60):
  ret, bgframe = cap.read()

bgframe = np.flip(bgframe, axis=1)
# print(bgframe)
# cv.imwrite("test.jpg", bgframe)
while(cap.isOpened()):
  ret, frame = cap.read()
  frame = np.flip(frame, axis=1)
  gray = cv.cvtColor( frame, cv.COLOR_BGR2GRAY)
  

  human = human_cascade.detectMultiScale(gray, 1.1, 4)
  if len(human) > 0:
    # edges = cv.Canny(frame,150,200)
    # contours, hierrachy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # cv.imshow("Canny", edges)

    for (x,y,w,h) in human:
      # frame = cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,0),3)
      gray[y:y+h, x:x+w] = 255
      ret, mask = cv.threshold(gray, 250, 255, cv.THRESH_BINARY)
      mask_inv = cv.bitwise_not(mask)
      # # mask = gray
      img1 = cv.bitwise_and(bgframe,bgframe,mask=mask)
      img2 = cv.bitwise_and(frame,frame,mask=mask_inv)

      output = cv.addWeighted(img1,1,img2,0.7,0)
      # output = cv.add(img1,img2)
      # mask = frame[y:y+h, x:x+w]
      # img = frame[y:y+h, x:x+w]
      cv.imshow("Cropped", img1)
      cv.imshow("Cropped1", output)

    # for cnt in contours:
    #   print(cnt)
    #   print("-------------------------")
    #   size = cv.contourArea(cnt)
    #   print(size)
    #   if size > 100:
    #     cv.drawContours(frame, [cnt], -1, (255,0,0), 3)

  cv.imshow("Frame", frame)
  if cv.waitKey(1)==ord("q"):
    break
cap.release()
# result.release()
cv.destroyAllWindows()