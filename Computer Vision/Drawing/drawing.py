#1. Draw a line --- cv2.line()
#cv2.line(img , pt1 , pt2 , color_of_line , thickness)    ------ pt1 = (50,100) => 50 -right , 100-down; pt2 = (300, 100)

import cv2
image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is None:
    print("Error!")
else:
    print("Image loaded successfully")
    line = cv2.line(image , (50,20) , (80 , 20) , (255,0,0) ,4 )
    pt1 = (20 , 100)
    pt2 = ( 180 , 100)
    line2 = cv2.line(image , pt1 , pt2 , (0,0 , 255) , 2)

    cv2.imshow("Lined" , line)
    cv2.imshow("Lined" , line2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
