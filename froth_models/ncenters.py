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
    return sorted(centers)

 def find_directions(img1, img2, threshold=30): # [[3333],[44444],[],[]]
    
    img1 = image_preproc(img1)
    img2 = image_preproc(img2)
    
    prev = find_centers(img1)
    now = find_centers(img2)
    
    d = []
    
    for x in now:
        for y in prev:
            if y[0]-threshold<x[0]<y[0]+threshold and y[1]-threshold<x[1]<y[1]+threshold:
                d.append([x[0]-y[0],x[1]-y[1]])         
    d = np.array(d) 
    if len(d)==0: #если не нашел объектов, которые сдвинулись на нужную величину пикселей (15)
        dx = 0
        dy = 0
    else:
        d = np.median(d, axis=0).astype(np.int) # берем медиану всех смещений, чтобы уменьшить вероятность ошибки
        # далее выкидываем

        dx = d[0]
        dy = d[1]
    v = round(np.sqrt(dx*dx+dy*dy),1)
    return v, (dx, dy)
