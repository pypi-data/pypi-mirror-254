import numpy as np
import matplotlib.pyplot as plt

def image_break_into_slices(image, horizontal_slices, vertical_slices):
    """
    Slices an image into smaller sections (slices) based on specified horizontal and vertical divisions.

    This function segments an image array into smaller rectangular portions. The image is divided into a grid
    defined by the number of horizontal and vertical slices. Each portion of the grid corresponds to a slice.

    Parameters:
        image (numpy.ndarray): The image to be divided, represented as a 3D RGB array.
        horizontal_slices (int): The number of slices along the horizontal axis.
        vertical_slices (int): The number of slices along the vertical axis.

    Returns:
        list[list[numpy.ndarray]]: A list where each sublist contains numpy arrays representing horizontal slices.
        The overall structure represents the entire sliced image.

    Example:
    --------
    Given a numpy array representing an 8x8 pixel image:
    
    >>> slices = image_break_into_slices(image, 2, 2)
    
    This will return a list with 4 sublists (2x2 grid), each sublist containing a numpy array for a 4x4 pixel slice.
    """
    # Check inputs
    if not isinstance(image, np.ndarray):
        raise TypeError("The 'image' should be a numpy.ndarray.")
    if len(image.shape) != 3:
        raise ValueError("The 'image' should be a 3D array.")
    if not (isinstance(horizontal_slices, int) and isinstance(vertical_slices, int)):
        raise TypeError("Both 'horizontal_slices' and 'vertical_slices' should be integers.")
    if horizontal_slices <= 0 or vertical_slices <= 0:
        raise ValueError("Both 'horizontal_slices' and 'vertical_slices' should be greater than 0.")
    
    # Calculate the height and width of the image
    image_height = len(image)
    image_width = len(image[0]) if image_height > 0 else 0

    # Adjust slice numbers if they exceed image dimensions
    horizontal_slices = min(horizontal_slices, image_height)
    vertical_slices = min(vertical_slices, image_width)

    # Calculate the height and width of each slice
    slice_height = max(1, image_height // horizontal_slices)
    slice_width = max(1, image_width // vertical_slices)

    # Create a 2D list to hold the image slices
    slices = []

    # Slice the image and add each slice to the list
    for h in range(horizontal_slices):
        row = []
        for v in range(vertical_slices):
            # Calculate the coordinates of the slice
            top = h * slice_height
            bottom = min((h + 1) * slice_height, image_height)
            left = v * slice_width
            right = min((v + 1) * slice_width, image_width)

            # Create the slice as a 2D list
            slice = [row[left:right] for row in image[top:bottom]]
            row.append(np.array(slice))
        slices.append(row)

    return slices
    
def slice_image(image, horizontal_slices=2, vertical_slices=2, display_images=True):
    """
    Visualizes slices of an image in a grid format using matplotlib and returns the slices.

    This function first uses `image_break_into_slices` to divide the image into smaller sections and then 
    displays these slices in a grid layout using matplotlib. Each slice is shown in a subplot with its position in the grid.

    Parameters:
        image (numpy.ndarray): The image to be sliced and displayed.
        horizontal_slices (int, optional): The number of horizontal divisions for slicing. Default is 2.
        vertical_slices (int, optional): The number of vertical divisions for slicing. Default is 2.
        display_images (bool): If True, display the images using matplotlib. Default is True.

    Returns:
        list[list[numpy.ndarray]]: A list of numpy arrays, each representing a slice of the original image.

    The function assumes the slices form a rectangular grid and directly displays the plot using matplotlib.
    """

    # Check inputs
    if not isinstance(image, np.ndarray):
        raise TypeError("The 'image' should be a numpy.ndarray.")
    if len(image.shape) != 3:
        raise ValueError("The 'image' should be a 3D array.")
    if not (isinstance(horizontal_slices, int) and isinstance(vertical_slices, int)):
        raise TypeError("Both 'horizontal_slices' and 'vertical_slices' should be integers.")
    if horizontal_slices <= 0 or vertical_slices <= 0:
        raise ValueError("Both 'horizontal_slices' and 'vertical_slices' should be greater than 0.")

    # Slice the image
    slices = image_break_into_slices(image, horizontal_slices, vertical_slices)

    # Set up the plot dimensions
    n_rows = len(slices)
    n_cols = len(slices[0])
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols)

    if n_rows == 1 or n_cols == 1:
        axes = np.array(axes).reshape(n_rows, n_cols)

    # Prepare display of each slice
    for i in range(n_rows):
        for j in range(n_cols):
            ax = axes[i, j]
            ax.imshow(slices[i][j])
            ax.set_title(f"Slice {i*n_cols + j + 1}")
            ax.axis('off')
    plt.tight_layout()

    # Slice display
    if display_images:
        plt.show()
    else:
        pass

    return slices