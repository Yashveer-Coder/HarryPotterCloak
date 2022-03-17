# Import Libraries
import numpy as np
import cv2
import time

#Calling Camera Function
cap = cv2.VideoCapture(0)
time.sleep(2)     
background = 0

for i in range(50):
    ret, background = cap.read()

while(cap.isOpened()): 
    ret, img = cap.read()
    if not ret:
        break
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

  #Defining which colour to detect
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255]) # values is for red colour Cloth
    mask1 = cv2.inRange(hsv, lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red =  np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
#Combining the masks so that It can be viewed as in one frame
    mask1 = mask1 +mask2
#After combining the mask we are storing the value in deafult mask.
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)
#Processing 
    mask2 =cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background,background,mask=mask1)
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Cloak',final_output)
#Lines to close the camera window    
    k = cv2.waitKey(10)
    if k==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
