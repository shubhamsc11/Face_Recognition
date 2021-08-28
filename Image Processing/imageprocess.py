#read image
import cv2

img = cv2.imread("C:/Users/shubham singh/Downloads/face_detection/Inputs/test1.jpg")

print(img)

cv2.imshow('Image', img)

# cv2.waitKey(0)

res = cv2.waitKey(0)

# if res == 27:

if res == ord('q'):
    cv2.destroyAllWindows()




# Basic Function to test with images:-

import cv2

import numpy as np

img = cv2.imread("C:/Users/shubham singh/Downloads/face_detection/Inputs/test1.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

imgCanny = cv2.Canny(img, 100, 100)

# im = np.ones((500,500),np.uint8)


kernal = np.ones((5, 5), np.uint8)

imgDilation = cv2.dilate(imgCanny, kernal, iterations=1)

# Erode is opposit of Dilation

imgEroded = cv2.erode(imgDilation, kernal, iterations=1)

# cv2.imshow("IM",im)

cv2.imshow("Image ", img)
cv2.imshow("Gray Image ", imgGray)

cv2.imshow("Blur Image ", imgBlur)
cv2.imshow("Canny Image ", imgCanny)
cv2.imshow("Eroded Image ", imgEroded)

cv2.imshow("Dilation Image ", imgDilation)

cv2.waitKey(0)

cv2.destroyAllWindows()
