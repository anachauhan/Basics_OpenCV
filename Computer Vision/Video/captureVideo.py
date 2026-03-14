#cap = cv2.VideoCapture(source)          ---> read the frame
#source -> 0= computer / laptop webcam
#          1 = external webcam

import cv2 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()     # ret = return True/False  frame = image

    if not ret:
        print("Could not read frame")
        break
    
    cv2.imshow("WebCam Feed" , frame)
                                                        #0xFF --> bitwise AND op. for carefully checking
    if cv2.waitKey(1) & 0xFF == ord('q'):               #ord -> ASCII number  ; waitKey(1) = wait for 1 milisecond
        print("Quitting ....")
        break

cap.release()
cv2.destroyAllWindows()
