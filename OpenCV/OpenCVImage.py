import cv2
img = cv2.imread("opencv-master\samples\data\lena.jpg",1)
cv2.imshow("Test",img)
while(True):
    if cv2.waitKey(0) == ord('s'):
        cv2.imwrite("test.png", img)
        print('Done')
        cv2.destroyAllWindows()
        break
    
        