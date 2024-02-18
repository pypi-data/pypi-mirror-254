# ImageModifier

[![](https://img.shields.io/badge/language-Python-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/UBC-MDS/image_modifier.svg)](https://github.com/UBC-MDS/image_modifier/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/image_modifier.svg)](https://github.com/UBC-MDS/image_modifier/commits/main)
[![GitHub release](https://img.shields.io/github/release/UBC-MDS/image_modifier.svg)](https://github.com/UBC-MDS/image_modifier/releases)
[![Documentation Status](https://readthedocs.org/projects/image-modifier/badge/?version=latest)](https://image-modifier.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/UBC-MDS/image_modifier/graph/badge.svg?token=Je2mYFYCUP)](https://codecov.io/gh/UBC-MDS/image_modifier)

![Created by DALL·E](https://github.com/UBC-MDS/image_modifier/blob/f9b89b556437eaab10e84b01f8aa59a59cbd0e9d/docs/logo.png)

*Created by DALL.E*

ImageModifier is a Python package dedicated to providing an intuitive and efficient way to manipulate images. This package focuses on core image processing functions, allowing users to easily modify images through operations like rotating, slicing, adding frame, and adjusting RGB channels. The primary goal is to offer a straightforward way for basic yet powerful image transformations, making it a useful tool for image processing.

## Contributors

Chun Li, Celeste Zhao, He Ma, Karan Khubdikar

## Motivation

ImageModifier offers a streamlined and intuitive approach, making it highly accessible to a wide range of users, unlike many complex image processing tools that can be overwhelming for beginners and cumbersome for quick tasks. This package caters to both novices seeking an easy entry point into image manipulation and experienced users looking for a tool to perform quick modifications without the overhead of more complex software. With core functionalities like rotating, slicing, adding frames, and selecting RGB channels, ImageModifier simplifies these common tasks, allowing users to achieve their goals with minimal coding effort.

## Functions

**rotate_90**: Rotating an image by 90 degrees clockwise.

**add_frame**: Adding a frame to an image.

**select_channel**: Modifying an image with/without a specified RGB channel.

**slice_image**: Slicing an image into a specified number of horizontal and vertical slices.


## Documentation

The package documentation, including installation instructions, usage examples and API details, is available on ReadTheDocs and accessible [here](https://image-modifier.readthedocs.io/en/latest).


## Installation

### For user

#### Installing the package

```bash
$ pip install image_modifier
```

### For developer

#### Setting up the project

Clone the repository to your local machine:

```bash
$ git clone https://github.com/UBC-MDS/image_modifier
$ cd image_modifier/
```

Create and activate the virtual environment:

```bash
$ conda env create -f image_modifier.yml
$ conda activate image_modifier
```

Install the packages via poetry:

```bash
$ poetry install
```

#### Running unit tests

To run unit tests to ensure the functionality of the modifications, execute:

```bash
$ poetry run pytest
```

To include code coverage reporting, can also run:

```bash
$ poetry run pytest --cov=image_modifier
```

## Usage

### **Importing libraries and image**

The following code can be used to import libraries and an image in python.

```bash
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> from PIL import Image

>>> image = Image.open("src/ubc.jpeg")  # Example for demonstration
>>> image_ary = np.array(image)
```

### **Function usage**

#### **Rotate the image by 90 degree clockwise**

```bash
>>> from image_modifier.rotate_90 import rotate_90

>>> rotated_image = rotate_90(image_ary)
>>> plt.imshow(rotated_image)
```

#### **Add frame to the image**

```bash
>>> from image_modifier.add_frame import add_frame

>>> framed_image = add_frame(image_ary, border_size=30, color_name='blue', overlay=True)
>>> plt.imshow(framed_image)
```

#### **Select color channel**

```bash
>>> from image_modifier.select_channel import select_channel

>>> colored_image = select_channel(image_ary, 'r')
>>> plt.imshow(colored_image)
```

#### **Slice the image**

```bash
>>> from image_modifier.slice_image import slice_image

>>> slices = slice_image(image_ary, horizontal_slices=2, vertical_slices=2)
```

### **Usage examples**

Detailed usage examples can be found [here](https://image-modifier.readthedocs.io/en/latest/example.html).


## Position within the Python ecosystem

ImageModifier bridges the gap between highly complex image processing libraries and the need for straightforward, user-friendly image manipulation tools. Its focus on core image processing functionalities—such as rotating, slicing, adding frames, and adjusting RGB channels. While Python boasts powerful image processing libraries like OpenCV and PIL/Pillow, these can often be overwhelming for beginners or overkill for simple tasks. ImageModifier's simplicity makes it an attractive starting point for newcomers to image processing, as well as a quick and efficient tool for experienced users needing to perform routine tasks without the overhead of more complex libraries.

## Contributing

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`image_modifier` was created by Karan Khubdikar, Celeste Zhao, He Ma, Chun Li. It is licensed under the terms of the MIT license, and more details can be found in the [LICENSE](LICENSE).

## Credits

`image_modifier` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
