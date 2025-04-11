import cv2
import numpy as np

def selectiveMean(image, intensity_range=(100, 135)):

    # Ensure the image is in grayscale
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image

    lower, upper = intensity_range

    mask = (gray_image >= lower) & (gray_image <= upper)

    padded_image = cv2.copyMakeBorder(gray_image, 1, 1, 1, 1, cv2.BORDER_REFLECT)

    result_image = gray_image.copy()

    for i in range(1, padded_image.shape[0] - 1):
        for j in range(1, padded_image.shape[1] - 1):
            if mask[i-1, j-1]:  # Check if the original pixel is within the range
                # Extract the 3x3 neighborhood
                neighborhood = padded_image[i-1:i+2, j-1:j+2]
                # Calculate the mean and update the result image
                result_image[i-1, j-1] = np.mean(neighborhood)

    return result_image

# Example usage

# Load a grayscale image
image = cv2.imread("img-34.jpg", cv2.IMREAD_GRAYSCALE)

# Apply the selective mean filter
filtered_image = selectiveMean(image)

# Save or display the result
cv2.imwrite("filtered_image.jpg", filtered_image)
cv2.imshow("Filtered Image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
