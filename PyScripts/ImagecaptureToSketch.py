#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:18:09 2020

@author: nancyscarlet
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Real time image capture from camera 
# 0 uses the default camera in laptop. To use webcam specify 1 here
cam = cv2.VideoCapture(0)
cv2.namedWindow('Camera for testing')

def dodge(img,mask):
    return cv2.divide(img,255-mask,scale=256)

while True:
    ret,frame = cam.read()
    if not ret:
        print('Failed to capture frame')
        break
    #Showing captured image in a frame named 'testframe'
    cv2.imshow('testframe',frame)
    
    #Waiting on key press 
    k = cv2.waitKey(1)
    itr=0
    if(k%256==27):
        #If esc is pressed then close camera
        print("Closing camera....")
        break
    elif k%256 == 32:
        #Capturing image
        img_name = "opencv"+str(itr)+".png"
        #Reading the captured image
        capturedImg = cv2.imread(img_name)
        #Running Canny edge detection algo
        #Params- imgread,minfthreshold,maxthreshold
        #In canny we hv min threshold and max threoshold for variation 
        #in pixels . if the intensity gradient of pixel lies below min threshold then it is ignore
        #This is done to see if the edge is actually a continum of another edge but is thinner in texture
        #If the pixel lies below threshold it means it is not an actual edge so itll be discarded
        
        edges = cv2.canny(capturedImg,100,200)
        
        #This canny wont be enough for us to get desired effect
        
        #Invert the image
        inv_img = 255-capturedImg
        
        #apply Gaussian blur to inv img
        img_blur = cv2.GaussianBlur(inv_img,ksize=(10,10),sigmaX=0,sigmaY=0)
        img_blend = dodgeV2(capturedImg,img_blur)
        plt.imshow(img_blend,cmap='gray')
        plt.show()
        
        #Saving the image to separate file
        cv2.imwrite(img_name,img_blend)
        
cam.release()
cv2.destroyAllWindows()
        
        
        
        
        
        
        
        
        
        
        
        
    