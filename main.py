# Import necessary libaraies 
import cv2
import argparse
import numpy as np

argparser = argparse.ArgumentParser(description='Simple implementation of Yolov3 algorithm in Python, using custom Dataset.')

argparser.add_argument('--img', type=str)
argparser.add_argument('--video', type=str)
argparser.add_argument('--out', type=str)
