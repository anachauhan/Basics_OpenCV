#sharpening --> to clear the softness -> to make it sharp
#cv2.filter2D(src , depth , kernel)
#depth = -1 --> same as it is           , kernel = 3*3 matrix

import numpy as np
import cv2
image = cv2.imread("E:\DeepDive\Computer Vision\low_resol.jpg")

sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharpened = cv2.filter2D(image , -1, sharpen_kernel )

cv2.imshow("Original Image:" , image)
cv2.imshow("Sharpened Image:" , sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
