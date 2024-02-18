def rgb_to_hex(*args):
    """
    Convert RGB color to hexadecimal format.

    Parameters
    ----------
    *args
        Variable length argument list. Can either be three integers (r, g, b) or a single tuple with three integers.

    Returns
    -------
    str
        The hexadecimal color code as a string. The format of the returned string is '#RRGGBB'.
    
    Examples
    --------
    >>> rgb_to_hex(255, 0, 0)
    'FF0000'  # Red color

    >>> rgb_to_hex(0, 255, 0)
    '00FF00'  # Green color

    >>> rgb_to_hex(0, 0, 255)
    '0000FF'  # Blue color
    """

    def convert_color(color):
        # Calculate quotient and remainder for hex conversion
        quotient = color // 16
        remainder = int((color / 16 - quotient) * 16)
        # Convert to hex code 
        return '{:X}{:X}'.format(quotient, remainder)

    # Check if args is a tuple of length 3 or three separate arguments
    if len(args) == 1 and isinstance(args[0], (tuple)) and len(args[0]) == 3:
        r, g, b = args[0]
    elif len(args) == 3:
        r, g, b = args

    # Convert each color component to hexadecimal and concatenate
    return '#' + convert_color(r) + convert_color(g) + convert_color(b)
