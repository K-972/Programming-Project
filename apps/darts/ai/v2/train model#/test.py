from ultralytics import YOLO
import cv2
import os

# Configuration
model_path = "runs/detect/train/dart_detection/weights/best.pt"  # Path to the trained YOLO model
image_path = "test_images/dart_test.jpg"  # Path to a test image (update as needed)
video_path = "test_videos/dart_test.mp4"  # Path to a test video (optional)
use_camera = False  # Set to True to use a live camera feed

# Ensure model exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Trained model not found: {model_path}")

# Load the YOLO model
print("Loading YOLO model...")
model = YOLO(model_path)

# Test on an image
def test_image():
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Test image not found: {image_path}")
    
    print("Running inference on image...")
    results = model(image_path)
    results[0].plot(show=True)  # Display the image with predictions

# Test on a video
def test_video():
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Test video not found: {video_path}")
    
    print("Running inference on video...")
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform inference
        results = model(frame)
        annotated_frame = results[0].plot()
        
        # Display the frame
        cv2.imshow("Dart Detection", annotated_frame)
        
        # Quit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Test with a live camera feed
def test_camera():
    print("Starting live camera feed...")
    cap = cv2.VideoCapture(0)  # Replace 0 with your camera index
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform inference
        results = model(frame)
        annotated_frame = results[0].plot()
        
        # Display the frame
        cv2.imshow("Dart Detection", annotated_frame)
        
        # Quit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Choose the test method
if __name__ == "__main__":
    if use_camera:
        test_camera()
    elif os.path.exists(image_path):
        test_image()
    elif os.path.exists(video_path):
        test_video()
    else:
        print("No valid input found for testing. Please provide an image, video, or enable the camera.")
