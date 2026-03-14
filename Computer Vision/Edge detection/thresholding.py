#threhold_img = cv2.threshold(image , thresh_value , max_value , method)
#image --> input grayscale image      # thresh_value = 0-255    # max_value = 255   
# #method = THRESH BINARY  --> if value is greater than thresh_value --> make it 255 otherwise 0

import cv2

img = cv2.imread("E:\DeepDive\Computer Vision\cameraman.jpg", cv2.IMREAD_GRAYSCALE)

ret , thresh_img =cv2.threshold(img , 120 , 255 , cv2.THRESH_BINARY)

cv2.imshow("Original Image " , img)
cv2.imshow("Threshold_Image" , thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
90 -> 0 black
130 -> 255 white
180 - 255 white
50 -> 0 black

try these values for threshold --> 100, 120 , 150   to find the best of the image
"""