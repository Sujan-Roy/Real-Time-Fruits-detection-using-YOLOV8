# Import necessary libaraies 
import cv2
import argparse
import numpy as np

argparser = argparse.ArgumentParser(description='Simple implementation of Yolov3 algorithm in Python, using custom Dataset.')

argparser.add_argument('--img', type=str)
argparser.add_argument('--video', type=str)
argparser.add_argument('--out', type=str)

args = argparser.parse_args()
confidence, threshold = 0.5, 0.3 
labelPath = './obj.names'
labels = open(labelPath).read().strip().split('\n')


weightsPath = './yolov3-tiny.weights'
configPath = './yolov3-tiny.cfg'
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)


layer_names = net.getLayerNames()
yolo_layers = []
for i in net.getUnconnectedOutLayers():
    yolo_layers.append(layer_names[i[0] - 1])
def img_draw(img, boxes, confidences, classids, idxs, labels):
