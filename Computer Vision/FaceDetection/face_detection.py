"""
Start --> Haar Cascades --> 1. Face  2. Eye  3. Smile detection --> Draw Boxes --> End
Problem statements (of computer)-->
1. didn't understand faces
2. manual marking for faces
3. Consistent & fast detection was not possible 
--> then comes Haar cascades   ----> pre trained ai face detector
1. Face detection
2. Real time (fast)
3. without internet 

requirements -->
1. webcam    2 . opencv install   3. Haar XLM file(pre trained ai model)

"""
"""
    detectMultiScale() --> scan & & detect faces
    1.1 --> scaleFactor  (zoom 10 % smaller)
    5 --> min Neighbours  --> safe checking .......... 3-> loose checking ........... 6 or more--> strict checking
"""
"""
        x , y- top - left corner
        face ={
        (100 , 150 , 80 , 80)   face 1 --->  x = 100 , y= 150 , 80x80
        (250 , 120 ,90 , 90)    face 2  ---> x = 250 , y= 120 , 90x90
        }
        
        x - how far from left
        y- how far from top
        w- width of face
        h - height of face
"""

import cv2

face_cascade = cv2.CascadeClassifier("FaceDetection/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True: 
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray , 1.1 , 5)
    
    for (x , y , w ,h) in faces:
        cv2.rectangle(frame , (x,y) , (x+w , y+h) , (0 , 255 ,0) , 2)

    cv2.imshow("Webcam face detection" , frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
    