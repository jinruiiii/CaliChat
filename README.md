# PCB Component Recognition Project

## Overview
This project contains two implementations aimed at solving the same problem: identifying individual components on PCB images and extracting the text labels. 

## Implementations

### 1. PCB GPU
The `PCB GPU` folder contains scripts and resources for training and running the object detection model using a GPU. This implementation includes:
- **Object Detection**: Training scripts to train a Faster R-CNN model for detecting components on PCB images.
- **Text Recognition**: Using LLAVA1.6, a visual language model that requires a GPU, to identify the text labels on the PCB.

### 2. PCB CPU
The `PCB CPU` folder leverages the trained model from the `PCB GPU` implementation but uses CPU-based text recognition. This implementation includes:
- **Object Detection**: Using the pre-trained Faster R-CNN model from the `PCB GPU` folder.
- **Text Recognition**: Using PyTesseract to identify the text labels on the PCB.

### Usage Instructions
Follow the instructions in the respective README files within each folder (`PCB_GPU` and `PCB_CPU`) for detailed setup and usage.
