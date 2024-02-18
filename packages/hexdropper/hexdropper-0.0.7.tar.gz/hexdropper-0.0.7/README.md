# hexdropper

[![ci-cd](https://github.com/UBC-MDS/hexdropper/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/hexdropper/actions/workflows/ci-cd.yml) <!-- CI/CD Badge --> 
[![codecov](https://codecov.io/gh/UBC-MDS/hexdropper/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/hexdropper) <!-- CodeCov Badge -->
[![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/) <!-- Python Version Badge -->
[![Documentation Status](https://readthedocs.org/projects/hexdropper/badge/?version=latest)](https://hexdropper.readthedocs.io/en/latest/?badge=latest) <!-- Documentation Status Badge -->
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/hexdropper) <!-- Code Size Badge -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- License Badge -->
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) <!-- Project Status Badge -->
[![version](https://img.shields.io/github/v/release/UBC-MDS/hexdropper)](https://github.com/UBC-MDS/hexdropper/releases) <!-- Version Status Badge -->
[![release](https://img.shields.io/github/release-date/UBC-MDS/hexdropper)](https://github.com/UBC-MDS/hexdropper/releases) <!-- Release Date Badge -->


A Python package designed for graphic designers, developers, and color enthusiasts. It simplifies the process of obtaining hex color codes from images. Given a cropped image, hexdropper quickly identifies and outputs the corresponding hex color code, streamlining design and development workflows.

## Contributors

- [Julia Everitt](https://github.com/juliaeveritt)
- [Hancheng Qin](https://github.com/hchqin)
- [Joey Wu](https://github.com/joeywwwu)
- [Mona Zhu](https://github.com/monazhu)

## Features
The key functionalities include:

- `read_image`: This function reads image files, and converts the image into a numpy array of RGB values.

- `most_common_rgb`: This function identifies the most common RGB value within the given image. 

- `rgb_to_hex`: This function converts RGB values into their corresponding hex color codes. 

- `create_color_image`: This function generates an image displaying the hex code on a background of the color it represents. 

## Installation

The current package is still under development. We have provided below a set of developer installation instructions.

### User Installation

To install `hexdropper`, simply run the following command in your terminal:

```bash
$ pip install hexdropper
```

This will download and install the latest version of `hexdropper` from the Python Package Index (PyPI).

### Developer Installation

#### Getting Started

Clone a copy of [this repository](https://github.com/UBC-MDS/hexdropper) onto your local machine. See [this page](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for details on how to clone a repository.

#### Setting up a Conda Environment

We recommend creating an isolated conda environment on your local machine to test and develop the package. To create and activate a conda environment for this project, type in the below command in your terminal.

```bash
$ conda create --name hexdropper python=3.9 -y 
$ conda activate hexdropper
```

#### Using Poetry for Package Management

Please follow the official poetry [documentation](https://python-poetry.org/docs/) to install poetry on your local machine. Note that poetry should **always be installed on a dedicated virtual environment.**

Navigate to the root directory of your project folder. Ensure that your virtual conda environment has been activated. Run the following line of code to install existing packages required for the `hexdropper` package:

```bash
$ poetry install
```

If you would like to add a new package or dependency, run the following code in your terminal, replacing `[name-of-dependency]` with the package you would like to install (e.g., numpy)

```bash
$ poetry add [name-of-dependency]
```

You can also pin the specific version of the package you would like to install like so: 

```bash
$ poetry add numpy=1.22.0 --dry-run
```

#### Running Tests

Ensure `pytest` and `pytest-cov` are installed via poetry. If not, run the following in your terminal: 

```bash
$ poetry add --group dev pytest
$ poetry add --group dev pytest-cov
```

Ensuring that your test scripts are completed, then run the following code in your terminal to run the tests for all functions in the package: 

```bash
$ pytest tests/
```

To run coverage tests, run the following command:

```bash
$ pytest tests/ --cov=hexdropper
```


## Usage
Rather than using multiple external tools to obtain the necessary hex code to better customize one's graphics or visualization, we developed a package, `hexdropper`, that would make it easier for users to directly obtain the desired hex code right here in Python.

### Package set up

Once the package is installed, import the package directly by running the following command in Python

```python
from hexdropper import *
```

### Read image

Start by reading in a cropped image containing the color you would like to match, using the `read_image` function and specifying the path to the image on the device. The image does not need to be perfectly cropped, as long as the color we are interested in is most prominent.

Note that the input image must be of type **jpg** or any other color formats that only have 3 color channels. Formats like png have 4 channels (RGB and an alpha channel that controls transparency). 

```python
image = read_image('img/cropped_img.jpg') 
```

### Obtaining the most common RGB

Now that the cropped image has been imported as an array, we can extract its RGB values. 

Sometimes, it might not be feasible to crop an image perfectly. For instance, a user may have missed a few dark pixels at the edge of the cropped image, or perhaps, the image itself is a bit noisy. To account for these situations, the function `most_common_rgb` takes the most common RGB value in the cropped image and outputs it as a tuple that corresponds to the red, green, and blue channels respectively.

```python
rgb_val = most_common_rgb(image)
```

### Converting RGB to hexadecimal format

Once we have obtained the most common RGB value from an image using the `most_common_rgb` function, we can convert its output using the `rgb_to_hex` function. This function returns a string representing the color in hexadecimal format.

```python
rgb_to_hex(rgb_val) 
```

In addition to accepting tuples, the `rgb_to_hex` function can also accept three separate integers representing the red, green, and blue color channels. 

```python
rgb_to_hex(8, 181, 212)
```

### Export the extrated color as an image

The user can also create a new image that solely features the extracted color. This allows for a visual reference of the color for other users (particularly if they do not have a programming background) when designing graphics that coordinate with MDS logo's color scheme.

By default, the function will create a 200x200 pixel image with the extrated color. By default, the image will be saved in the current working directory and named with the color code (e.g., 08B5D4.png).

```python
hex_code = rgb_to_hex(8, 181, 212)
create_color_image(hex_code)
```

The user can also change the size of the image and the directory to save the image in. we can do so by adjusting the parameters of the `create_color_image` function.

```python
# Create a 100x100 pixel image and save it to a specific path
create_color_image(hex_code, image_size=(100, 100), output_path='/path/to/save/08B5D4.png')
```

This package can be especially useful for designers and developers who need visuals that match or complement colors extracted from images, as demonstrated with the UBC MDS Logo in our example.

If you have any questions or feedback about `hexdropper`, feel free to reach out or contribute to our project. Happy color dropping!


## Python Ecosystem Context
hexdropper fills a unique niche in the Python ecosystem. While there are packages like Pillow for image processing and Matplotlib for visualization, hexdropper specifically focuses on color extraction and conversion, a task not directly addressed by existing packages. Its ability to directly translate image colors into hex codes and visually represent them is distinctive, setting it apart from general-purpose image manipulation tools. Related packages include:

- [Pillow](https://python-pillow.org/): For comprehensive image processing capabilities.
- [Matplotlib](https://matplotlib.org/): For creating visualizations and figures.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`hexdropper` was created by Julia Everitt, Hancheng Qin, Joey Wu, Mona Zhu. It is licensed under the terms of the MIT license.

## Credits

`hexdropper` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

