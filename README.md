# 🖼 Computer Vision Basics – OpenCV

## 📌 Overview
This project demonstrates fundamental Computer Vision techniques using OpenCV.

Topics covered:
- Image representation in Machine Learning
- Image transformations
- Blurring & filtering
- Edge detection (Canny)
- Face detection (Haar Cascade)

---

## 📷 What is an Image in ML?

An image is a NumPy array of shape:

(height, width, channels)

Example:
(414, 736, 3)

Each pixel stores intensity values between 0–255.

---

## 🔍 Edge Detection

Canny edge detection identifies boundaries in an image by detecting strong intensity gradients.

Pipeline:
1. Convert to grayscale
2. Apply Gaussian blur
3. Apply Canny edge detector

---

## 👤 Face Detection

Uses Haar Cascade (pre-trained classical model).

The model detects faces by identifying intensity patterns similar to facial structures.

---

## ▶ How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run edge detection:

python edge_detection.py

3. Run face detection:

python face_detection.py

---

## 📦 Requirements

- opencv-python
- matplotlib
- numpy