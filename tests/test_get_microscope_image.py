import numpy as np
from better_scipy.get_microscope_image import get_image
import pytest

@pytest.mark.online
def test_get_image_check_image_size():
    test = get_image()

    result = np.shape(test)
    expected = (480, 640, 3)

    assert result == expected