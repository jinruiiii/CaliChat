# PCB Object Detection

## Description
This project is an application designed to process PCB (Printed Circuit Board) images. By uploading PCB images to the application, the application can detect individual components and read text labels such as "R1" and "R2" on the PCB. The application is user-friendly and leverages advanced machine learning and OCR (Optical Character Recognition) techniques to provide results.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
### Prerequisites
- Ensure you have the following dependencies.
  1. PyTorch
  2. Flask
  3. Pytesseract
  4. PIL
  5. Regex

### Steps
1. Clone the repository:
   ```sh
   git clone https://gitlab.ai-stack.dso/fjinrui/pcb.git

2. You can start the application by running the command below in the root directory of this project.
   ```sh
   python app.py
## Usage
1. Upload an image of a PCB by clicking "Select Image".
2. Click "Annotate Now" to get the results. 
