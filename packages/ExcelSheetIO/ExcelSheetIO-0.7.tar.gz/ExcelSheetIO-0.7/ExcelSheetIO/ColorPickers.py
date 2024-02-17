'''
Developer :: soumyajitmahi7@gmail.com
'''

import matplotlib.colors as mcolors
import re

def rgb(r, g, b):
    return (r, g, b)

def RGB(r, g, b):
    return (r, g, b)

def _get_hex_color(color_input):
    # If the input is a string, it's assumed to be a color name, a hex color code, or an RGB color
    if isinstance(color_input, str):
        # If the input is a valid hex color code without '#'
        if re.match(r'^[A-Fa-f0-9]{6}$', color_input):
            return color_input.upper()
        # If the input is a valid hex color code with 8 characters, ignore the first two characters
        elif re.match(r'^[A-Fa-f0-9]{8}$', color_input):
            return color_input[2:].upper()
        # If the input starts with '#', it's assumed to be a hex color code
        elif color_input.startswith('#'):
            return color_input.replace('#', '').upper()
        # If the input starts with 'rgb(', it's assumed to be an RGB color
        elif color_input.lower().startswith('rgb('):
            rgb_values = re.findall(r'\d+', color_input)
            if len(rgb_values) == 3:
                return _get_hex_color(tuple(map(int, rgb_values)))
            else:
                return f"Invalid RGB color: {color_input}. RGB colors should be in the format 'rgb(r, g, b)'."
        else:
            hex_color = mcolors.CSS4_COLORS.get(color_input.lower())
            if hex_color is None:
                # Check if the input is a valid hex color code
                if re.match(r'^[A-Fa-f0-9]{6}$', color_input):
                    return color_input.upper()
                else:
                    return f"Color name '{color_input}' not found in matplotlib CSS4_COLORS."
            else:
                return hex_color.replace('#', '').upper()
    # Rest of the code...

    # If the input is a tuple of length 3, it's assumed to be an RGB color
    elif isinstance(color_input, tuple) and len(color_input) == 3:
        try:
            # Normalize the RGB values to the range [0, 1]
            normalized_rgb = tuple([x/255 for x in color_input])
            hex_color = mcolors.rgb2hex(normalized_rgb)
            return hex_color.replace('#', '').upper()
        except ValueError:
            return f"Invalid RGB color: {color_input}. RGB colors should be 3-tuples of integers between 0 and 255."
    else:
        return f"Invalid color input: {color_input}. Please provide a color name, a hex color code, or an RGB color."


if __name__=='__main__': 
    print(_get_hex_color('Salmon'))  # Outputs: FA8072
    print(_get_hex_color('rgb(220,20,60)'))  # Outputs: DC143C
    print(_get_hex_color(rgb(220,20,60)))  # Outputs: DC143C
    print(_get_hex_color((220,20,60)))  # Outputs: DC143C
    print(_get_hex_color(RGB(220,20,60)))  # Outputs: DC143C
    print(_get_hex_color('#dc143c'))  # Outputs: DC143C
    print(_get_hex_color('FA8072'))  # Outputs: FA8072
    print(_get_hex_color('00000000'))  # Outputs: 000000
    print(_get_hex_color('00FA8072'))  # Outputs: 000000
