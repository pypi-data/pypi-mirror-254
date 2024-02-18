import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

def apply_filter(image, method, degree=0.7, verbose=False):
      """
      Apply filter from a chosen range of colours. 

      This function allows a filter to be applied on the image which can be retrieved 
      from ['red', 'blue', 'green', 'gray', 'sepia'].

      Parameters
      ----------
      image_path : image
            Image object to be worked on. 
      method : str
            Choose from a list of available filters to be applied onto the image. 
      degree : int or float
            Degree to apply the filter on the image. Minimum value is 0 and maximum value is 1.
            Default is set as 0.7. 

      Returns
      -------
      None
            The filtered image is saved as a .png file at the same location as the input with "_filter_img" appended
            to the original filename.  

      Raises
      ------
      FileNotFoundError
            If the image file cannot be opened or saved.

      ValueError
            If incorrect type of variables are used in parameters. 

      Examples
      --------
      To apply 'sephia' filter on 'photo.jpg' by 30%:
      >>> apply_filter('photo.jpg', 'sephia', 0.3)

      To apply 'aquamarine' filter on 'photo.jpg' by 70%:
      >>> apply_filter('photo.jpg', 'aquamarine', 0.7)
      """
      new_image = image.copy()

      if degree < 0.5:
            raise Exception("Degree of filter shouldn't be smaller than 0.5.")

      if method == "sepia":
            new_image[::, ::, 0] = (image[::, ::, 0] * 0.786 * degree) + (image[::, ::, 1] * 0.769) + (image[::, ::, 2] * 0.189)
            new_image[::, ::, 1] = (image[::, ::, 0] * 0.349 * degree) + (image[::, ::, 1] * 0.686) + (image[::, ::, 2] * 0.168)
            new_image[::, ::, 2] = (image[::, ::, 0] * 0.272 * degree) + (image[::, ::, 1] * 0.534) + (image[::, ::, 2] * 0.131)
      elif method == "blue":
            new_image[:, :, 0] = image[:, :, 0] * (1-degree)
            new_image[:, :, 1] = image[:, :, 1] * (1-degree)
            new_image[:, :, 2] = (image[:, :, 2] * (1 * degree if degree is not None else 0))
      elif method == "gray":
            new_image[:, :, 0] = (image[::, ::, 0] * (1-degree)) 
            new_image[:, :, 1] = (image[::, ::, 1] * (1-degree))
            new_image[:, :, 2] = (image[::, ::, 2] * (1-degree))
      elif method == "red":
            new_image[:, :, 0] = (image[:, :, 0] * (1 * degree if degree is not None else 0))
            new_image[:, :, 1] = image[:, :, 1] * (1-degree)
            new_image[:, :, 2] = image[:, :, 2] * (1-degree)
      elif method == "green":
            new_image[:, :, 0] = image[:, :, 0] * (1-degree)
            new_image[:, :, 1] = (image[:, :, 1] * (1 * degree if degree is not None else 0))
            new_image[:, :, 2] = image[:, :, 2] * (1-degree)
      else:
            raise ValueError("Method is not an accepted type.")

      new_image = np.clip(new_image, 0, 1)

      if verbose:
            plt.imshow(new_image)
            plt.show()
      
      return new_image