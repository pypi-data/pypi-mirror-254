import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os


def transform_image(image, method: str = 'rotate', direction: str = 'clockwise', verbose: bool = False):
    """
    Transform Image Function
    This function takes a numpy image array and either rotates or flips the image in a 
    specified direction. 
    
    Parameters:
    -------
    - image (numpy.ndarray): The input image array.
    - method (str, optional): The method to transform the image. ex: rotate, flip
      Options: 'rotate' (default) for rotating in the specified direction (clockwise or counterclockwise),
      'flip' for flipping over the specified axis (horizontal or vertical).
    - direction (str, optional): The direction to transform the image. ex: (clockwise, counterclockwise, 
        vertical, horizontal)
        Options: 'clockwise' and 'counterclockwise' for rotating an image,
        'vertical' or 'horizontal' for the axis to flip the image over.
    - verbose (bool, optional): If True, print verbose information. False is the default.
    
    Returns:
    -------
    Image Numpy Array
        The adjusted image, returned as a NumPy array.
        
    Raises
    ------
    ValueError
        If the method and direction are not compatible, ie method = 'flip', direction = 'clockwise',
        or the method or direction are not one of the options.
    
    Example:
    >>> image = mpimg.imread('path/to/input_image.jpg')
    >>> transform_image(image, method = 'flip', direction = 'horizontal', transpose = False)
    """
    img = np.array(image)
    new_image = img.copy()
    
    if method.lower() == 'rotate':
        if direction == 'clockwise':
            new_image = np.rot90(img, -1)
            new_image = np.copy(new_image, order='C')
        elif direction.lower() == 'counterclockwise':
            new_image = np.rot90(img, 1)
            new_image = np.copy(new_image, order='C')
        else:
            raise ValueError("For rotation, the direction should be either 'clockwise' or 'counterclockwise'")
    
    elif method.lower() == 'flip':
        if direction.lower() == 'horizontal':
            new_image = np.flipud(img)
        elif direction.lower() == 'vertical':
            new_image = np.fliplr(img)
        else:
            raise ValueError("For flipping, the direction should be either 'horizontal' or 'vertical'")
    else:
        raise ValueError("Method should be either 'rotate' or 'flip'")
    
    if verbose:
        plt.imshow(new_image)
        plt.show()
    
    return new_image