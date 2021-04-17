import cv2
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

def image_preproc(image):
  return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

def find_centers(p, threshold=0.9):
    '''
    Функция: нахождение центров бликов
    Входные параметры:
        • p - картинка в пространстве цветов GRAY, массив пикселей, np.float32 [0.0,..,1.0]
    Выходные параметры:
        • centers - sorted list of tuples [(x1,y1),(x2,y2),...,(xn,yn)] and x1<=x2<=...<=xn
    '''
    img_erode = (p>threshold).astype(np.uint8)
    contours,_ = cv2.findContours(img_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    centers =  []
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if w>=3 and h>=3:
            centers.append((x+w//2, y+h//2))    
    #return sorted(centers)
    return len(centers)
