"""
metrics.py

Evaluation metrics for
Hybrid DWT-DCT Watermarking
"""

import numpy as np

from skimage.metrics import (
    structural_similarity as ssim
)

from sklearn.metrics import (
    mean_squared_error
)


# =====================================================
# MSE
# =====================================================

def compute_mse(
        original,
        processed):

    original = original.astype(
        np.float64
    )

    processed = processed.astype(
        np.float64
    )

    mse = np.mean(
        (
            original -
            processed
        ) ** 2
    )

    return mse


# =====================================================
# PSNR
# =====================================================

def compute_psnr(
        original,
        processed):

    mse = compute_mse(
        original,
        processed
    )

    if mse == 0:
        return 100

    max_pixel = 255.0

    psnr = (
        20 *
        np.log10(
            max_pixel /
            np.sqrt(mse)
        )
    )

    return psnr


# =====================================================
# SSIM
# =====================================================

def compute_ssim(
        original,
        processed):

    score = ssim(
        original,
        processed,
        data_range=255
    )

    return score


# =====================================================
# Normalized Correlation
# =====================================================

def compute_nc(
        original_wm,
        extracted_wm):

    original = original_wm.astype(
        np.float64
    ).flatten()

    extracted = extracted_wm.astype(
        np.float64
    ).flatten()

    numerator = np.sum(
        original * extracted
    )

    denominator = (
        np.sqrt(
            np.sum(
                original ** 2
            )
        )
        *
        np.sqrt(
            np.sum(
                extracted ** 2
            )
        )
    )

    if denominator == 0:
        return 0

    nc = numerator / denominator

    return nc


# =====================================================
# Bit Error Rate
# =====================================================

def compute_ber(
        original_wm,
        extracted_wm):

    original = (
        original_wm > 127
    ).astype(np.uint8)

    extracted = (
        extracted_wm > 127
    ).astype(np.uint8)

    total_bits = (
        original.shape[0] *
        original.shape[1]
    )

    errors = np.sum(
        original != extracted
    )

    ber = errors / total_bits

    return ber


# =====================================================
# Watermark Accuracy
# =====================================================

def watermark_accuracy(
        original_wm,
        extracted_wm):

    original = (
        original_wm > 127
    ).astype(np.uint8)

    extracted = (
        extracted_wm > 127
    ).astype(np.uint8)

    correct = np.sum(
        original == extracted
    )

    total = original.size

    accuracy = (
        correct /
        total
    ) * 100

    return accuracy


# =====================================================
# Combined Evaluation
# =====================================================

def evaluate_watermarking(
        original_image,
        watermarked_image,
        original_wm,
        extracted_wm):

    results = {

        "PSNR":
            compute_psnr(
                original_image,
                watermarked_image
            ),

        "SSIM":
            compute_ssim(
                original_image,
                watermarked_image
            ),

        "NC":
            compute_nc(
                original_wm,
                extracted_wm
            ),

        "BER":
            compute_ber(
                original_wm,
                extracted_wm
            ),

        "Accuracy":
            watermark_accuracy(
                original_wm,
                extracted_wm
            )
    }

    return results


# =====================================================
# Pretty Print
# =====================================================

def print_metrics(
        metrics_dict):

    print(
        "\\n========== RESULTS =========="
    )

    for key, value in (
            metrics_dict.items()):

        print(
            f"{key}: {value:.4f}"
        )

    print(
        "=============================\\n"
    )