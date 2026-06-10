# 🔐 Hybrid DWT-DCT Watermarking System with NSGA-II Optimization

## 🌐 Live Demo

🚀 **Streamlit Application**

https://hybrid-dwt-dct-watermarking-2gdzlqek2qqfsvmkzmpds7.streamlit.app/

---

## 📌 Project Overview

This project presents a robust digital image watermarking framework based on a hybrid **Discrete Wavelet Transform (DWT)** and **Discrete Cosine Transform (DCT)** architecture.

The system embeds an invisible watermark into a host image while maintaining high visual quality and robustness against image processing attacks.

To further enhance performance, **NSGA-II Multi-Objective Optimization** is used to determine optimal embedding parameters.

The project is deployed as an interactive Streamlit web application for real-time watermark embedding, extraction, optimization, and analysis.

---

## 🎯 Objectives

- Protect digital image ownership
- Embed invisible watermarks securely
- Improve robustness against attacks
- Optimize embedding parameters using NSGA-II
- Provide an interactive web-based platform

---

## ✨ Features

### 🔹 Watermark Embedding

- Hybrid DWT-DCT watermarking
- Adjustable embedding strength
- Invisible watermark insertion
- Real-time image processing

### 🔹 Watermark Extraction

- Recover embedded watermark
- Visual comparison with original watermark

### 🔹 Performance Evaluation

- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)
- NC (Normalized Correlation)
- BER (Bit Error Rate)

### 🔹 Attack Robustness Analysis

Supported attacks include:

- Gaussian Noise
- Salt & Pepper Noise
- JPEG Compression
- Gaussian Blur
- Image Resizing
- Rotation
- Cropping
- Brightness Adjustment
- Contrast Modification

### 🔹 NSGA-II Optimization

Multi-objective optimization for:

- Maximizing PSNR
- Maximizing SSIM
- Maximizing NC
- Minimizing BER

### 🔹 Research Visualizations

- Pareto Front Analysis
- Parameter Optimization Graphs
- Robustness Analysis Charts
- Baseline Comparison Graphs

### 🔹 Automated Report Generation

Generate project reports directly from the dashboard.

---

## 🏗️ System Architecture

```text
Host Image
      │
      ▼
      DWT
      │
      ▼
      DCT
      │
      ▼
Watermark Embedding
      │
      ▼
Watermarked Image
      │
      ▼
Attack Simulation
      │
      ▼
Watermark Extraction
      │
      ▼
Performance Evaluation
```

---

## 📂 Project Structure

```text
hybrid-dwt-dct-watermarking/

├── app.py
├── watermark_core.py
├── metrics.py
├── attacks.py
├── optimization.py
├── visualization.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries & Frameworks

- Streamlit
- OpenCV
- NumPy
- SciPy
- PyWavelets
- Matplotlib
- Pandas
- Scikit-Image
- Pymoo
- Pillow

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/hybrid-dwt-dct-watermarking.git

cd hybrid-dwt-dct-watermarking
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🚀 Deployment

This application is deployed on Streamlit Community Cloud.

### Live Link

https://hybrid-dwt-dct-watermarking-2gdzlqek2qqfsvmkzmpds7.streamlit.app/

---

## 📊 Evaluation Metrics

### PSNR

Measures image quality after watermark embedding.

Higher values indicate better imperceptibility.

### SSIM

Measures structural similarity between images.

Values closer to 1 indicate better similarity.

### NC

Measures watermark extraction accuracy.

Values closer to 1 indicate successful recovery.

### BER

Measures watermark bit extraction errors.

Lower values indicate better performance.

---

## 🔬 Experimental Workflow

1. Upload Host Image
2. Upload Watermark Image
3. Select Embedding Parameters
4. Embed Watermark
5. Extract Watermark
6. Evaluate Metrics
7. Run NSGA-II Optimization
8. Perform Attack Analysis
9. Generate Research Report

---

## 📈 Future Enhancements

- DWT-DCT-SVD Watermarking
- Blind Watermark Extraction
- Color Image Watermarking
- QR-Code Based Watermarks
- Deep Learning Watermarking
- Medical Image Security
- Video Watermarking
- Blockchain-Based Copyright Protection

---

## 🎓 Academic Significance

This project demonstrates:

- Digital Image Processing
- Information Security
- Optimization Algorithms
- Signal Processing
- Research-Oriented Software Development

The system can be used for:

- Copyright Protection
- Digital Rights Management
- Content Authentication
- Secure Multimedia Distribution

---

## 👩‍💻 Author

**Shruti Shreya**

B.Tech – Computer Science & Engineering

Dr. B.C. Roy Engineering College, Durgapur

---

## 📜 License

This project is developed for academic and research purposes.

Feel free to use and extend it with proper attribution.

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🔗 Share the project

🚀 Try the live Streamlit demo
