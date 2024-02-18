import numpy as np

def select_channel(image, channel, without=False):
    """
    Modifies an RGB image by either isolating or removing a specified color channel.

    Parameters:
    image (numpy.ndarray): The input image as a 3-dimensional RGB array.
    channel (str): The color channel to interact with. Valid options are 'r', 'g', or 'b' for red, green, or blue, respectively.
    without (bool, optional): If True, removes the specified channel from the image. Defaults to False.

    Returns:
    numpy.ndarray: The modified image with either the specified channel isolated or removed.

    Raises:
    ValueError: If an invalid channel is specified or the input image does not have 3 channels.
    TypeError: If the input image is not a NumPy array.

    Example usage:
    modified_image_with_channel = select_channel(original_image, 'g', without=False)  # Isolate green channel
    modified_image_without_channel = select_channel(original_image, 'r', without=True) # Remove red channel
    """

    if not isinstance(image, np.ndarray):
        raise TypeError("The input image must be a NumPy array.")

    if len(image.shape) != 3:
        raise ValueError("The dimension of the array should be 3.")

    if image.shape[2] != 3:
        raise ValueError("The input image must be a 3-channel RGB image.")
        

    channels = {'r': 0, 'g': 1, 'b': 2}
    if channel.lower() not in channels:
        raise ValueError("Invalid channel. Please choose 'r', 'g', or 'b'.")

    channel_idx = channels[channel.lower()]

   
    modified_image = np.copy(image)

    if without:
        modified_image[:, :, channel_idx] = 0
    else:
        other_channels = [i for i in range(3) if i != channel_idx]
        for idx in other_channels:
            modified_image[:, :, idx] = 0

    return modified_image

