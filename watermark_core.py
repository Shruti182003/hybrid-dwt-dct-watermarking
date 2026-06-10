import cv2
import numpy as np
import pywt
from scipy.fftpack import dct, idct


# =====================================================
# Utility Functions
# =====================================================

def make_even(img):
    """
    Ensure image dimensions are even
    required by DWT
    """
    h, w = img.shape

    if h % 2 != 0:
        img = img[:-1, :]

    if w % 2 != 0:
        img = img[:, :-1]

    return img


def apply_dct(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')


def apply_idct(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')


# =====================================================
# Watermark Preparation
# =====================================================

def prepare_watermark(watermark, target_shape):

    wm = cv2.resize(
        watermark,
        target_shape,
        interpolation=cv2.INTER_AREA
    )

    wm = np.where(wm > 127, 1, -1)

    return wm


# =====================================================
# Embed in One Band
# =====================================================

def embed_band(
        band,
        watermark_bits,
        strength):

    block_size = 8

    rows, cols = band.shape

    wm_rows, wm_cols = watermark_bits.shape

    embedded_band = band.copy()

    for i in range(wm_rows):

        for j in range(wm_cols):

            r = i * block_size
            c = j * block_size

            if r + 8 > rows or c + 8 > cols:
                continue

            block = embedded_band[
                r:r + 8,
                c:c + 8
            ]

            dct_block = apply_dct(block)

            bit = watermark_bits[i, j]

            # Multiple coefficient embedding
            dct_block[3, 3] += strength * bit
            dct_block[4, 4] += strength * bit
            dct_block[5, 5] += strength * bit

            embedded_band[
                r:r + 8,
                c:c + 8
            ] = apply_idct(dct_block)

    return embedded_band


# =====================================================
# Extract From One Band
# =====================================================

def extract_band(
        original_band,
        watermarked_band,
        wm_shape):

    block_size = 8

    rows, cols = original_band.shape

    wm_rows, wm_cols = wm_shape

    extracted = np.zeros(
        (wm_rows, wm_cols),
        dtype=np.int8
    )

    for i in range(wm_rows):

        for j in range(wm_cols):

            r = i * block_size
            c = j * block_size

            if r + 8 > rows or c + 8 > cols:
                continue

            orig_block = original_band[
                r:r + 8,
                c:c + 8
            ]

            wm_block = watermarked_band[
                r:r + 8,
                c:c + 8
            ]

            dct_orig = apply_dct(orig_block)
            dct_wm = apply_dct(wm_block)

            vote = 0

            vote += np.sign(
                dct_wm[3, 3] - dct_orig[3, 3]
            )

            vote += np.sign(
                dct_wm[4, 4] - dct_orig[4, 4]
            )

            vote += np.sign(
                dct_wm[5, 5] - dct_orig[5, 5]
            )

            extracted[i, j] = 1 if vote >= 0 else -1

    return extracted


# =====================================================
# Hybrid DWT-DCT Embed
# =====================================================

def embed_watermark(
        image,
        watermark,
        alpha=5,
        beta=5):

    image = make_even(image)

    coeffs = pywt.dwt2(
        image,
        'haar'
    )

    LL, (LH, HL, HH) = coeffs

    wm_shape = (
        LL.shape[0] // 8,
        LL.shape[1] // 8
    )

    wm_bits = prepare_watermark(
        watermark,
        (wm_shape[1], wm_shape[0])
    )

    # Multi-band embedding

    LL_emb = embed_band(
        LL,
        wm_bits,
        alpha * 0.5
    )

    LH_emb = embed_band(
        LH,
        wm_bits,
        alpha
    )

    HL_emb = embed_band(
        HL,
        wm_bits,
        beta
    )

    watermarked = pywt.idwt2(
        (
            LL_emb,
            (
                LH_emb,
                HL_emb,
                HH
            )
        ),
        'haar'
    )

    watermarked = np.clip(
        watermarked,
        0,
        255
    )

    return watermarked.astype(
        np.uint8
    )


# =====================================================
# Hybrid DWT-DCT Extraction
# =====================================================

def extract_watermark(
        original_image,
        watermarked_image,
        watermark_size):

    original_image = make_even(
        original_image
    )

    watermarked_image = make_even(
        watermarked_image
    )

    coeff_orig = pywt.dwt2(
        original_image,
        'haar'
    )

    coeff_wm = pywt.dwt2(
        watermarked_image,
        'haar'
    )

    LL_o, (LH_o, HL_o, HH_o) = coeff_orig
    LL_w, (LH_w, HL_w, HH_w) = coeff_wm

    wm_shape = (
        LL_o.shape[0] // 8,
        LL_o.shape[1] // 8
    )

    LL_bits = extract_band(
        LL_o,
        LL_w,
        wm_shape
    )

    LH_bits = extract_band(
        LH_o,
        LH_w,
        wm_shape
    )

    HL_bits = extract_band(
        HL_o,
        HL_w,
        wm_shape
    )

    # Majority Voting

    combined = (
        LL_bits +
        LH_bits +
        HL_bits
    )

    combined = np.where(
        combined >= 0,
        255,
        0
    ).astype(np.uint8)

    extracted = cv2.resize(
        combined,
        watermark_size,
        interpolation=cv2.INTER_NEAREST
    )

    return extracted