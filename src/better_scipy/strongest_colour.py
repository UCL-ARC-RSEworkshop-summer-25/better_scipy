import imageio as iio
import matplotlib.pyplot as plt
import numpy as np


def compare_colours(main_colour, colour_1, colour_2, threshold=1.1):
    return np.logical_and(main_colour> threshold*colour_1,main_colour > threshold*colour_2)

def strongest_colour(image, colour, threshold = 1.1):
    """
    This function tells us which colour is strongest in our image, pixel by pixel.

    inputs:
    image = the image as a .png or .jpeg
    colour = either 'red', 'blue','green'
    threshold = it is default 1.1

    output:
    A numpy array with shape 300 by 451 of booleans
    Entries represent pixels.
    The entry will be True if the colour you inputted is the strongest colour in the corresponding pixel.

    Example:
    image = 'imageio:chelsea.png'
    print(type(strongest_colour(image, 'red'))) = <class 'numpy.ndarray'>
    print(strongest_colour(image, 'red')[0,0]) = True
    """
    im = iio.v3.imread(image)
    red = im[:, :, 0].astype(float)
    green = im[:,:, 1].astype(float)
    blue = im[:,:, 2].astype(float)
    if colour == 'red':
        value = compare_colours(red,blue,green,threshold)
    elif colour == 'green':
        value = compare_colours(green,blue,red,threshold)
    elif colour == 'blue':
        value = compare_colours(blue,green,red,threshold)
    else:
        raise ValueError('You need to choose from \'red\', \'green\', \'blue\' ' )
    return value

#uncomment to see a cute cat
#im = iio.v3.imread('imageio:chelsea.png')
# plt.imshow(im)
# plt.show()
