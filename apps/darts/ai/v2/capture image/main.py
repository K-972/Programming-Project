import cv2
import os
from datetime import datetime

# Configuration
output_folder = r"D:\photos"  # Folder to save images
camera_index = 0  # Default camera index; change if necessary

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize the camera
cap = cv2.VideoCapture(camera_index)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press SPACE to capture an image. Press 'q' to quit.")

image_count = 0  # Counter for naming images

try:
    while True:
        # Read the frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from the camera.")
            break
        
        # Display the live video feed
        cv2.imshow("Dartboard Camera", frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF
        
        # Capture and save the image on SPACE press
        if key == ord(' '):  # Spacebar
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_name = f"dart_{timestamp}_{image_count:04d}.jpg"
            image_path = os.path.join(output_folder, image_name)
            cv2.imwrite(image_path, frame)
            print(f"Image saved: {image_path}")
            image_count += 1
        
        # Quit the program on 'q' press
        elif key == ord('q'):
            print("Quitting the program.")
            break

finally:
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
