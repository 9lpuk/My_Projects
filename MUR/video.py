import pymurapi as mur
import cv2 as cv
import time
auv = mur.mur_init()

while True:
    depth = auv.get_depth()
    print(depth)
    time.sleep(0.5)
       
    yaw = auv.get_yaw()
    print(yaw)
   
    image = auv.get_image_front()
    
    cv.imshow("",image)
    cv.waitKey(10)
    
    auv.set_motor_power(0, 50)
    auv.set_motor_power(1, 50)
    
    
