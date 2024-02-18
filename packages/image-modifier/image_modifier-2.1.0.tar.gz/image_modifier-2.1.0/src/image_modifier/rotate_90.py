import numpy as np
def rotate_90(image):
    """
    Rotate an image by 90 degrees clockwise.

    Parameters:
        image: A jpeg image image with 3 channels. (This image is converted to an array for easy manipulation)

    Returns:
        array: A new 3D array representing the rotated image.

    Example:
    >>> original_image = np.array([[[255, 0, 0],   # Red
                            [0, 255, 0],   # Green
                            [0, 0, 255],   # Blue
                            [255, 255, 0]], # Yellow

                           [[128, 128, 128], # Gray
                            [255, 127, 0],   # Orange
                            [0, 255, 255],   # Cyan
                            [255, 0, 255]]]) # Magenta
    >>> rotated_image = rotate_90(original_image)
    >>> print(rotated_image)
        
        np.array([[[128, 128, 128],
        [255,   0,   0]],

       [[255, 127,   0],
        [  0, 255,   0]],

       [[  0, 255, 255],
        [  0,   0, 255]],

       [[255,   0, 255],
        [255, 255,   0]]])
    """
    image = np.array(image)

     # Check if the input image is empty
    if image.size == 0:
        return image

    # Check if the input image has 3 channels
    if not isinstance(image, np.ndarray):
        raise TypeError("The input image must be a NumPy array.")

    if len(image.shape) != 3:
        raise ValueError("The dimension of the array should be 3.")
    
    rows, cols, channels = image.shape
    rotated_image = np.empty((cols, rows, channels), dtype=image.dtype)
    for i in range(rows):
        for j in range(cols):
            rotated_image[j, rows - 1 - i, :] = image[i, j, :]
    return rotated_image
