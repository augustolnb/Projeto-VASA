import cv2
import numpy as np

# Builds an image of merged images #

# Reads in the images to be merged #

img1 = cv2.imread('logoOpenCV.png')
img2 = cv2.imread('logoOpenCV.png') 
img3 = cv2.imread('logoOpenCV.png') 
img4 = cv2.imread('logoOpenCV.png')  

# Copies the images #

SecondOverlay = img2.copy()
ThirdOverlay = img3.copy()
FourthOverlay = img4.copy()


# Add overlay onto the image #

cv2.addWeighted(SecondOverlay, 1, img1, 2, 0, img2)
cv2.addWeighted(ThirdOverlay, 1, img2, 2, 0, img3)
cv2.addWeighted(FourthOverlay, 1, img3, 2, 0, img4)


# Write image to be used #

cv2.imwrite("Merged.png", img4)
cv2.imshow("Merged.png", img4)
cv2.waitKey(0)

### Initial images are read in as BGR   ###
img = cv2.imread('Merged.png')  #Reads in the merged image

### Converts & Saves images read in from BGR to grayscale   ###
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

### Converts & Saves images read in from BGR to HSV ###
hsvimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)



circles = np.array([]) # Declares the arrays that will store


circles = cv2.HoughCircles(grayimg,cv2.cv.CV_HOUGH_GRADIENT, 1, 4, circles, param1=10, param2=7, minRadius=0, maxRadius =  10)
circles = np.uint16(np.around(circles))



for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(grayimg,(i[0],i[1]),i[2],(0,255,0),2) # gray img or img works?
    # draw the center of the circle
    cv2.circle(grayimg,(i[0],i[1]),2,(0,0,255),3)
    print "Center Colour (Of Feature)", img[i[1], i[0]]# prints the color
print(circles) # prints entire x and y coords of the cirlces found

cv2.imshow('HoughCircled Merged Grayscale',grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
