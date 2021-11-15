import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt


def imshow(X, resize=None):
    res = cv2.resize(X, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)
    print(plt.imshow(img)) #code to print the image
  
    pass