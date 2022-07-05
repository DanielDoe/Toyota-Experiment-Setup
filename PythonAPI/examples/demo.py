import os,sys
import cv2
import time




color = (36,255,12)
thickness = 1
map_image = cv2.imread('Town02.jpg')
(h, w, c) = map_image.shape[:3]
#cv2.imshow('HD Map',map_image)
#time.sleep(5000)

while True:
    ff1 = open('vehicle_output_1.txt','r')
    ff2 = open('vehicle_output_2.txt','r')
    location_vehicle_1 = ff1.readlines()[-1]
    x1,y1 = location_vehicle_1.strip().split(' ')
    x1,y1 = int((190-float(x1))/190*h),int((float(y1)-108)/190*h)
    location_vehicle_2 = ff2.readlines()[-1]
    x2,y2 = location_vehicle_2.strip().split(' ')
    x2,y2 = int((190-float(x2))/190*h),int((float(y2)-108)/190*h)

    start_point = (x1, y1)
    end_point = (x1+10, y1+10)
    print('vehicle1_start: ', start_point)
    print('vehicle1_start: ', end_point)
    map_image = cv2.imread('Town02.jpg')
    image = cv2.rectangle(map_image, start_point, end_point, color, thickness)
    cv2.putText(image, 'vehicle1', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    #cv2.imshow('HD Map',image)
    #time.sleep(5000)

    start_point = (x2, y2)
    end_point = (x2+10, y2+10)
    print('vehicle2_start: ', start_point)
    print('vehicle2_start: ', end_point)

    image = cv2.rectangle(image, start_point, end_point, color, thickness)
    cv2.putText(image, 'vehicle2', (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,0,12), 2)
	
    cv2.imshow('HD Map',image); 
    cv2.waitKey(50); 
    
cv2.destroyAllWindows()
    #time.sleep(5000)


    #https://carla.readthedocs.io/en/latest/core_map/