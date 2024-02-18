# Pythoshop

<img src="https://github.com/UBC-MDS/Pythoshop/blob/main/img/cover.png?raw=true" height="300">

Pythoshop is a Python package designed to provide a set of handy image processing functions for simple yet effective adjustments to images. Whether you need to tweak brightness, adjust aspect ratios, transform images, or apply filters, Pythoshop has you covered.

[![Documentation Status](https://readthedocs.org/projects/pythoshop/badge/?version=latest)](https://pythoshop.readthedocs.io/en/latest/?badge=latest) ![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![version](https://img.shields.io/github/v/release/UBC-MDS/pythoshop) ![release](https://img.shields.io/github/release-date/UBC-MDS/pythoshop) [![ci-cd](https://github.com/UBC-MDS/pythoshop/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/pythoshop/actions/workflows/ci-cd.yml) [![codecov](https://codecov.io/gh/UBC-MDS/pythoshop/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/pythoshop) [![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Functions

- **adjust_brightness(image, brightness_factor, verbose):**
  Adjusts the brightness of an image object in the form of a NumPy array. The `brightness_factor` parameter allows fine-tuning the brightness level. Returns an updated NumPy array.

- **resize_image(image, height, width, method:, verbose):**
  This function takes a Numpy array image object and adjusts the image to have the inputted dimensions using the selected method. Returns an updated NumPy array.

- **transform_image(image, method, direction, verbose):**
  Transforms a NumPy array image object based on the specified method and direction. Options include "rotate" or "flip", allowing users to orient images as needed. Returns an updated NumPy array.

- **apply_filter(image, method, degree, verbose):**
  Applies a filter to an image object in the form of a NumPy array. Users can choose from filter methods and adjust the degree of filtering to achieve the desired visual effect. Returns an updated NumPy array.


## Python Ecosystem Integration

Pythoshop complements existing image processing libraries in the Python ecosystem, offering a lightweight solution for common image adjustments. While other comprehensive libraries like Pillow and OpenCV provide extensive functionalities, Pythoshop focuses on simplicity and ease of use. If you need quick and straightforward image processing without the overhead of more extensive libraries, Pythoshop is the ideal choice.

### Related Packages:

- [Pillow](https://python-pillow.org/): A powerful image processing library in Python, providing comprehensive features for image manipulation and editing.

- [OpenCV](https://opencv.org/): An open-source computer vision and machine learning library, suitable for complex image processing tasks and computer vision applications.


## Installation

This package is currently under development. Hence the installation instructions are as below.
First, you need to make sure you have installed conda and poetry.

**To install Anaconda:**

1. Download the Anaconda Installer:
- Visit the [Anaconda Download page](https://www.anaconda.com/download)
- Choose the installer for your operating system (Windows, macOS, or Linux).
- Select the version for Python 3.x.
2. Run the Installer:
- Windows: Open the downloaded .exe file and follow the instructions. It's recommended to check the option to "Add Anaconda to my PATH environment variable" for easy use in the command prompt, but be aware this can interfere with other software.
- macOS or Linux: Open Terminal, navigate to the directory containing the downloaded script, and run it with bash Anaconda3-xxxxxx.sh, following the on-screen instructions.
3. Verify Installation:
Open your command line interface (CLI) and type `conda list`. If Anaconda is installed properly, you should see a list of installed packages.

**To install `poetry`, follow the instructions below:**

We recommend installing `Poetry` using their official installer while referring to their official [poetry documentation](https://python-poetry.org/docs/) for detailed installation instructions and support. (You will be installing poetry in your base environment, make sure to add poetry to system path on windows)

Now navigate to the folder where you want to download the pythoshop package.
```bash
# 1. clone the repo
$ git clone git@github.com:UBC-MDS/Pythoshop.git
```

```bash
# 2. create virtual environment
$ conda create --name pythoshop python=3.9 -y
$ conda activate pythoshop
```

```bash
# 3. install the package at the command line from the root package directory:
$ poetry install
```
In the future 
Once this package is published on PyPi, the package will be available for installation via:
```
pip install pythoshop
```

## Usage
To unleash the power of Pythoshop, follow the simple steps below:
1. Load the functions from Pythoshop
```python
from pythoshop import adjust_brightness, resize_image, transform_image, apply_filter
```
2. Make sure you assign the images you need to transform in the form of NumPy arrays.
3. Now, You can process your images, below is an example of one how you can change the brightness of your image:
### Adjust Brightness

```python
from pythoshop import adjust_brightness, resize_image, transform_image, apply_filter
import matplotlib.image as mpimg

image = mpimg.imread('path/to/input_image.jpg')
brightness_factor = 1.5  # Adjust as needed

adjust_brightness.adjust_brightness(image, brightness_factor)
```

For further details on how you can use the other 3 functions, please refer to the docs linked [here](https://pythoshop.readthedocs.io/en/latest/?badge=latest). 

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.


## Contributors

Salva Umar, 
Jenny Lee, 
Ella Hein, 
Runtian (Rachel) Li

## License

`Pythoshop` was created by Salva Umar, Jenny Lee, Ella Hein, Rachel Li. It is licensed under the terms of the GNU GPLv3 license.

## Credits

`pythoshop` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
