# 🚗 Road Lane Detection using OpenCV

## Project Title
**Road Lane Detection using Computer Vision and OpenCV**

**Author:** Shraddha Bankar  
**Affiliation:** Computer Science Engineering (Data Science)  
**Date:** June 2026

---

## Abstract
This project presents a Road Lane Detection system using Python and OpenCV. The system detects lane markings from road images and videos using image processing techniques such as edge detection and Hough Line Transform. The detected lanes are highlighted on the original frame, supporting road safety and autonomous driving applications.

---

## Introduction
Road lane detection is an important component of Advanced Driver Assistance Systems (ADAS). It helps identify lane boundaries and improve vehicle navigation. This project aims to develop a simple and efficient lane detection system using computer vision techniques.

---

## Literature Review
Traditional lane detection methods use image processing techniques like Canny Edge Detection and Hough Transform, while modern systems incorporate deep learning models. This project focuses on the OpenCV-based approach due to its simplicity and real-time performance.

---

## Methodology
The system follows these steps:
1. Input image or video.
2. Convert to grayscale.
3. Apply Gaussian blur.
4. Perform Canny edge detection.
5. Select the region of interest.
6. Detect lane lines using Hough Transform.
7. Overlay detected lanes on the original frame.

---

## Implementation

### Programming Language
- Python

### Libraries
- OpenCV
- NumPy
- Matplotlib

### Tools
- Google Colab
- Jupyter Notebook
- GitHub

---

## Results and Discussion
The system successfully detects road lanes under standard conditions and highlights them accurately. It demonstrates the practical application of computer vision for intelligent transportation systems.

---

## Limitations
- Reduced accuracy in poor lighting.
- Difficulty detecting curved or faded lanes.
- Sensitive to weather and shadows.

---

## Future Scope
- Curved lane detection.
- Deep learning integration.
- Lane departure warning system.
- Real-time autonomous vehicle support.

---

## Conclusion
This project demonstrates a simple and efficient road lane detection system using Python and OpenCV. It provides a strong foundation for understanding computer vision applications in road safety and autonomous driving.

---

## References

1. OpenCV Documentation: https://opencv.org/
2. NumPy Documentation: https://numpy.org/
3. Google Colab: https://colab.research.google.com/
4. J. Canny, *A Computational Approach to Edge Detection*, IEEE, 1986.
5. Duda & Hart, *Use of the Hough Transformation to Detect Lines and Curves*, ACM, 1972.

---

## 📌 Keywords
`Python` `OpenCV` `Computer Vision` `Lane Detection` `Image Processing` `ADAS` `Autonomous Driving`
