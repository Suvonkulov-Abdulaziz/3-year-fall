import cv2
import numpy as np
import matplotlib.pyplot as plt

def edge_sobel(image, threshold):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    rows, cols = image.shape
    edge_image = np.zeros_like(image, dtype=np.float32)

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            region = image[i-1:i+2, j-1:j+2]
            gradient_x = np.sum(region * sobel_x)
            gradient_y = np.sum(region * sobel_y)
            magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
            edge_image[i, j] = magnitude

    edge_image = np.where(edge_image > threshold, 255, 0)
    return edge_image.astype(np.uint8)

image = cv2.imread('img-34.jpg', cv2.IMREAD_GRAYSCALE)


threshold_value = 100
edge_image = edge_sobel(image, threshold_value)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f"Sobel Edge Detection (Threshold = {threshold_value})")
plt.imshow(edge_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
