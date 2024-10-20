
# Face Recognition Using Python

This project implements a simple and efficient face recognition system using Python. The system is capable of detecting and recognizing faces from images or real-time video streams. It leverages modern libraries such as OpenCV for image processing and face_recognition for face detection and recognition.



## Features

- Face Detection: Detects faces in images or video streams in real-time using OpenCV.
- Face Recognition: Matches detected faces with known faces from a pre-trained database.
- Real-time Performance: Processes live video feed and recognizes faces in real-time.
- Scalable: Easily add or remove people from the face database.
- High Accuracy: Utilizes the dlib library's highly accurate face recognition models.


## Prerequisites
- Python 3.x
- OpenCV
- dlib
- face_recognition (uses dlib under the hood)
- NumPy

## Installation

1. Clone this repository:

```bash
  git clone https://github.com/aary20/face-recognition-using-python.git

```
2. Install required dependencies:
``` bash
   pip install -r requirements.txt
```
## Usage
 ### Running The Project

 1. To recognize faces from an image:

```bash
   python program.py --image <path_to_image>

```

  2. For real-time face recognition using a webcam:
```bash
    python program.py --webcam
```
 ### Adding new faces
- Place the images of new faces in the ```known_faces```/ directory.
- Run the encoding script to add new faces to the database:
```bash
 python encode_faces.py
```

## Project Structure
```bash
- known_faces/       # Directory containing images of known individuals
- face_encodings/    # Stored encodings of known faces
- recognize_faces.py # Main script for face recognition
- encode_faces.py    # Script for encoding known faces
- requirements.txt   # List of dependencies
```
## Acknowledgements

- [face_recognition](https://pypi.org/project/face-recognition/)  library by Adam Geitgey for providing an easy-to-use and powerful face recognition API.
- [OpenCV](https://opencv.org/) for its extensive library of computer vision functions.
- [dlib](http://dlib.net/) for its robust machine learning models, particularly in face detection and facial landmark detection.
- The open-source community for their helpful tutorials and discussions on face recognition and computer vision.
