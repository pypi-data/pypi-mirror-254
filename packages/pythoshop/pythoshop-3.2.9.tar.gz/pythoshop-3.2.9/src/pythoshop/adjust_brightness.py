import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

def adjust_brightness(img, brightness_factor, verbose=False):
    """
    Adjust the brightness of an image and save the result.

    This function changes the brightness of an input image by a specified factor. The factor can be 
    positive to increase brightness or negative to decrease it. The brightness change is applied 
    uniformly to all pixels of the image.

    Parameters
    ----------
    image_path : str
        The file path to the image that needs brightness adjustment. The image can be in .jpg or .png format.
    brightness_factor : int or float
        A value that determines the amount by which to adjust the brightness. Positive values increase 
        brightness, while negative values decrease it.

    Returns
    -------
    None
        The adjusted image is saved as a .png file at the same location as the input with "_brightened" appended
        to the original filename.

    Raises
    ------
    IOError
        If the image file cannot be opened or saved.
    
    Example:
    >>> img = mpimg.imread("tests/test_img_1.png")
    >>> img_adjusted = adjust_brightness(img, -0.3)

    """
    if not isinstance(brightness_factor, (int, float)):
        raise ValueError("Brightness factor must be an integer or float")

    try:
        # Check if brightness_factor is integer or float and adjust brightness accordingly
        if isinstance(brightness_factor, int):
            # Adjust brightness for integer factor
            adjusted_img = np.clip(img.astype(np.int16) + brightness_factor, 0, 255).astype(np.uint8)

        elif isinstance(brightness_factor, float):
            # Adjust brightness for float factor
            adjusted_img = np.clip(img.astype(np.float32) * (1 + brightness_factor), 0, 1)

        return adjusted_img

    except Exception as e:
        raise IOError(f"Error processing the image: {e}")

