import cv2
import time

def take_images_and_calculate_average(filename_base, interval, num_images):
    # Open a connection to the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    total_time = 0  # Initialize total time variable

    # Capture the specified number of images at the given interval
    for i in range(num_images):
        start_time = time.time()  # Start time for this capture
        
        ret, frame = cap.read()
        if ret:
            # Save the image with an indexed filename
            image_filename = f"{filename_base}_{i+1}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"Image {i+1} saved as: {image_filename}")
        else:
            print("Error: Could not capture image.")
            break
        
        # Calculate the time taken for this capture
        elapsed_time = time.time() - start_time
        total_time += elapsed_time  # Accumulate the total time
        
        # Wait for the specified interval
        time.sleep(interval)

        # Include the interval in the total time
        total_time += interval

    # Release the camera after finishing
    cap.release()

    # Calculate the average time per image (total_time includes all waits)
    average_time = total_time / num_images if num_images > 0 else 0
    print(f"Average time taken for each image (including wait): {average_time:.4f} seconds")

# Usage example: Take 100 pictures, one every 0.5 seconds
take_images_and_calculate_average(filename_base='output_image', interval=0.5, num_images=100)
