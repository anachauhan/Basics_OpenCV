# M = cv2.getRotationMatrix2D(center , angle , scale)
#center = (width//2 , height//2)            # scale ->  1.0 = same ,   0.5 = half ,   2.0 = double
#rotated = cv2.warpAffine(image ,M , (width , height))

#width = center horizontally
#height = center vertically

import cv2
image = cv2.imread("E:\DeepDive\Computer Vision\mountain.jpg")

if image is None:
    print("Could not load image")
else:
    (h , w) = image.shape[:2]

    center = (w//2 , h//2)
    M = cv2.getRotationMatrix2D(center , 90 , 0.5)
    rotated = cv2.warpAffine(image , M , (w,h))

    cv2.imshow("Original" , image)
    cv2.imshow("Rotated" , rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

