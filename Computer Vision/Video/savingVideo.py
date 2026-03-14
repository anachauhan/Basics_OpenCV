# cv2.VideoWriter()    

#----------------Level1---------------
#VideoCapture(0)   --> camera open
# VideoWriter()    --> save video
# .release()       --> exit

#----------------Level2---------------
# 1. start -> open camera
# 2. tell width and height
# 3. save the video captured
# 4. show the frames
# 5. 'q' = quit

#avi --> audio video interleave     using XVID codec
#cv2.VideoWriter(filename , codec , fps , frame_size)               
# --> codec = compression format (.avi / .mps)
#fps => frames per sec ,    frame_size = (w, h)

import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
                                                #fourcc => four character code
codec = cv2.VideoWriter_fourcc(*'XVID')         #XVID ->.avi format , MP4V => mp4 format  , MJPG =>Motion JPEG

recorder = cv2.VideoWriter("My_video.avi" , codec , 20 ,(frame_width,frame_height))

while True:
    success , image= camera.read()

    if not success:
        break

    recorder.write(image)
    cv2.imshow("Recording live" , image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
