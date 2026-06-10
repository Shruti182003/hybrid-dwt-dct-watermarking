# Hybrid DWT-DCT Watermarking System with NSGA-II Optimization

## Overview

This project presents a robust digital image watermarking framework based on a Hybrid Discrete Wavelet Transform (DWT) and Discrete Cosine Transform (DCT) approach. The system embeds an invisible watermark into a host image while maintaining high visual quality and robustness against various image processing attacks.

The proposed method employs:

* Hybrid DWT-DCT watermark embedding
* Multi-band embedding (LL, LH, HL)
* Multi-coefficient DCT embedding
* Majority voting extraction
* NSGA-II multi-objective optimization
* Attack robustness analysis
* Baseline comparison with DCT-only and DWT-only approaches
* Streamlit-based interactive dashboard

---

## Features

### Watermark Embedding

* Invisible watermark embedding
* Multi-band DWT decomposition
* DCT coefficient modification
* Adjustable embedding strengths (Alpha and Beta)

### Watermark Extraction

* Watermark recovery from watermarked images
* Majority voting mechanism
* Redundancy-based extraction

### Optimization

* NSGA-II optimization
* Automatic Alpha-Beta parameter tuning
* Pareto Front generation

### Attack Analysis

Supported attacks:

* Gaussian Noise
* Salt & Pepper Noise
* JPEG Compression
* Gaussian Blur
* Resize Attack
* Rotation Attack
* Cropping Attack
* Contrast Adjustment
* Brightness Modification
* Combined Attack

### Evaluation Metrics

* PSNR (Peak Signal-to-Noise Ratio)
* SSIM (Structural Similarity Index)
* NC (Normalized Correlation)
* BER (Bit Error Rate)

### Research Visualizations

* Pareto Front Plot
* PSNR vs Alpha
* SSIM vs Alpha
* NC vs Alpha
* Attack Robustness Graphs
* Baseline Comparison Graphs

---

## Project Structure

```text
watermarking_research_app/

├── app.py
├── watermark_core.py
├── metrics.py
├── attacks.py
├── optimization.py
├── visualization.py
├── requirements.txt
├── README.md
│
├── assets/
├── outputs/
└── results/
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd watermarking_research_app
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Application will launch at:

```text
http://localhost:8501
```

---

## Workflow

### Step 1

Upload Host Image

### Step 2

Upload Watermark Image

### Step 3

Navigate to Watermarking Page

### Step 4

Select Alpha and Beta values

### Step 5

Run Watermark Embedding

### Step 6

Extract Watermark

### Step 7

Evaluate Metrics

### Step 8

Run NSGA-II Optimization

### Step 9

Perform Attack Analysis

### Step 10

Generate Research Report

---

## Methodology

### DWT Decomposition

The host image is decomposed into:

* LL
* LH
* HL
* HH

sub-bands using Haar Wavelet Transform.

### DCT Embedding

DCT is applied to each selected sub-band and watermark bits are embedded into selected mid-frequency coefficients.

### Multi-Band Embedding

Watermark information is redundantly embedded into:

* LL Band
* LH Band
* HL Band

to improve robustness.

### Majority Voting Extraction

During extraction, watermark bits recovered from multiple bands are combined using majority voting to improve reliability.

### NSGA-II Optimization

Embedding parameters are optimized using NSGA-II considering:

* Maximize PSNR
* Maximize SSIM
* Maximize NC
* Minimize BER

---

## Experimental Evaluation

### Image Quality Metrics

* PSNR
* SSIM

### Watermark Robustness Metrics

* NC
* BER

### Attack Resistance Testing

Evaluation is performed under multiple image processing attacks.

---

## Baseline Comparison

The proposed method is compared against:

| Method          | Description                  |
| --------------- | ---------------------------- |
| DCT Only        | Traditional DCT Watermarking |
| DWT Only        | Traditional DWT Watermarking |
| Proposed Hybrid | Hybrid DWT-DCT + NSGA-II     |

---

## Results

Expected outcomes:

* High PSNR (> 40 dB)
* High SSIM (> 0.95)
* High NC (> 0.95)
* Low BER (< 0.05)

The proposed hybrid framework demonstrates superior imperceptibility and robustness compared to conventional watermarking approaches.

---

## Future Scope

* Deep Learning-based Watermarking
* Blind Watermark Extraction
* Medical Image Security
* Video Watermarking
* Blockchain-based Copyright Protection
* Federated Watermarking Systems

---

## Technologies Used

* Python
* Streamlit
* OpenCV
* NumPy
* SciPy
* PyWavelets
* Matplotlib
* Pandas
* Pymoo
* Scikit-Image

---

## Authors

Final Year B.Tech Project

Department of Computer Science and Engineering

Project Title:

**Hybrid DWT-DCT Watermarking System with NSGA-II Optimization for Robust Copyright Protection**

---

## License

This project is intended for academic and research purposes.
