
Here's an English version of the README, along with additional details on the SSD (Single Shot Multibox Detector) model architecture:

# Real-Time Face Detection using DNN Model
This project demonstrates a simple real-time face detection program using a Deep Neural Network (DNN) model with OpenCV. The program utilizes the camera to detect faces in a video stream and draws a rectangle around them.

## Prerequisites
OpenCV version 3.4 or later
Python 3.6 or later

## Setup
Installing OpenCV
To run this project, you need to install the OpenCV library. You can install it with the following command:
"pip install opencv-python"

## Downloading the Model Files
To run the program, download the following files:

[deploy.prototxt](https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt): Defines the architecture of the neural network model.
[Res10_300x300_ssd_iter_140000.caffemodel](https://github.com/keyurr2/face-detection/blob/master/res10_300x300_ssd_iter_140000.caffemodel): Contains the pre-trained weights for the SSD model.

## Code Explanation
The code consists of the following steps:

1. Loading the DNN Model: The DNN model is loaded from the deploy.prototxt and caffemodel files.
2. Real-Time Face Detection: The program accesses the camera to capture video frames in real time.
3. Processing Frames: Each frame is resized to (300, 300) and then transformed into a blob, which prepares it as input for the neural network.
4. Detecting and Drawing Bounding Boxes: If the model’s confidence in a detection is above the set threshold (e.g., 0.5), it calculates the coordinates of the detected face and draws a bounding box.
5. Displaying Output and Exiting the Program: The processed frame is displayed, and you can exit the program by pressing q.

# Comparison with the Haar Cascade Model
This project uses a DNN model for face detection, which generally offers higher accuracy and performance than the Haar Cascade model.

### Haar Cascade Model
. The Haar Cascade model is a traditional face detection method that uses Haar-like features. It’s based on pre-trained XML files and operates quickly.
. However, it is less accurate than DNNs, particularly in cases of varying lighting or angles.

### DNN (Deep Neural Network) Model with SSD (Single Shot Multibox Detector)
. The DNN model here uses the SSD (Single Shot Multibox Detector) architecture, which significantly improves accuracy.
. It is more robust to different lighting and angles, making it more effective for real-time face detection in diverse environments.

# About SSD Architecture
The SSD (Single Shot Multibox Detector) is a modern convolutional neural network architecture designed for real-time object detection tasks. Here’s a breakdown of its key features:

1. Single-Shot Detection: Unlike traditional methods that perform object localization and classification in multiple stages, SSD performs these tasks in a single pass. This results in much faster processing speeds, making it suitable for real-time applications.

2. Multi-Scale Feature Maps: SSD uses multiple layers within the network to detect objects of varying sizes. Earlier layers capture finer details for small objects, while deeper layers detect larger objects. This approach enables SSD to handle a variety of object sizes effectively.

3. Anchor Boxes: At each location on the feature maps, SSD uses pre-defined anchor boxes with different aspect ratios. The model adjusts these boxes to fit detected objects more accurately, which improves localization without additional computational cost.

4. Efficiency: By combining single-shot detection with the use of anchor boxes and multi-scale feature maps, SSD achieves a balance between accuracy and speed, which is ideal for real-time face detection.

## Usage
Once the prerequisites are installed and the model files are downloaded, run the code. This program will open your device’s camera and detect faces in real time.
To exit the program, press q.

**[Face detection using the Haar Cascade algorithm](https://github.com/NasrinAlaei/FaceDetection_HeerCascade_)**