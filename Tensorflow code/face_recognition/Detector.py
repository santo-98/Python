import cv2 
import numpy as np 
import Execute
from tkinter import *
from tkinter import messagebox
top = Tk()  
  
top.geometry("100x100")      
face_cascade = cv2.CascadeClassifier('CascadeClassifier.xml')

cap = cv2.VideoCapture(0)
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor= 1.4, minNeighbors= 5)

    for (x,y,w,h) in faces:
        count = count+1
        roi_img = frame[y:y+h,x:x+w]
        # cv2.imwrite("Capture\\ Capture.png", frame)
        # cv2.imwrite("Dataset\\"+str(count)+".png",frame)
        print(count)
        break
        
    cv2.imshow('Face Detection', frame)
    name = Execute.Recognize() 
    messagebox.showinfo("information","Welcome to Skcript, "+name)  
  
    top.mainloop()

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()