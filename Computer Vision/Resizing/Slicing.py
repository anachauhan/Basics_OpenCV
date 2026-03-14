#cropped_img = image[startY: endY , startX: endX]

import cv2

image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is not None:
    cropped = image[50:300 , 0:200]
    
    cv2.imshow("Original " , image)
    cv2.imshow("Cropped image" , cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
