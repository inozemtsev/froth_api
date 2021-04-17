from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt
import numpy as np
import cv2
from collections import Counter
# from skimage.color import rgb2lab, deltaE_cie76
import os


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))
  
def get_image(image):
    #image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image
  
  
def get_colors(image, number_of_colors=3, show_chart=False):
    
    modified_image = image

    modified_image = modified_image[modified_image.shape[0]//4:modified_image.shape[0]//2,modified_image.shape[1]//4:3*modified_image.shape[1]//4]
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)

    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)

    # Sorting
    D = {}
    sum_v = 0

    for (k, v) in counts.most_common():
      sum_v += v 
      D[k] = v
    
    center_colors = clf.cluster_centers_
    
    # Ordering through the keys
    ordered_colors = [center_colors[i] for i in D.keys()]

    if (show_chart):
        plt.figure(figsize = (8, 6))
        plt.pie(D.values(), labels = hex_colors, colors = hex_colors)

    colors = []

    for i in D.keys():
      colors.append((RGB2HEX(ordered_colors[i]), round(D[i]/sum_v*100, 2)))

    
    return colors
