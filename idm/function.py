import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt


def imshow(X, resize=None):
    image=X
    res = cv2.resize(image, (54, 140), interpolation=cv2.INTER_CUBIC)
    plt.imshow(res) #code to print the image
    pass