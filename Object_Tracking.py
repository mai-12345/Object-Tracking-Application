
import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import tempfile 

st.title("Object Tracking Application ")

upload = st.file_uploader('Please, Upload a Video...', type = ['mp4', 'mov', 'avi'])

def ConvertColor(image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return image

if upload is not None:
        with tempfile.NamedTemporaryFile(delete = False) as temp_video:
            temp_video.write(upload.read())
            video_path = temp_video.name
        captures = cv2.VideoCapture(video_path)
    
        frame_rate = 40 #control how many frames
        frame_count = 0

        frame_get=captures.get(cv2.CAP_PROP_FRAME_COUNT)*np.random.uniform(size=30)
        frames=[]
        for i in frame_get:
            captures.set(cv2.CAP_PROP_POS_FRAMES,i)
            ret,frame=captures.read()
            frames.append(frame)
       

        while captures.isOpened():    
            ret, frame = captures.read()
            if not ret:
                 break
            frame_count += 1

            if frame_count % frame_rate == 0:
                 
                 frame_median=np.median(frames,axis=0).astype(dtype=np.uint8)
                 frame=frames[0]
                 gray_frame_median=cv2.cvtColor(frame_median,cv2.COLOR_BGR2GRAY)
                 gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                 background_remove_frame=cv2.absdiff(gray_frame,gray_frame_median)
                 frame_blur=cv2.GaussianBlur(background_remove_frame,(11,11),0)
                 ret,frame_threshold=cv2.threshold(frame_blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
                 (contours, _) = cv2.findContours(frame_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                 for i in contours:
                     x,y,width,height=cv2.boundingRect(i)
                     cv2.rectangle(frame,(x,y),(x+width,y+height),(25,0,255),2)
             
                     st.image(ConvertColor(frame), channels = 'RGB')


        captures.release()
