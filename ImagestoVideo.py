# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:18:53 2019

@author: HariGopal V
"""

# importing necessary modules
import numpy as np
import cv2
import os
import sys
import argparse
import tqdm


# construct the argument parse and parse the arguments
input_path = input("Enter the path of folder : ")
output_path = input("Enter the output folder : ")
fps = int(input("Enter the FPS : "))
codec = input("Enter the video codec : ")

'''
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="path to folfer of images")
ap.add_argument("-o", "--output", required=False, help="path to output folder")
ap.add_argument("-f", "--fps", required=False, default = 30, help="fps of the output video")
ap.add_argument("-c", "--codec", required=False, default="MJPG", help="Codec of the video file")


args = vars(ap.parse_args())
input_path = args["path"]
output_path = args["output"]
fps = int(args["fps"])
codec = args["codec"]
'''

# checking the existancy of the paths
if(os.path.isdir(input_path)):
    listOfFiles = os.listdir(input_path)
    print(len(listOfFiles))
else:
    print("Input Folder doesn't exists.")


if(os.path.isfile(output_path)):
    print("File "+output_path.split('/')[-1]+" already exists.")
    if(input("Do you want to override it (Y/N) : ") != 'Y'):
        sys.exit(-1)

# initialize the FourCC, video writer, dimensions of the frame, and
# zeros array
fourcc = cv2.VideoWriter_fourcc(*codec)
writer = None
(h, w) = (None, None)
zeros = None

# read and the write the frames
try:
    # loop over frames from the video stream
    for i in tqdm.tqdm(listOfFiles, position=0, leave=True):
        im = cv2.imread(input_path+'/'+i)
    	# check if the writer is None
        if writer is None:
    		# store the image dimensions, initialize the video writer,
    		# and construct the zeros array
            (h, w) = im.shape[:2]
            writer = cv2.VideoWriter(output_path, fourcc, fps, (w, h), True)
            zeros = np.zeros((h, w), dtype="uint8")
        writer.write(im)
    writer.release()
except Exception as e:
    print(e)

