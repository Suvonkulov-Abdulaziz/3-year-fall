import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretch(image, new_min, new_max):
    old_min = np.min(image)
    old_max = np.max(image)
    stretched = ((image - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
    return np.clip(stretched, new_min, new_max).astype(np.uint8)

def normalize(image):
    normalized = (image - np.min(image)) / (np.max(image) - np.min(image))
    return normalized

# Load an image (replace 'image.jpg' with your image path)
image = cv2.imread('imgs/5.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
normalized_image = normalize(image)

# Apply contrast stretching to non-normalized image
new_min, new_max = 0, 255
stretched_non_normalized = contrast_stretch(image, new_min, new_max)

# Apply contrast stretching after normalization
stretched_normalized = contrast_stretch((normalized_image * 255).astype(np.uint8), new_min, new_max)

# Display results to observe differences
plt.subplot(1, 2, 1)
plt.title('Stretched Non-Normalized')
plt.imshow(stretched_non_normalized, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Stretched Normalized')
plt.imshow(stretched_normalized, cmap='gray')
plt.show()
