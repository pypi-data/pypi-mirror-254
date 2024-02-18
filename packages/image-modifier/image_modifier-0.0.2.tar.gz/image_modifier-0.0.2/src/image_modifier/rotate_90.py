import numpy as np
def rotate_90(image):
    """
    Rotate a 2D image represented as a list of lists by 90 degrees clockwise.

    Parameters:
        image (list of lists): A 2D list representing the original image.

    Returns:
        list of lists: A new 2D list representing the rotated image.

    Example:
    >>> original_image = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> rotated_image = rotate_90(original_image)
    >>> print(rotated_image)
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    """
    image = np.array(image)
    if image.size == 0:
        return image
    rows, cols, channels = image.shape
    rotated_image = np.empty((cols, rows, channels), dtype=image.dtype)
    for i in range(rows):
        for j in range(cols):
            rotated_image[j, rows - 1 - i, :] = image[i, j, :]
    return rotated_image
