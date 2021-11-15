import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt


def imshow(X, resize=None):
    img = np.resize(X) #code to resize the image
    print(plt.imshow(img)) #code to print the image
    #browse_images(img) #to diplay the image interact using matplotlib and ipywidgets
    pass