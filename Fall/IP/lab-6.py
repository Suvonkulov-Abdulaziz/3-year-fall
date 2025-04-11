import cv2
import matplotlib.pyplot as plt
import numpy as np
import copy


def apply_filters(image_input, box, filt_size):
    """
    Applies a box filter to the input image.

    Parameters:
    - image_input: The input image as a 2D numpy array.
    - box: The box filter kernel.
    - filt_size: The size of the filter (should match the size of the box kernel).

    Returns:
    - image_box: The filtered image.
    """
    pad_size = int(np.floor(filt_size / 2))

    # Pad the image symmetrically
    image_padded = np.pad(image_input, pad_width=((pad_size, pad_size), (pad_size, pad_size)), mode='symmetric')

    # Make a deep copy of the input image for the output
    image_box = copy.deepcopy(image_input)

    # Get the dimensions of the input image
    row, column = image_input.shape

    # Apply the filter
    for i in range(row):
        for j in range(column):
            # Extract the current patch
            patch_curr = image_padded[i:i + filt_size, j:j + filt_size]

            # Multiply the patch by the filter (element-wise)
            results_box = box * patch_curr

            # Sum the results and assign to the output image
            image_box[i, j] = np.sum(results_box)

    return image_box


def box_filt(n):
    """
    Creates a box filter kernel of size n x n.
    """
    if n <= 0 or n % 2 == 0:
        raise ValueError("Window size must be a positive odd integer.")

    # Create a kernel with all elements equal to 1/(n*n)
    kernel = np.ones((n, n), np.float32) / (n * n)
    return kernel


image = cv2.imread('imgs/img-2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("a",image)
cv2.imshow("b", apply_filters(image,box_filt(5),5))

cv2.waitKey(0)