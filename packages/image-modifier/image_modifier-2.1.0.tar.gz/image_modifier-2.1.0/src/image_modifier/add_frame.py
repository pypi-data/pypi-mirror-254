import numpy as np

def add_pad(image, border_size=30):
    """
    Adds padding to all sides of an image.

    This function applies a uniform padding around the image. The padding is added to the top, 
    bottom, left, and right sides of the image. The added padding is black by default.

    Parameters:
    image (numpy.ndarray): The input image to which padding will be added. 
                           It should be a 3-dimensional array representing an RGB image.
    border_size (int, optional): The size of the padding to be added to each side of the image. 
                                 Defaults to 30.

    Returns:
    numpy.ndarray: The padded image. The size of the output image will be increased by 
                   2 * border_size in both height and width.

    Note:
    The padding is only added to the spatial dimensions (height and width) of the image. 
    The depth (color channels) of the image remains unaltered.

    Example usage:
    padded_image = add_pad(original_image, border_size=50)
    """
    pad_width = ((border_size, border_size), (border_size, border_size), (0, 0))
    return np.pad(image, pad_width=pad_width)


def make_borders_colored(image, border_size=30, color_name="red"):
    """
    Adds a colored border to all sides of an image. This function now supports both RGB and RGBA images.

    Parameters:
    image (numpy.ndarray): The input image to which the border will be added. 
                           It should be a 3-dimensional array representing an RGB or RGBA image.
    border_size (int, optional): The thickness of the border to be added to each side of the image. 
                                 Defaults to 30 pixels.
    color_name (str or tuple, optional): The color of the border. This can be a predefined color name 
                                         ('red', 'green', 'blue', 'yellow', 'black', 'white') or an RGB/RGBA tuple. 
                                         Defaults to 'red'.

    Returns:
    numpy.ndarray: The image with the colored border added. The size of the output image remains unchanged.

    Raises:
    ValueError: If the border size is too large for the given image dimensions or if the provided color name 
                is not valid.
    """

    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "black": (0, 0, 0),
        "white": (255, 255, 255)
    }

    if image.shape[0] < 2 * border_size or image.shape[1] < 2 * border_size:
        raise ValueError("Border size is too large for the given image dimensions.")

    if color_name in colors:
        border_color = colors[color_name]
    elif isinstance(color_name, tuple) and (len(color_name) == 3 or len(color_name) == 4):
        border_color = color_name
    else:
        raise ValueError("Invalid color name or RGB/RGBA value.")

    channel_count = image.shape[2]  # Number of color channels in the image

    # Ensure border_color matches the image's color channel count
    if len(border_color) != channel_count:
        if len(border_color) == 3 and channel_count == 4:
            border_color = (*border_color, 255)  # Add full opacity to RGB color
        else:
            raise ValueError("Color and image channel mismatch.")

    # Make a writable copy of the image
    writable_image = np.copy(image)

    # Set the border pixels to the specified color
    writable_image[:border_size, :] = border_color  # Top border
    writable_image[-border_size:, :] = border_color  # Bottom border
    writable_image[:, :border_size] = border_color  # Left border
    writable_image[:, -border_size:] = border_color  # Right border

    return writable_image


def add_frame(image, border_size=30, color_name="red", overlay=True):
    """
    Adds a frame to an image either by overlaying a colored border or by first padding the image and 
    then adding a colored border. The function supports both RGB images and PNG images with alpha channels.

    If 'overlay' is set to True, the function overlays a colored border on the image without changing its size.
    If 'overlay' is False, the function first adds padding (increasing the image size) and then applies the colored border.

    Parameters:
    image (numpy.ndarray): The input image to which the frame will be added. 
                           It should be a 3 or 4-dimensional array.
    border_size (int, optional): The thickness of the border/frame to be added. Defaults to 100 pixels.
    color_name (str or tuple, optional): The color of the border/frame. Can be a predefined color name 
                                         (like 'red', 'green', 'blue', etc.) or an RGB tuple. Defaults to 'red'.
    overlay (bool, optional): A flag to determine if the border should be overlaid on the existing image (True) 
                              or if the image should be first padded (False). Defaults to True.

    Returns:
    numpy.ndarray: The image with the added frame. The size of the output image depends on the 'overlay' flag.

    Raises:
    ValueError: If the input image is grayscale or if the color name is invalid.

    Example usage:
    framed_image_overlay = add_frame(original_image, border_size=50, color_name='blue', overlay=True)
    framed_image_padded = add_frame(original_image, border_size=50, color_name='green', overlay=False)
    """

    if len(image.shape) < 3:
        raise ValueError("Grayscale pictures supported will be added in a future version")

    if overlay:
        # Apply colored borders and return the result
        # Input image remains the same size
        return make_borders_colored(image, border_size, color_name)    
    else:
        # Add padding and then apply colored borders
        # Input image is enlarged by the border_size on all four sides
        padded_image = add_pad(image, border_size)
        return make_borders_colored(padded_image, border_size, color_name)

