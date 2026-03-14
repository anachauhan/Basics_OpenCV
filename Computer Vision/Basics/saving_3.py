import cv2 

image = cv2.imread("PythonLogo.png")

if image is not None:
    success = cv2.imwrite("output_python.png" , image)
    if success:
        print("Image saved successfully as 'output_python.png")
    else:
        print("Failed to save the image!")
else:
    print("Error! could no load the image")



#image dimensions ---
#.shape --- (height , width , channel)
# for red color = (480 , 640 , 3)         here 3 = BGR , if channel is missing = greyscale