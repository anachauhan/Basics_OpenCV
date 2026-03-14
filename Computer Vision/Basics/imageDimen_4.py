import cv2 

image = cv2.imread("E:\DeepDive\Computer Vision\PythonLogo.png")

if image is not None:
    h , w, c = image.shape
    print(f"Image loaded: \nHeight: {h} \nWidth: {w} \nChannels: {c}")
else:
    print("Could not load image")

#convert to grayscale 
#cvtColor(img , cv2.COLOR_BGR2GRAY)
