
import cv2
import matplotlib.pyplot as plt
from skimage import exposure
import numpy as np

#
# # Read the grayscale image
# image = cv2.imread('imgs/img-2.jpg', cv2.IMREAD_GRAYSCALE)
#
# # Apply histogram equalization to improve contrast
# equalized_image = cv2.equalizeHist(image)
#
# # Set up a figure to display both images and their histograms
# plt.figure(figsize=(12, 6))
#
# # Display the original image
# plt.subplot(2, 2, 1)
# plt.imshow(image, cmap='gray')
# plt.title('Original Image')
# plt.axis('off')
#
# # Display the histogram of the original image
# plt.subplot(2, 2, 2)
# plt.hist(image.ravel(), bins=256, range=[0, 256], color='black')
# plt.title('Histogram (Original)')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
#
# # Display the equalized image
# plt.subplot(2, 2, 3)
# plt.imshow(equalized_image, cmap='gray')
# plt.title('Equalized Image')
# plt.axis('off')
#
# # Display the histogram of the equalized image
# plt.subplot(2, 2, 4)
# plt.hist(equalized_image.ravel(), bins=256, range=[0, 256], color='black')
# plt.title('Histogram (Equalized)')
# plt.xlabel('Pixel Intensity')
# plt.ylabel('Frequency')
#
# # Adjust layout to prevent overlap
# plt.tight_layout()
#
# # Show the plot
# plt.show()


# # Read a color image
# color_image = cv2.imread('imgs/img-2.jpg')
#
# # Split the image into B, G, R channels
# b, g, r = cv2.split(color_image)
#
# # Equalize each channel separately
# equalized_b = cv2.equalizeHist(b)
# equalized_g = cv2.equalizeHist(g)
# equalized_r = cv2.equalizeHist(r)
#
# # Merge the equalized channels back into a color image
# equalized_color_image = cv2.merge([equalized_g,equalized_b, equalized_r])
#
# # Display the original and equalized images
# plt.figure(figsize=(12, 6))
#
# # Original color image
# plt.subplot(1, 2, 1)
# plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
# plt.title('Original Color Image')
# plt.axis('off')
#
# # Equalized color image (separate channel equalization)
# plt.subplot(1, 2, 2)
# plt.imshow(cv2.cvtColor(equalized_color_image, cv2.COLOR_BGR2RGB))
# plt.title('Equalized Color Image (Channels Separately)')
# plt.axis('off')
#
# # Adjust layout to prevent overlap
# plt.tight_layout()
#
# # Show the plot
# plt.show()

# Read two grayscale images (source and target)
image_source = cv2.imread('imgs/images.jpeg', cv2.IMREAD_GRAYSCALE)
image_target = cv2.imread('imgs/img-2.jpg', cv2.IMREAD_GRAYSCALE)

# Perform histogram matching
matched_image = exposure.match_histograms(image_source, image_target)

# Set up the figure with a 3x3 grid to display images and histograms
plt.figure(figsize=(15, 5))

# Display the source image and its histogram
plt.subplot(3, 3, 1)
plt.imshow(image_source, cmap='gray')
plt.title('Source Image')
plt.axis('off')

plt.subplot(3, 3, 2)
plt.hist(image_source.ravel(), bins=256, range=[0, 256], color='black')
plt.title('Histogram (Source)')

# Display the target image and its histogram
plt.subplot(3, 3, 4)
plt.imshow(image_target, cmap='gray')
plt.title('Target Image')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.hist(image_target.ravel(), bins=256, range=[0, 256], color='black')
plt.title('Histogram (Target)')

# Display the matched image and its histogram
plt.subplot(3, 3, 7)
plt.imshow(matched_image, cmap='gray')
plt.title('Matched Image')
plt.axis('off')

plt.subplot(3, 3, 8)
plt.hist(matched_image.ravel(), bins=256, range=[0, 256], color='black')
plt.title('Histogram (Matched)')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
