import cv2
'''print(img.size)
print(img.shape)
print(img.dtype)'''
img = cv2.imread("opencv-master\samples\data\lena.jpg",1)

extimg = img[250:260,259:270]
img[180:190,189:200] = extimg 
cv2.imshow('img', img)
cv2.waitKey(0)
