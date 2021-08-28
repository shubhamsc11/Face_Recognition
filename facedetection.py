Face Detection with Python using OpenCV:-

Import the OpenCV library
import cv2

Using the pre-trained classifier from OpenCV
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Load the cascade

Upload the imput image
img = cv2.imread('test4.jpg') #Read the input image

Perform face detection
faces = face_cascade.detectMultiScale(img, 1.1, 4) #Detect faces

Drawing rectangle around the faces
#Draw rectangle around the faces
for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

Exporting the image file
#Export the result
cv2.imwrite("face_detected.png", img) 
print('Photo successfully exported!')

"Photo successfully exported!"