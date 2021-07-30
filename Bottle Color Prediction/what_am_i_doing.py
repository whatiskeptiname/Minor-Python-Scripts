# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#for pixel processing
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
camera.hflip = True
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

    #converting frame(img i.e BGR) to HSV (hue-saturation-value)

	hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

	#definig the range of red color
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)

	#defining the Range of Blue color
	blue_lower=np.array([77,118,119],np.uint8)
	blue_upper=np.array([124,255,255],np.uint8)
	
	#defining the Range of yellow color
	yellow_lower=np.array([22,60,34],np.uint8)
	yellow_upper=np.array([32,255,255],np.uint8)
	
	#defining the Range of green color
	green_lower=np.array([36,70,102],np.uint8)
	green_upper=np.array([81,255,255],np.uint8)


	#finding the range of red,blue and yellow color in the image
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
	yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	green=cv2.inRange(hsv,green_lower,green_upper)

	kernal = np.ones((5,5),"uint8")
	red = cv2.dilate(red, kernal)
	res = cv2.bitwise_and(image, image, mask = red)

	blue = cv2.dilate(blue,kernal)
	res1 = cv2.bitwise_and(image, image, mask = blue)

	yellow = cv2.dilate(yellow,kernal)
	res2 = cv2.bitwise_and(image, image, mask = yellow)

	green = cv2.dilate(green,kernal)
	res3 = cv2.bitwise_and(image, image, mask = green)

	#Tracking the Red Color
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>500):
			x,y,w,h = cv2.boundingRect(contour)	
			image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(image,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
			
	#Tracking the Blue Color
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>500):
			x,y,w,h = cv2.boundingRect(contour)	
			image = cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(image,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

	#Tracking the yellow Color
	(_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>500):
			x,y,w,h = cv2.boundingRect(contour)	
			image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
			cv2.putText(image,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255))
                print(x.y)  
		

	#Tracking the green Color
	(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>500):
			x,y,w,h = cv2.boundingRect(contour)	
			image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(image,"green  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))  

	cv2.imshow("color Tracking", image)

    #cv2.imshow("Redcolour",red)
    #cv2.imshow("red",res) 	
    
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break