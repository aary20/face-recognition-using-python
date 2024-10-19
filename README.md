Face Recognition using Python
This project implements a simple and efficient face recognition system using Python. The system is capable of detecting and recognizing faces from images or real-time video streams. It leverages modern libraries such as OpenCV for image processing and face_recognition for face detection and recognition.

Features
Face Detection: Detects faces in images or video streams in real-time using OpenCV.
Face Recognition: Matches detected faces with known faces from a pre-trained database.
Face Encoding: Converts facial features into a numerical vector for efficient comparison.
Real-time Performance: Processes live video feed and recognizes faces in real-time.
Scalable: Easily add or remove people from the face database.
High Accuracy: Utilizes the dlib library's highly accurate face recognition models.
Prerequisites
Python 3.x
OpenCV
dlib
face_recognition (uses dlib under the hood)
NumPy
Installation
Clone this repository:
bash
Copy code
git clone https://github.com/your-username/face-recognition-python.git
Install required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Running the project
To recognize faces from an image:

bash
Copy code
python recognize_faces.py --image <path_to_image>
For real-time face recognition using a webcam:

bash
Copy code
python recognize_faces.py --webcam
Adding New Faces
Place the images of new faces in the known_faces/ directory.
Run the encoding script to add new faces to the database:
bash
Copy code
python encode_faces.py
Project Structure
bash
Copy code
- known_faces/       # Directory containing images of known individuals
- face_encodings/    # Stored encodings of known faces
- recognize_faces.py # Main script for face recognition
- encode_faces.py    # Script for encoding known faces
- requirements.txt   # List of dependencies
Acknowledgements
face_recognition
OpenCV
dlib
