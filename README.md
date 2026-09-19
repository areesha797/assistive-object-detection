# Assistive Object Detection System

A computer vision prototype designed to detect objects in images and provide basic assistive scene information through spatial positioning and text-to-speech feedback.

## Overview

The Assistive Object Detection System uses a pretrained YOLO model to identify objects in an uploaded image. For each detected object, the system estimates whether it is positioned on the left, center, or right side of the image.

The detected information is then converted into a simple scene description that can be read aloud using text-to-speech.

This project was developed as a research-oriented prototype exploring computer vision and assistive interaction.

## Features

- Object detection using a pretrained YOLO model
- Confidence scores for detected objects
- Approximate left, center, and right spatial positioning
- Automatic scene description generation
- Text-to-speech feedback
- Interactive Streamlit interface
- Image-based computer vision processing

## Technology Stack

- Python
- YOLO
- Ultralytics
- OpenCV
- Streamlit
- Pillow
- pyttsx3

## System Workflow

```text
Upload Image
      |
      v
YOLO Object Detection
      |
      v
Detected Objects
      |
      v
Spatial Position Estimation
(Left / Center / Right)
      |
      v
Scene Description
      |
      v
Text-to-Speech Feedback