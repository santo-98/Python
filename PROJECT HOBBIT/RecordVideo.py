# Python program to save a 
# video using OpenCV 


import cv2 

video = cv2.VideoCapture(0) 

if (video.isOpened() == False): 
	print("Error reading video file") 

frame_width = int(video.get(3)) 
frame_height = int(video.get(4)) 

size = (frame_width, frame_height) 

result = cv2.VideoWriter('filename.avi', 
						cv2.VideoWriter_fourcc(*'MJPG'), 
						10, size) 

human_cascade = cv.CascadeClassifier("haarcascade_upperbody.xml")
	
while(True): 
	ret, frame = video.read() 

	if ret == True: 
		result.write(frame) 

		human = human_cascade.detectMultiScale(gray, 1.1, 4)

		for (x,y,w,h) in human:
      cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),3)
      img = frame[y:y+h, x:x+w]
      cv.imshow("Cropped", img)
			
		if cv2.waitKey(1) == ord('q'): 
			break

	# Break the loop 
	else: 
		break

# When everything done, release 
# the video capture and video 
# write objects 
video.release() 
result.release() 
	
# Closes all the frames 
cv2.destroyAllWindows() 

print("The video was successfully saved") 
