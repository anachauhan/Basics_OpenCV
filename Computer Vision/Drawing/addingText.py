#cv2.putText(img , text , org , font , fontScale , color , thickness)
#org --> top left corner of the text
import cv2 

image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is None:
    print("Error")
else:
    print("Image loaded successfully")

    adText = cv2.putText(image , "Mount Fuji" , (50 , 40) 
                         , cv2.FONT_HERSHEY_COMPLEX , 1.2, (0, 20 , 255) ,2)

    cv2.imshow("Adding text" , adText)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
