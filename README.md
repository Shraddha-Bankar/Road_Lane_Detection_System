# 📌 Road Lane Detection System

## Author
Shraddha Bankar  

## Affiliation
Computer Science Engineering (Data Science)  

## Date
March 2026  

---

## 📖 Abstract  
This project presents a Road Lane Detection System designed to identify lane markings on roads using computer vision techniques. Lane detection plays a crucial role in advanced driver assistance systems (ADAS) and autonomous vehicles by ensuring safe navigation and reducing accidents.  

The system processes input images or video frames, applies image preprocessing techniques such as grayscale conversion, edge detection, and region masking, and then detects lane lines using algorithms like Hough Transform. The detected lanes are highlighted on the original image for clear visualization.  

The results show that the system can accurately detect lane boundaries under normal road conditions. This project demonstrates how computer vision can be effectively used in real-time applications for improving road safety and assisting drivers.  

---

## 📘 Introduction  
Road safety is a major concern due to the increasing number of vehicles and accidents. One of the key challenges in driving is maintaining the correct lane, especially in highways and crowded areas.  

The objective of this project is to develop a system that can automatically detect road lanes from images or video streams. The system helps drivers stay within their lane and can also be used in autonomous driving systems.  

This project is important because it contributes to safer driving by providing real-time lane detection and reducing the chances of accidents caused by lane deviation.  

---

## 📚 Literature Review   
Lane detection has been widely studied in the field of computer vision. Traditional methods use edge detection techniques like Canny Edge Detection and Hough Transform for line detection.  

Recent approaches use deep learning models such as Convolutional Neural Networks (CNNs) for more accurate lane detection under complex conditions.  

However, traditional methods are still widely used due to their simplicity and efficiency. This project uses classical computer vision techniques to build a reliable and easy-to-implement lane detection system.  

---

## ⚙️ Methodology  
The system takes input images or video frames and processes them step by step. First, the image is converted to grayscale to simplify processing. Then, noise is reduced using Gaussian blur. Edge detection is applied using the Canny algorithm to identify important edges.  

A region of interest is selected to focus only on the road area. After that, the Hough Transform is used to detect straight lines representing lane boundaries. Finally, the detected lane lines are drawn on the original image for visualization.  

---

## 💻 Implementation  

**Programming Language**  
- Python  

**Frameworks / Libraries**  
- OpenCV  
- NumPy  
- Matplotlib  

**Tools Used**  
- Jupyter Notebook  
- VS Code  
- Google Colab  
- GitHub  

---

## 📊 Results and Discussion  
The system successfully detects lane lines in road images and video streams under normal conditions.  

It performs well on clear roads with visible lane markings. The output shows highlighted lane lines over the original image, making it easier for drivers to understand lane positions.  

However, performance may decrease in challenging conditions such as poor lighting, shadows, or unclear lane markings.  

---

## ⚠️ Limitation  
- Performance decreases in low-light or rainy conditions  
- Difficulty in detecting faded or unclear lane markings  
- Cannot handle curved lanes effectively in all cases  
- Not suitable for highly complex road environments  

---

## 🚀 Future Scope  
- Use deep learning models for better accuracy  
- Improve detection in night and bad weather conditions  
- Detect curved lanes more effectively  
- Integrate with real-time driving systems  
- Combine with object detection for advanced safety systems  

---

## ✅ Conclusion  
This project demonstrates how computer vision techniques can be used to detect road lanes effectively.  

The system provides a simple and efficient solution for lane detection, which can be useful in driver assistance systems. With further improvements, it can be applied in real-world autonomous driving applications.  

---

## 📎 References  
[1] "Lane Detection Using Computer Vision," Journal, 2020  
[2] "Advanced Driver Assistance Systems," 2019  
[3] https://opencv.org/  
[4] https://www.kaggle.com/  
