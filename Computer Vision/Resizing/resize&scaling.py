#cv2.resize(src , dsize , fx , fy , interpolation)
#src = original image
#dsize = (width , height)     @not(height , width)

#smaller image --- faster detection

import cv2

image = cv2.imread("E:\DeepDive\Computer Vision\PythonLogo.png")

if image is None:
    print("Image not found")
else:
    print("Image loaded")
    resized = cv2.resize(image , (300 , 300))

    #cv2.imshow("Original Image" , image)
    cv2.imshow("Resized image" , resized)

    cv2.imwrite("resized_output.png" , resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
