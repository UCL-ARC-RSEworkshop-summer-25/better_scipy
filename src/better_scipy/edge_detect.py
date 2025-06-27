import numpy as np
import matplotlib.image as mpimg

def sobel_kernel(axis):
    # Define Sobel kernel
    K = np.array([[1, 0, -1],
                  [2, 0, -2],
                  [1, 0, -1]])
    if axis == 'x': return K
    if axis == 'y': return K.T

def convert_to_BW(image_array):
    # Average across RGB channels
    return np.mean(image_array, axis=-1)

def get_image(img_path):
    img = mpimg.imread(img_path)
    return img

# Function to perform Sobel edge detection
def edge_detect(image):
    
    image_array = get_image(image)

    if len(image_array.shape) > 2:
        image_array = convert_to_BW(image_array)

    # Get image dimensions
    rows, cols = image_array.shape

    # Initialize gradient images
    Gx = np.zeros_like(image_array)
    Gy = np.zeros_like(image_array)

    # Make sobel kernels
    Kx = sobel_kernel('x')
    Ky = sobel_kernel('y')

    # Apply Sobel kernels to the image
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            patch = image_array[i-1:i+2, j-1:j+2]
            Gx[i, j] = np.sum(Kx * patch)
            Gy[i, j] = np.sum(Ky * patch)

    # Compute gradient magnitude
    G = np.sqrt(Gx**2 + Gy**2)
    G = (G / G.max()) * 255 # Normalize to 0-255

    # mpimg.imsave('tests/edge_detect_expected.jpg', G.astype(np.uint8), cmap='gray')
    return G.astype(np.uint8)