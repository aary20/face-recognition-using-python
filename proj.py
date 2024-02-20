import cv2

# Load pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                    'haarcascade_frontalface_default.xml')

# Load a sample image or use the webcam
# For a sample image
image = cv2.imread('aarya.jpg')

# For using the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
video_capture.release()
video_capture.close()
cv2.destroyAllWindows()