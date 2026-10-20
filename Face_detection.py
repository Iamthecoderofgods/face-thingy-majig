import cv2,numpy,sys,os

#prebuilt face detection
haarfile = r"C:/Users/hjbeb/OneDrive/Desktop/python/Open_Cv/haarcascade_frontalface_default.xml"

Cascade = cv2.CascadeClassifier(haarfile)

if Cascade.empty():
    print("Cscade Classifier could not be loaded")
    exit()

#where all datasets will be stored
datasets = "datasets"
subdata = "Max Flynn James"


path = os.path.join(datasets,subdata)

#creating folder if not existing
os.makedirs(path,exist_ok=True)

Width = 500
Height = 500

Webcam = cv2.VideoCapture(0)

count = 1

while count<30:
    #Ret indicates if the frames was captured corrctly. im is the image that the webcam returns to us
    Ret,im = Webcam.read()
    if not Ret:
        print("Frames where not captured/webcam was not working")
        break
    
    grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    face_detected  = Cascade.detectMultiScale(grey,1.3,4)

    #draw rectangle
    for (x,y,w,h) in face_detected:
        cv2.rectangle(im,(x,y),(x+w,y+h),(0, 128, 0),5)
        
    cv2.imshow("Face Detection",im)
    count +=1
    key = cv2.waitKey(10)
    if key == 27:
        break

Webcam.release()
cv2.destroyAllWindows()