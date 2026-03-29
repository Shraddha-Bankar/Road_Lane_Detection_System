# 📌 Road Lane Detection System  

## Author  
Shraddha Bankar  

## Affiliation  
Computer Science Engineering (Data Science)  

## Date  
March 2026  

---

## 📖 Abstract  
This project focuses on detecting road lanes using computer vision techniques. It takes images or video as input and identifies lane lines to help in safe driving.  

Basic image processing methods like edge detection and Hough Transform are used to highlight lanes. This system can be useful in driver assistance and road safety applications.  

---

## 📘 Introduction  
Road accidents are increasing, and maintaining the correct lane is very important for safe driving.  

The goal of this project is to build a system that can automatically detect lanes from images or videos. It helps drivers stay in their lane and can also be used in self-driving systems.  

---

## 📚 Literature Review  
Lane detection is an important part of computer vision.  

Traditional methods like Canny Edge Detection and Hough Transform are simple and widely used. New methods use deep learning for better accuracy, but this project uses basic techniques for simplicity and efficiency.  

---

## ⚙️ Methodology  
- Convert image to grayscale  
- Apply Gaussian blur to reduce noise  
- Detect edges using Canny  
- Select road region (ROI)  
- Detect lines using Hough Transform  
- Draw lane lines on original image  

---

## 💻 Implementation  

**Language:** Python  

**Libraries:**  
- OpenCV  
- NumPy  
- Matplotlib  

**Tools:**  
- Jupyter Notebook  
- VS Code  
- Google Colab  
- GitHub  

---

## 📊 Results  
The system can detect lane lines clearly in normal road conditions.  

It works well when lane markings are visible, but performance may reduce in low light or unclear roads.  

---

## ⚠️ Limitations  
- Poor performance in low light or rain  
- Difficulty with faded lane markings  
- Limited handling of curved lanes  

---

## 🚀 Future Scope  
- Use deep learning for better accuracy  
- Improve detection in difficult conditions  
- Handle curved lanes better  
- Integrate with real-time systems  

---

## ✅ Conclusion  
This project shows how computer vision can be used for lane detection.  

It is a simple and useful system that can help improve road safety and assist drivers.  

---

## 📎 References  
1. Lane Detection Using Computer Vision (2020)  
2. Advanced Driver Assistance Systems (2019)  
3. https://opencv.org/  
4. https://www.kaggle.com/  
