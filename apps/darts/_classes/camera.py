import cv2
import time

def record_video(video_length, filename):
    # Open a connection to the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Get the width and height of the camera feed
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change codec if needed
    out = cv2.VideoWriter(filename + '.avi', fourcc, 20.0, (frame_width, frame_height))

    # Record video for the specified length
    start_time = time.time()
    print("Recording video...")
    
    while (time.time() - start_time) < video_length:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Write the frame to the video file
        out.write(frame)

        # Display the frame (optional)
        cv2.imshow('Recording', frame)
        
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Finished recording.")

    # Release the video writer and camera
    out.release()
    cap.release()

    # Close any OpenCV windows
    cv2.destroyAllWindows()

def take_image(filename):
    # Open a connection to the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Take a picture
    ret, frame = cap.read()
    if ret:
        image_filename = filename + '.jpg'
        cv2.imwrite(image_filename, frame)
        print(f"Image saved as: {image_filename}")
    else:
        print("Error: Could not capture image.")

    # Release the camera
    cap.release()

# Usage
while True:
    take_image(filename=f'/home/toor/Documents/GitHub/Programming-Project/apps/darts/images/{time.datetime()}')
    time.sleep(5)

