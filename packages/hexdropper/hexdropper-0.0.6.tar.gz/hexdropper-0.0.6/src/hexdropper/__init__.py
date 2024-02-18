# read version from installed package
from importlib.metadata import version
__version__ = version("hexdropper")

# populate package namespace
from hexdropper.read_image import read_image
from hexdropper.most_common_rgb import most_common_rgb 
from hexdropper.rgb_to_hex import rgb_to_hex
from hexdropper.create_color_image import create_color_image