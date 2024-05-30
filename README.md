# Model Training Directory

## Purpose
This directory is dedicated to the training of an object detection model specifically designed for identifying individual components on printed circuit boards (PCBs) and reading the text on them. The model used for object detection is Faster R-CNN, while the text recognition is handled by LLAVA1.6, a visual language model. Both tasks are optimized for GPU implementation to ensure efficient training and inference.

## End-to-End Product Overview

### 1. Model Training and Evaluation
- **Notebook**: `pcb_component_recognition_train.ipynb`
- **Description**: This notebook handles both training and evaluation of the Faster R-CNN model. It uses helper functions from `utils.ipynb` and saves the best model parameters to `best_model_final`.

### 2. Model Inference and Full Pipeline
- **Notebook**: `client.ipynb`
- **Description**: This notebook demonstrates the full process. It takes a PCB image as input, uses the trained Faster R-CNN model to detect components, and then uses the LLAVA1.6 model to predict the labels.

### 3. Helper Functions
- **Notebook**: `utils.ipynb`
- **Description**: Contains various helper functions used in 'pcb_component_recognition_train.ipynb'

### 4. Dataset
- **Folder**:`PCB`
- **Description**: Contains the PCB Images used in training and testing.


### Usage Instructions
To run the notebooks and scripts, follow these steps:
1. **Model Training and Evaluation**: Open and run `pcb_component_recognition_train.ipynb`
2. **Model Inference and Full Pipeline**: Open and run `client.ipynb`
