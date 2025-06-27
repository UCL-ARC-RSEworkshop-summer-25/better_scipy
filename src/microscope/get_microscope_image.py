"""Retrieving microscope image from website."""

import requests 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def get_image(image_url = 'http://10.97.23.240/image', display_image=False):
    """Get image from microscope. By default, it retrieves the image from the address.
    Example:
    >>> image = get_image()"""
    #image_url = 'http://10.97.23.240/image'
    response = requests.get(image_url).content
    with open('microscope_image.png', 'wb') as handler:
        handler.write(response)

    im = Image.open('microscope_image.png' , 'r')

    pix_val = list(im.getdata())

    pix_val_array = np.array(pix_val)
    #print(pix_val_array.shape)  

    image = pix_val_array.reshape(480, 640, 3)
    #print(image.shape)  

    if display_image:
        plt.imshow(image)
        plt.show()

    return image













