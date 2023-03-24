import cv2
import numpy as np

img1 = cv2.imread('logoOpenCV.png')
img2 = cv2.imread('logoOpenCV.png') 
img3 = cv2.imread('logoOpenCV.png') 
img4 = cv2.imread('logoOpenCV.png')  

SecondOverlay = img2.copy()
ThirdOverlay = img3.copy()
FourthOverlay = img4.copy()

cv2.addWeighted(SecondOverlay, 1, img1, 2, 0, img2)
cv2.addWeighted(ThirdOverlay, 1, img2, 2, 0, img3)
cv2.addWeighted(FourthOverlay, 1, img3, 2, 0, img4)

cv2.imwrite("Merged.png", img4)
cv2.imshow("Merged.png", img4)
cv2.waitKey(0)

img = cv2.imread('Merged.png') 

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
circles = np.array([])

circles = cv2.HoughCircles(grayimg,cv2.cv.CV_HOUGH_GRADIENT, 1, 4, circles, param1=10, param2=7, minRadius=0, maxRadius =  10)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(grayimg,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(grayimg,(i[0],i[1]),2,(0,0,255),3)
    print "Center Colour (Of Feature)", img[i[1], i[0]]

print(circles)
cv2.imshow('HoughCircled Merged Grayscale',grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
