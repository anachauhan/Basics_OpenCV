import cv2

#to load an image
image = cv2.imread("PythonLogo.png")

if image is None:
    print("Error! :Image not found")
else:
    print("Image loaded successfully!")


#display----
#imshow()
#waitkey()        0= as soon as any key is clicked , the image goes off
#destroy()
