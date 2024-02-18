import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os


def transform_image(image_path: str, method: str = 'rotate', direction: str = 'clockwise'):
    """
    Transform Image Function
    This function takes an image path and either rotates or flips the image in a 
    specified direction. 
    
    Parameters:
    -------
    - image_path (str): The path to the input image.
    - method (str, optional): The method to transform the image. ex: rotate, flip
      Options: 'rotate' (default) for rotating in the specified direction (clockwise or counterclockwise),
      'flip' for flipping over the specified axis (horizontal or vertical).
    - direction (str, optional): The direction to transform the image. ex: (clockwise, counterclockwise, 
        vertical, horizontal)
        Options: 'clockwise' and 'counterclockwise' for rotating an image,
        'vertical' or 'horizontal' for the axis to flip the image over.
    
    Returns:
    -------
    None
        The adjusted image is saved as a .png file at the same location as the input with "_trns_img" appended
        to the original filename.
        
    Raises
    ------
    FileNotFoundError
        If the image file cannot be opened or saved.
    
    ValueError
        If the method and direction are not compatible, ie method = 'flip', direction = 'clockwise',
        or the method or direction are not one of the options.
    
    Example:
    >>> input_path = 'path/to/input_image.jpg'
    >>> adjust_aspect_ratio(input_path, method = 'flip', direction = 'horizontal')
    """
    img = mpimg.imread(image_path)

    new_image = img.copy()

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file '{image_path}' does not exist.")
    
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
    
    plt.imshow(new_image)
    plt.show()

    output_path = image_path.rsplit('.', 1)[0] + "_trns_img.png"
    mpimg.imsave(output_path, new_image, format = "png")

    print(f"Transformed image saved as {output_path}")