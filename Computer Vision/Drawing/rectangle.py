import cv2

image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is None:
    print("Error! Could not load")
else:
    print("Image loaded successfully")
    pt1 = (100,30)
    pt2 = (200 , 100)
    color = (0 , 0 ,255)
    thickness = 3

    rect = cv2.rectangle(image , pt1 , pt2 , color , thickness)

    cv2.imshow("New image" , rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
