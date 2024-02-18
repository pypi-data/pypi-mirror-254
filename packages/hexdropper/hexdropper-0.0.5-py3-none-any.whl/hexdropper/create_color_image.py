import os
import re
from PIL import Image, ImageDraw

def create_color_image(hex_code, image_size=(200, 200), output_path=None):
    """
    Create an image with a specific background color and display the hex code.

    Parameters
    ----------
    hex_code : str
        A hexadecimal color code string (e.g., '#FF5733'), without the '#' symbol.
    image_size : tuple of int, optional
        The size of the image as a (width, height) tuple. Default is (200, 200).
    output_path : str, optional
        The file path where the image will be saved. If not specified, the image
        will be saved in the current working directory with a default name.

    Returns
    -------
    None
        The function saves the created image as a PNG file with the name based on
        the hex code (e.g., 'FF5733.png').

    Examples
    --------
    >>> create_color_image('#FF5733')
    # This will create and save an image with a red background and 'FF5733' text in the center.

    >>> create_color_image('#00FF00', (100, 100), '/path/to/save/image.png')
    # This will create a 100x100 green background image with '00FF00' text in the center and save it to the specified path.
    """
    # Validate the hex code
    if not bool(re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex_code)):
        raise ValueError("Invalid hex code provided, hexcode should be a string with the '#' symbol")
    
    # Check if the hex_code is a string
    if not isinstance(hex_code, str):
        raise ValueError("hex_code should be a string")
    
    # Check if image_size is a tuple of two integers
    if not (isinstance(image_size, tuple) and len(image_size) == 2):
        raise ValueError("image_size should be a (width, height) tuple")
    
    if not (isinstance(image_size[0], int) and isinstance(image_size[1], int)):
        raise ValueError("image_size should be a tuple of int")
    
    # Process the hex code for filename
    hex_code_for_filename = hex_code.lstrip('#')

    # If no output path is provided, use the hex code as the file name
    if output_path is None:
        output_path = hex_code_for_filename  + '.png'
    else:
        # Ensure the directory of the output path exists, create it if not
        parent_dir = os.path.dirname(output_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

    # Create a new image with the specified color
    image = Image.new("RGB", image_size, hex_code)

    # Save the image to the specified path
    image.save(output_path)