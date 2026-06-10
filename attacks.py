"""
attacks.py

Robustness testing attacks
for Hybrid DWT-DCT Watermarking
"""

import cv2
import numpy as np


# =====================================================
# Gaussian Noise Attack
# =====================================================

def gaussian_noise_attack(
        image,
        mean=0,
        sigma=10):

    image = image.astype(
        np.float32
    )

    noise = np.random.normal(
        mean,
        sigma,
        image.shape
    )

    attacked = image + noise

    attacked = np.clip(
        attacked,
        0,
        255
    )

    return attacked.astype(
        np.uint8
    )


# =====================================================
# Salt and Pepper Noise
# =====================================================

def salt_pepper_attack(
        image,
        amount=0.01):

    attacked = image.copy()

    num_salt = int(
        amount *
        image.size *
        0.5
    )

    num_pepper = int(
        amount *
        image.size *
        0.5
    )

    # Salt

    coords = [
        np.random.randint(
            0,
            i - 1,
            num_salt
        )
        for i in image.shape
    ]

    attacked[
        coords[0],
        coords[1]
    ] = 255

    # Pepper

    coords = [
        np.random.randint(
            0,
            i - 1,
            num_pepper
        )
        for i in image.shape
    ]

    attacked[
        coords[0],
        coords[1]
    ] = 0

    return attacked


# =====================================================
# JPEG Compression Attack
# =====================================================

def jpeg_attack(
        image,
        quality=50):

    encode_param = [
        int(
            cv2.IMWRITE_JPEG_QUALITY
        ),
        quality
    ]

    result, encimg = cv2.imencode(
        '.jpg',
        image,
        encode_param
    )

    if not result:
        return image

    decimg = cv2.imdecode(
        encimg,
        0
    )

    return decimg


# =====================================================
# Blur Attack
# =====================================================

def blur_attack(
        image,
        kernel_size=5):

    attacked = cv2.GaussianBlur(
        image,
        (
            kernel_size,
            kernel_size
        ),
        0
    )

    return attacked


# =====================================================
# Median Blur Attack
# =====================================================

def median_blur_attack(
        image,
        kernel_size=5):

    return cv2.medianBlur(
        image,
        kernel_size
    )


# =====================================================
# Resize Attack
# =====================================================

def resize_attack(
        image,
        scale=0.5):

    h, w = image.shape

    resized = cv2.resize(
        image,
        (
            int(w * scale),
            int(h * scale)
        )
    )

    restored = cv2.resize(
        resized,
        (
            w,
            h
        )
    )

    return restored


# =====================================================
# Rotation Attack
# =====================================================

def rotation_attack(
        image,
        angle=5):

    h, w = image.shape

    center = (
        w // 2,
        h // 2
    )

    matrix = cv2.getRotationMatrix2D(
        center,
        angle,
        1.0
    )

    rotated = cv2.warpAffine(
        image,
        matrix,
        (
            w,
            h
        )
    )

    return rotated


# =====================================================
# Cropping Attack
# =====================================================

def crop_attack(
        image,
        crop_percent=0.1):

    h, w = image.shape

    crop_h = int(
        h * crop_percent
    )

    crop_w = int(
        w * crop_percent
    )

    cropped = image[
        crop_h:h - crop_h,
        crop_w:w - crop_w
    ]

    restored = cv2.resize(
        cropped,
        (
            w,
            h
        )
    )

    return restored


# =====================================================
# Histogram Equalization Attack
# =====================================================

def histogram_equalization_attack(
        image):

    return cv2.equalizeHist(
        image
    )


# =====================================================
# Contrast Attack
# =====================================================

def contrast_attack(
        image,
        alpha=1.3,
        beta=10):

    attacked = cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=beta
    )

    return attacked


# =====================================================
# Brightness Attack
# =====================================================

def brightness_attack(
        image,
        value=30):

    attacked = cv2.add(
        image,
        value
    )

    return attacked


# =====================================================
# Combined Attack
# =====================================================

def combined_attack(
        image):

    attacked = gaussian_noise_attack(
        image,
        sigma=10
    )

    attacked = jpeg_attack(
        attacked,
        quality=50
    )

    attacked = blur_attack(
        attacked,
        kernel_size=3
    )

    return attacked


# =====================================================
# Attack Dictionary
# =====================================================

def get_attack_suite():

    attacks = {

        "Gaussian Noise":
            lambda x:
            gaussian_noise_attack(
                x,
                sigma=10
            ),

        "Salt & Pepper":
            lambda x:
            salt_pepper_attack(
                x,
                amount=0.01
            ),

        "JPEG Compression":
            lambda x:
            jpeg_attack(
                x,
                quality=50
            ),

        "Gaussian Blur":
            lambda x:
            blur_attack(
                x,
                kernel_size=5
            ),

        "Resize":
            lambda x:
            resize_attack(
                x,
                scale=0.5
            ),

        "Rotation":
            lambda x:
            rotation_attack(
                x,
                angle=5
            ),

        "Cropping":
            lambda x:
            crop_attack(
                x,
                crop_percent=0.1
            ),

        "Histogram Equalization":
            histogram_equalization_attack,

        "Contrast Change":
            contrast_attack,

        "Brightness Change":
            brightness_attack,

        "Combined Attack":
            combined_attack
    }

    return attacks