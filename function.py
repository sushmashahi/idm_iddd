import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt


def browse_images(digits):
    n = len(digits.images)
    def view_image(i):
        plt.imshow(digits.images[i], cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Training: %s' % digits.target[i])
        plt.show()
    interact(view_image, i=(0,n-1))
    
    

def imshow(X, resize=None):
    img=np.resize(X,(2,3)) #code to resize the image
    print(plt.imshow(img)) #code to print the image
    browse_images(img) #to diplay the image interact using matplotlib and ipywidgets
    pass