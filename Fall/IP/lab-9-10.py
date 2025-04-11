import cv2
import numpy as np
import matplotlib.pyplot as plt


def add_salt_pepper_noise(image, salt_prob=0.1, pepper_prob=0.1):
    noisy_image = image.copy()
    num_salt = int(salt_prob * image.size)
    num_pepper = int(pepper_prob * image.size)

    # Salt noise (white pixels)
    coords_salt = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[coords_salt[0], coords_salt[1]] = 255

    # Pepper noise (black pixels)
    coords_pepper = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[coords_pepper[0], coords_pepper[1]] = 0

    return noisy_image


def apply_min_filter(image, kernel_size=5):
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='edge')
    filtered_image = np.zeros_like(image)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_image[i:i + kernel_size, j:j + kernel_size]
            filtered_image[i, j] = np.min(window)

    return filtered_image


def apply_contraharmonic_mean_filter(image, kernel_size=5, Q=-2):
    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='edge').astype(float)
    filtered_image = np.zeros_like(image, dtype=float)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_image[i:i + kernel_size, j:j + kernel_size]
            numerator = np.sum(np.power(window, Q + 1))
            denominator = np.sum(np.power(window, Q))
            filtered_image[i, j] = numerator / (denominator + 1e-5)  # avoid division by zero

    return np.clip(filtered_image, 0, 255).astype(image.dtype)


def apply_harmonic_mean_filter(image, kernel_size=5):

    pad_size = kernel_size // 2
    padded_image = np.pad(image, pad_size, mode='edge').astype(float)
    filtered_image = np.zeros_like(image, dtype=float)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            window = padded_image[i:i + kernel_size, j:j + kernel_size]
            harmonic_mean = kernel_size ** 2 / (np.sum(1.0 / (window + 1e-5)))
            filtered_image[i, j] = harmonic_mean

    return np.clip(filtered_image, 0, 255).astype(image.dtype)


def plot_image_comparison(original, filtered, title, title2):

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original, cmap='gray')
    axes[0].set_title(title)
    axes[0].axis('off')

    axes[1].imshow(filtered, cmap='gray')
    axes[1].set_title(title2)
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()


image = cv2.imread('img-34.jpg', cv2.IMREAD_GRAYSCALE)

noisy_image = add_salt_pepper_noise(image, salt_prob=0, pepper_prob=0.2)
plot_image_comparison(image, noisy_image, "Original","Pepper Noise (p=0.2)")

min_filtered_image = apply_min_filter(noisy_image, kernel_size=5)
plot_image_comparison(noisy_image, min_filtered_image, "Pepper Noise (p=0.2)","5x5 Min Filter")

contraharmonic_filtered_image = apply_contraharmonic_mean_filter(noisy_image, kernel_size=5, Q=-2)
plot_image_comparison(noisy_image, contraharmonic_filtered_image, "Pepper Noise (p=0.2)","5x5 Contraharmonic Mean Filter (Q=-2)")

harmonic_filtered_image = apply_harmonic_mean_filter(noisy_image, kernel_size=5)
plot_image_comparison(noisy_image, harmonic_filtered_image, "Pepper Noise (p=0.2)","5x5 Harmonic Mean Filter")
