'''
Developer :: soumyajitmahi7@gmail.com
'''

import matplotlib.colors as mcolors

def rgb(r, g, b):
    return (r, g, b)

def RGB(r, g, b):
    return (r, g, b)


def get_hex_color(color_input):
    # If the input is a string, it's assumed to be a color name or a hex color code
    if isinstance(color_input, str):
        # If the input starts with '#', it's assumed to be a hex color code
        if color_input.startswith('#'):
            return color_input.replace('#', '')
        else:
            hex_color = mcolors.CSS4_COLORS.get(color_input.lower())
            if hex_color is None:
                return f"Color name '{color_input}' not found in matplotlib CSS4_COLORS."
            else:
                return hex_color.replace('#', '')
        
    # If the input is a tuple of length 3, it's assumed to be an RGB color
    elif isinstance(color_input, tuple) and len(color_input) == 3:
        try:
            # Normalize the RGB values to the range [0, 1]
            normalized_rgb = tuple([x/255 for x in color_input])
            hex_color = mcolors.rgb2hex(normalized_rgb)
            return hex_color.replace('#', '')
        except ValueError:
            return f"Invalid RGB color: {color_input}. RGB colors should be 3-tuples of floats between 0 and 1."
    else:
        return f"Invalid color input: {color_input}. Please provide a color name or an RGB color."
    

if __name__=='__main__': 
    print(get_hex_color('crimson'))  # Outputs: dc143c
    print(get_hex_color(rgb(220,20,60)))  # Outputs: dc143c
    print(get_hex_color(RGB(220,20,60)))  # Outputs: dc143c
    print(get_hex_color('#dc143c'))  # Outputs: dc143c
