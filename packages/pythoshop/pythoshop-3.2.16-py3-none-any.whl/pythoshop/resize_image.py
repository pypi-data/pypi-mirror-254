import matplotlib.pyplot as plt
import numpy as np

def resize_image(image, height, width, method='crop', verbose=False):
    """
    Image Resizing Function

    This function takes an image and adjusts it to have the inputted dimensions using the selected method.

    Parameters:
    - image (numpy.ndarray): The input image array.
    - height (int): The desired height for the image.
    - width (int): The desired width for the image.
    - method (str, optional): The method to obtain the desired image dimensions.
      Options: 'maintain_aspect_ratio' (default) for maintaining the aspect ratio,
               'crop' for cropping to the specified dimensions,
               'add_borders' for adding borders to maintain the aspect ratio.
    - verbose (bool, optional): If True, print verbose information. False is the default.

    Returns:
    - Image Numpy Array
    The resized image is returned as a numpy array.

    Raises:
    - ValueError: If an invalid resize method is provided.
    """

    img = np.array(image)  # Ensure input is a numpy array

    if verbose:
        print(f"Initial image dimensions: {img.shape}")

    if method == 'maintain_aspect_ratio':
        aspect_ratio = img.shape[1] / img.shape[0]
        new_width = int(height * aspect_ratio)
        img = np.resize(img, (height, new_width, img.shape[2]))
    elif method == 'crop':
        img = img[:height, :width, :]
    elif method == 'add_borders':
        aspect_ratio = img.shape[1] / img.shape[0]
        new_width = int(height * aspect_ratio)
        img = np.resize(img, (height, new_width, img.shape[2]))

        # Initialize image with white background
        new_img = np.ones((height, width, img.shape[2])) * 255
        x_offset = (width - img.shape[1]) // 2
        y_offset = (height - img.shape[0]) // 2
        new_img[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1], :] = img
        # Normalize the image values to the range [0, 1]
        new_img = new_img / 255.0
        img = new_img
    else:
        raise ValueError("Invalid resize method. Supported methods: 'maintain_aspect_ratio', 'crop', 'add_borders'.")

    if verbose:
        print("Resized Image Dimensions: ", img.shape)
        plt.imshow(img)  # Display the resized image
        plt.show()

    return img
