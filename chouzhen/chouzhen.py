# coding=utf-8
'''
对1.视频 或是对 2.电脑摄像头 捕捉到的图像进行抽帧
'''
from os import path
import cv2
import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--video_path',help='the path which store your videos', default='C:/Users/asus/Desktop/chouzhen/video')
parser.add_argument('--save_path',help='the path which store your pictures', default='C:/Users/asus/Desktop/chouzhen/res/')
parser.add_argument('--capture',help='capture from computer camera or videos', default='True', type=bool)
parser.add_argument('--interval',help='Interval length', default='5', type=int)
args = parser.parse_args()

frame_count = 0
piece_num = 0

videos = os.listdir(args.video_path)
for each_video in videos:
    save_each_video_path = args.save_path + each_video.split('.')[0] + '/'
    Path(save_each_video_path).mkdir(exist_ok=True)
    if args.capture:
        cap = cv2.VideoCapture(0)
        save_each_video_path = args.save_path + 'capture/'
        Path(save_each_video_path).mkdir(exist_ok=True)
    else:
        cap = cv2.VideoCapture(args.video_path+'/'+each_video)

    if cap.isOpened():
        success = True
    else:
        success = False

    while(success):
        success, ret = cap.read()
        if frame_count % args.interval == 0 and success:
            cv2.imwrite(save_each_video_path + "%d.jpg" % piece_num, ret)
            piece_num += 1
        frame_count += 1
    
    cap.release()

