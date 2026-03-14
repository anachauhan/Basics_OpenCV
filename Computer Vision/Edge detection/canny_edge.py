"""
IMPORTANT ---> Canny edge detection - take out outline of the image
image theshold - complex image -clean , black , white image -- object detection
Bitwise Operations 

edges = cv2.Canny(image , threshold 1, threshold2)

#uses - Detect border , seperate objects  , feature extraction 
#threshold1 - lower boundary to detect weak edges   , threshold2 = upper boundary to detect strong edges
#threhold --> if value is just above threhold and the color is white --> make it complete white
# or if the value is just below the threhold --> make it complete black
"""

import cv2 

img = cv2.imread("E:/DeepDive/Computer Vision/flower.jpg" , cv2.IMREAD_GRAYSCALE)           #turn it into black and white
img = cv2.resize(img , (300 , 300))

edge = cv2.Canny(img , 50 , 150)
edge = cv2.resize(edge , (300 , 300))

cv2.imshow("Original " , img)
cv2.imshow("Edges" , edge)
cv2.waitKey(0)
cv2.destroyAllWindows()

