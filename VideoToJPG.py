# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:43:49 2019

@author: HariGopal V
"""
# importing necessary modules
#import numpy as np
import cv2
import os
#from sys import getsizeof
import sys
from imutils.video import count_frames
import argparse
import tqdm

# read them manually
#video_path = input("Enter Video path : ")
#output_path = 'C:/Users/ACER/Pictures/FreeVideoToJPGConverter/'

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to input video file")
ap.add_argument("-p", "--path", required=False, default = 'C:/Users/ACER/Pictures/FreeVideoToJPGConverter/', help="path to ioutput folder")

args = vars(ap.parse_args())
video_path = args["video"]
output_path = args["path"]


# checking the existancy of the input file
if(os.path.isfile(video_path)):
    file_name = video_path.split('/')[-1].split('.')[0]
else:
    print("File doesn't exists.")
    sys.exit(-1)

if(not os.path.isdir(output_path)):
    print("Output folder doesn't exist")
    sys.exit(-1)

if(os.path.isdir(output_path+file_name)):
    print("Folder "+output_path+file_name+" already exists.")
    sys.exit(-1)
#
total_frames = count_frames(video_path)

# read and the write the frames
try:
    os.mkdir(output_path+file_name)
    cap = cv2.VideoCapture(video_path)
    for i in tqdm.tqdm(range(total_frames), position=0, leave=True):

        ret, frame = cap.read()
        cv2.imwrite(output_path+file_name+'/'+file_name+'_'+str(i)+'.JPG', frame)

    cap.release()

except Exception as e:
    print(e)
