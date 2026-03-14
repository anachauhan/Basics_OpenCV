#Image Filtering process ->
# Goal -> image softening/smoothening , noise removal , etc
# 1. Blurring -> removing unwanted sharphness  -> Gaussian Blur , Median blur , Bilateral Blur , Normal blur
# 2. Noise 
# 3. Smoothening -> resolution ->high
# 4. Kernel


#----Gaussian Blur----
#blurred_image = cv2.GaussianBlur(image , (kernel_size_x , kernel_size_y), sigma)
# kernel_size_x or y -> (odd , odd)   ==> (3,3) -> light blur   , (9,9) -> strong blur ,(21,21) -> super blur
#sigma => 0-> opencv itself detect the amount to be blurred

import cv2
image = cv2.imread("E:\DeepDive\Computer Vision\clear_image.jpg")

blurred = cv2.GaussianBlur(image ,(7,7) , 1)
 
cv2.imshow("Original Image" , image)
cv2.imshow("Blurred Image" , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()