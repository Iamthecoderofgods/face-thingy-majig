import cv2,numpy,sys,os

haarfile = r"C:/Users/hjbeb/OneDrive/Desktop/python/Open_Cv/haarcascade_frontalface_default.xml"

Cascade = cv2.CascadeClassifier(haarfile)

if Cascade.empty():
    print("Cscade Classifier could not be loaded")
    exit()

datasets = "datasets"
subdata = "Max Flynn James"

path = os.path.join(datasets,subdata)

os.makedirs(path,exist_ok=True)

Width = 500
Height = 500

Webcam = cv2.VideoCapture(0)

count = 1

grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)