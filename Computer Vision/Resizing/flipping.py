#cv2.fip(image , flipscale)
# flipscale ->  0 = vertically (top to bottom) ,   1 = horizontally (left to right)  , -1 = both (horizontally & vertically)

import cv2
image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is None:
    print("Could not load the image")
else:
    flipped_horizontal = cv2.flip(image , 1)
    flipped_vertical = cv2.flip(image , 0)
    flipped_both = cv2.flip(image , -1)

    cv2.imshow("Original " , image)
    cv2.imshow("Flipped Horizontal" , flipped_horizontal)
    cv2.imshow("Flipped Vertical" , flipped_vertical)
    cv2.imshow("Flipped Both " , flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

