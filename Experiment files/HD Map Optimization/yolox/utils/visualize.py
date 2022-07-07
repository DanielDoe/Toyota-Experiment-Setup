#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) 2014-2021 Megvii Inc. All rights reserved.

import cv2
import numpy as np
import math
import torch
import time
from loguru import logger
import csv



def compress_image(img, ref_boxes_with_qualities):
    #with torch.no_grad():
    #    t0 = time.time()
    for box in ref_boxes_with_qualities:
        enc = cv2.imencode('.jpg', img[int(box.y0):int(box.y1), int(box.x0):int(box.x1)], [
                        cv2.IMWRITE_JPEG_QUALITY, box.quality, cv2.IMWRITE_JPEG_OPTIMIZE])[1]
        img[int(box.y0):int(box.y1), int(box.x0):int(box.x1)
        ] = cv2.imdecode(enc, 1).astype(img.dtype) 
    #    logger.info("Compression time: {:.4f}s".format(time.time() - t0))     
    return img


def get_ref_boxes(height, width, grid_shape):
    rows, cols = grid_shape
    dy, dx = round(height / rows), round(width / cols)
    grid = []
    for i in range(int(height/dy)):
        for j in range(int(width/dx)):
            grid.append((j*dx, i*dy, (j+1)*dx, (i+1)*dy))# returns x0 y0 x1 y1
    return grid


def draw_ref_boxes(img, height, width, grid_shape):
    rows, cols = grid_shape
    dy, dx = height / rows, width / cols
    color = (0, 255, 0)
    thickness = 1

    for x in np.linspace(start=dx, stop=width-dx, num=cols-1):
        x = int(round(x))
        cv2.line(img, (x, 0), (x, height), color=color, thickness=thickness)

    # draw horizontal lines
    for y in np.linspace(start=dy, stop=height-dy, num=rows-1):
        y = int(round(y))
        cv2.line(img, (0, y), (width, y), color=color, thickness=thickness)

    return img

def draw_bounding_boxes(img, x0, y0, x1, y1, cls_id, class_names, score):
    color = (_COLORS[cls_id] * 255).astype(np.uint8).tolist()
    text = '{}:{:.1f}%: {x0}, {x1}, {y0}, {y1}'.format(class_names[cls_id], score * 100,x0=x0, x1=x1, y0=y0, y1=y1)

    txt_color = (0, 0, 0) if np.mean(_COLORS[cls_id]) > 0.5 else (255, 255, 255)

    font = cv2.FONT_HERSHEY_SIMPLEX

    txt_size = cv2.getTextSize(text, font, 0.4, 1)[0]
    cv2.rectangle(img, (x0, y0), (x1, y1), color, 2)

    txt_bk_color = (_COLORS[cls_id] * 255 * 0.7).astype(np.uint8).tolist()
    cv2.rectangle(
        img,
        (x0, y0 + 1),
        (x0 + txt_size[0] + 1, y0 + int(1.5*txt_size[1])),
        txt_bk_color,
        -1
    )
    cv2.putText(img, text, (x0, y0 + txt_size[1]), font, 0.4, txt_color, thickness=1)

# Takes the coordinates of a grid and the coordinates of a bounding box and returns the area of the of the bounding box contained in the grid
def bounding_box_area_within_ref_box(ref_box, bounding_box):
    # print("ref box", ref_box.x0, " ", ref_box.y0, " ", ref_box.x1, " ", ref_box.y1) 
    # print("bounding box", bounding_box.x0, " ", bounding_box.y0, " ", bounding_box.x1, " ", bounding_box.y1)
    dx, dy = 0, 0
    if bounding_box.x1 >= ref_box.x0 and bounding_box.x0 <= ref_box.x1:
        #print("Hello from the first if")
        if bounding_box.x0 <= ref_box.x0:
            dy = bounding_box.x1 - ref_box.x0
        elif bounding_box.x1 >= ref_box.x1:
            dy = ref_box.x1 - bounding_box.x0
        elif bounding_box.x0 >= ref_box.x0 and bounding_box.x1 <= ref_box.x1:
            dy = bounding_box.x1 - bounding_box.x0
        elif bounding_box.x0 < ref_box.x0 and bounding_box.x1 > ref_box.x1:
            dy = ref_box.x1 - ref_box.x0
    if bounding_box.y1 >= ref_box.y0 and bounding_box.y0 <= ref_box.y1:
        #print("Hello from the second if")
        if bounding_box.y0 <= ref_box.y0:
            dx = bounding_box.y1 - ref_box.y0
        elif bounding_box.y1 >= ref_box.y1:
            dx = ref_box.y1 - bounding_box.y0
        elif bounding_box.y0 >= ref_box.y0 and bounding_box.y1 <= ref_box.y1:
            dx = bounding_box.y1 - bounding_box.y0
        elif bounding_box.y0 < ref_box.y0 and bounding_box.y1 > ref_box.y1:
            dx = ref_box.y1 - ref_box.y0
    #print("size: ", dx, "x", dy)        
    return dx*dy


def percentage_area_of_ref_box(ref_box, bounding_boxes):
    ref_box_area = (ref_box.x1 - ref_box.x0) * (ref_box.y1 - ref_box.y0)
    box_areas = 0
    for box in bounding_boxes:
        box_areas += bounding_box_area_within_ref_box(ref_box, box)
    return (box_areas/ref_box_area)*100


def get_quality(percentage_area):
    if percentage_area >= 1:
        return 80
    elif percentage_area >= 0.5 and percentage_area < 1:
        return 60
    elif percentage_area >= 0.25 and percentage_area < 0.5:
        return 40
    else:
        return 0


def get_qualities(ref_boxes, bounding_boxes):
    for box in ref_boxes:
        box.quality = get_quality(percentage_area_of_ref_box(box, bounding_boxes))


def get_center_values(x_cor, y_cor, destination):
    destination.append(x_cor, y_cor)


def vis(img, bounding_boxes, scores, cls_ids, conf=0.5, class_names=None):
    x_min, x_max, y_min, y_max = math.inf, 0, math.inf, 0
    #bounding_boxes.numpy())
    for i in range(len(bounding_boxes)):
        box = bounding_boxes[i]
        cls_id = int(cls_ids[i])
        score = scores[i]
        if score < conf:
            continue
        x0, y0, x1, y1 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        print(x0, x1, y0, y1)
        print("*****************************")

        # Get all bounding box coords
        x_min, x_max, y_min, y_max = min(x0, x_min), max(x1, x_max), min(y0, y_min), max(y1, y_max)

        draw_bounding_boxes(img, x0, y0, x1, y1, cls_id, class_names, score)
    
    with torch.no_grad():
       # write_inference_time(str(time.time() - t0))   
        grid_shape = (100, 100)
        ref_boxes = [RefBox(box[0],box[1],box[2],box[3]) for box in get_ref_boxes(y_max, x_max, grid_shape)]
        bounding_boxes = [Box(box[0],box[1],box[2],box[3]) for box in bounding_boxes.numpy()]
        
        get_qualities(ref_boxes,bounding_boxes)
        
        t0 = time.time()
        img = compress_image(img,ref_boxes)
        #img = draw_ref_boxes(img, y_max, x_max, grid_shape)
        #write_compression_time(str(time.time() - t0))
        
        img = img[y_min:y_max, x_min:x_max]
        logger.info("Total compression time: {:.4f}s".format(time.time() - t0))
        
    return img

def write_compression_time(data):
    with open('compression_time.csv', 'a', encoding='UTF8') as f:
        f.write(data+",")
class Box:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1 
        self.y1 = y1 
class RefBox(Box):
    def __init__(self, x0, y0, x1, y1):
        super().__init__(x0, y0, x1, y1) 
        
_COLORS = np.array(
    [
        0.000, 0.447, 0.741,
        0.850, 0.325, 0.098,
        0.929, 0.694, 0.125,
        0.494, 0.184, 0.556,
        0.466, 0.674, 0.188,
        0.301, 0.745, 0.933,
        0.635, 0.078, 0.184,
        0.300, 0.300, 0.300,
        0.600, 0.600, 0.600,
        1.000, 0.000, 0.000,
        1.000, 0.500, 0.000,
        0.749, 0.749, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 1.000,
        0.667, 0.000, 1.000,
        0.333, 0.333, 0.000,
        0.333, 0.667, 0.000,
        0.333, 1.000, 0.000,
        0.667, 0.333, 0.000,
        0.667, 0.667, 0.000,
        0.667, 1.000, 0.000,
        1.000, 0.333, 0.000,
        1.000, 0.667, 0.000,
        1.000, 1.000, 0.000,
        0.000, 0.333, 0.500,
        0.000, 0.667, 0.500,
        0.000, 1.000, 0.500,
        0.333, 0.000, 0.500,
        0.333, 0.333, 0.500,
        0.333, 0.667, 0.500,
        0.333, 1.000, 0.500,
        0.667, 0.000, 0.500,
        0.667, 0.333, 0.500,
        0.667, 0.667, 0.500,
        0.667, 1.000, 0.500,
        1.000, 0.000, 0.500,
        1.000, 0.333, 0.500,
        1.000, 0.667, 0.500,
        1.000, 1.000, 0.500,
        0.000, 0.333, 1.000,
        0.000, 0.667, 1.000,
        0.000, 1.000, 1.000,
        0.333, 0.000, 1.000,
        0.333, 0.333, 1.000,
        0.333, 0.667, 1.000,
        0.333, 1.000, 1.000,
        0.667, 0.000, 1.000,
        0.667, 0.333, 1.000,
        0.667, 0.667, 1.000,
        0.667, 1.000, 1.000,
        1.000, 0.000, 1.000,
        1.000, 0.333, 1.000,
        1.000, 0.667, 1.000,
        0.333, 0.000, 0.000,
        0.500, 0.000, 0.000,
        0.667, 0.000, 0.000,
        0.833, 0.000, 0.000,
        1.000, 0.000, 0.000,
        0.000, 0.167, 0.000,
        0.000, 0.333, 0.000,
        0.000, 0.500, 0.000,
        0.000, 0.667, 0.000,
        0.000, 0.833, 0.000,
        0.000, 1.000, 0.000,
        0.000, 0.000, 0.167,
        0.000, 0.000, 0.333,
        0.000, 0.000, 0.500,
        0.000, 0.000, 0.667,
        0.000, 0.000, 0.833,
        0.000, 0.000, 1.000,
        0.000, 0.000, 0.000,
        0.143, 0.143, 0.143,
        0.286, 0.286, 0.286,
        0.429, 0.429, 0.429,
        0.571, 0.571, 0.571,
        0.714, 0.714, 0.714,
        0.857, 0.857, 0.857,
        0.000, 0.447, 0.741,
        0.314, 0.717, 0.741,
        0.50, 0.5, 0
    ]
).astype(np.float32).reshape(-1, 3)