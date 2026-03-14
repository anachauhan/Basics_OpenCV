import cv2

image = cv2.imread("PythonLogo.png")

if image is not None:
    gray = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale Image" , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    success = cv2.imwrite("output_gray.png" , gray)
    if success:
        print("Image saved successfully")
    else:
        print("Not saved")

else:
    print("Could not load the image")



