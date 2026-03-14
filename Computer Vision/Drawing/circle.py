#cv2.circle(img , center , radius , color , thickness)
# if thickness = -1 --> it will fill the circle with color 

import cv2 

image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is None:
    print("Could not load the image")
else:
    print("Image loaded successfully")
    circle = cv2.circle(image , (150 , 60) , 30 , (90, 150 , 190) , 2)

    cv2.imshow("New image " , circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
