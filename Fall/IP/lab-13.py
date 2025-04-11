import matplotlib.pyplot as plt
from skimage.morphology import opening, closing, square
from skimage import data  # For loading a sample image
from skimage import color  # To convert images to grayscale if needed
import cv2
image = cv2.imread('img-4.png', cv2.IMREAD_GRAYSCALE)

# Load a sample image (you can replace this with your own image)
# image = color.rgb2gray(data.coins())

# Apply opening and closing with a square structuring element of size 3
opened = opening(image, square(3))
closed = closing(image, square(3))

# Display results
fig, axes = plt.subplots(1, 3, figsize=(12, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original Image")
axes[1].imshow(opened, cmap='gray')
axes[1].set_title("Opened Image")
axes[2].imshow(closed, cmap='gray')
axes[2].set_title("Closed Image")
plt.tight_layout()
plt.show()




















