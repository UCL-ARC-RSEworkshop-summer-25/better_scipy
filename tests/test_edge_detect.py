import os
from better_scipy import edge_detect
import matplotlib.image as mpimg
import numpy as np

def test_edge_detect():
    cwd = os.getcwd()
    img_path = os.path.join(cwd, 'tests/edge_detect.jpg')
    exp_path = os.path.join(cwd, 'tests/edge_detect_expected.npy')

    exp_img = np.load(exp_path)
    assert np.sum(edge_detect(img_path) - exp_img) == 0
