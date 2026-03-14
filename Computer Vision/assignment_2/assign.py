import cv2

img = input("Enter the file/image location: ")

image = cv2.imread(img)

if image is None:
    print("Error occurred during loading")
else:
    print("Image loaded successfully")
    print("\n")
    print("\tMenu to draw: \n")
    print("\t1.Line \t 2 . Circle  \t 3.Rectangle  \t 4. Text \n")
    ch = int(input("Enter your choice: "))

    def showImg(img):
        cv2.imshow("Required image :" , img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("Enter the co-ordinates :")
    if(ch== 1):
        x1 = int(input("Enter X1: "))
        y1 = int(input("Enter Y1: "))
        x2 = int(input("Enter X2: "))
        y2 = int(input("Enter Y2: "))
        color = tuple(map(int, input("Enter B G R values (e.g. 255 0 0): ").split()))
        thickness = int(input("Enter the thickness : "))
        line = cv2.line(image , (x1,y1) , (x2,y2) , color , thickness)
        showImg(line)
    
    elif(ch==2):
        x1 = int(input("Enter x co-ordinate of center: "))
        y1 = int(input("Enter y co-ordinate of center: "))
        r = int(input("Enter the radius of the circle: "))
        color = tuple(map(int, input("Enter B G R values (e.g. 255 0 0): ").split()))
        thickness = int(input("Enter the thickness : "))
        circle = cv2.circle(image , (x1,y1) , r , color, thickness)
        showImg(circle)

    elif(ch==3):
        x1 = int(input("Enter X1: "))
        y1 = int(input("Enter Y1: "))
        x2 = int(input("Enter X2: "))
        y2 = int(input("Enter Y2: "))
        color = tuple(map(int, input("Enter B G R values (e.g. 255 0 0): ").split()))
        thickness = int(input("Enter the thickness : "))
        rect = cv2.rectangle(image , (x1,y1) , (x2,y2) , color , thickness)
        showImg(rect)

    elif(ch==4):
        text = input("Enter the text: ")
        x1 = int(input("Enter X1: "))
        y1 = int(input("Enter Y1: "))
        
        print("Choose font:")
        print("1 - SIMPLEX")
        print("2 - COMPLEX")
        print("3 - SCRIPT")

        choice = int(input("Enter choice: "))

        if choice == 1:
            fDesign = cv2.FONT_HERSHEY_SIMPLEX
        elif choice == 2:
            fDesign = cv2.FONT_HERSHEY_COMPLEX
        elif choice == 3:
            fDesign = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        else:
            fDesign = cv2.FONT_HERSHEY_SIMPLEX 

        fScale = int(input("Enter the font scale: "))
        color = tuple(map(int, input("Enter B G R values (e.g. 255 0 0): ").split()))
        thickness = int(input("Enter the thickness : "))
        addtext = cv2.putText(image ,text , (x1,y1) , fDesign , fScale , color , thickness)
        showImg(addtext)

    else:
        print("Invalid choice")



