import cv2
#import sys

img = cv2.imread('2.jpeg')
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    
)
print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    ww=w-60
    hh=h-5
    cv2.putText(img,"Sara",(x+ww,y+hh),cv2.FONT_HERSHEY_DUPLEX,0.4,(255,0,0),1)
cv2.imshow("Faces found", img)
cv2.waitKey(0)
