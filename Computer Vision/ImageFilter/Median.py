#Gaussian Blur --> average of neighbour values  -- smooth , soft
#Median Blur --> middle value of neighbour pixels  -- Random blur

import cv2
image = cv2.imread("E:\DeepDive\Computer Vision\clear_image.jpg")

blurred = cv2.medianBlur(image , 11)

cv2.imshow("Original Image " , image)
cv2.imshow("Blurred Image " , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()