import cv2
import os

def read_image(image_path):
    """
    Read the input image into a matrix of pixel values.

    Parameters
    ----------
    image_path : string
        File path to the image to read.

    Returns
    -------
    ndarray(dtype=float, ndim=3)
        Matrix of RGB values for each pixel.

    Examples
    --------
    >>> read_image('tests/images/test_image.jpg')
    """
    if not isinstance(image_path, str):
        raise ValueError("Image filepath is of incorrect type - it should be a string.")
    
    if not os.path.isfile(image_path):
        raise KeyError("Image filepath does not exist: ", os.path.join(os.getcwd(),image_path))

    image_matrix = cv2.imread(image_path)
    return image_matrix