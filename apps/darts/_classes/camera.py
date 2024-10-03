import shutil
import cv2
import time
import os
import shutil
import random




class CameraController:

    def __init__(self) -> None:
        self.filepath = '/home/toor/Documents/GitHub/Programming-Project/apps/darts/images'


    def take_image(self):
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: Could not open camera.")
            return

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        ret, frame = cap.read()
        if ret:
            image_filename = f"{self.filepath}_{random.randint(0, 1000)}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"Image saved as: {image_filename}")
        else:
            print("Error: Could not capture image.")

        cap.release()

    def wipe_image_folder(self):
        for filename in os.listdir(self.filepath):
            file_path = os.path.join(self.filepath, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")


        






# test function to take images and calculate average time taken
# just for testing

def take_images__constantly(interval):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    total_time = 0

    for i in range(num_images):
        start_time = time.time()
        
        ret, frame = cap.read()
        if ret:
            image_filename = f"{filename_base}_{i+1}.jpg"
            cv2.imwrite(image_filename, frame)
            print(f"Image {i+1} saved as: {image_filename}")
        else:
            print("Error: Could not capture image.")
            break
        
        elapsed_time = time.time() - start_time
        total_time += elapsed_time
        
        time.sleep(interval)
        total_time += interval

    cap.release()

    average_time = total_time / num_images if num_images > 0 else 0
    print(f"Average time taken for each image (including wait): {average_time:.4f} seconds")


#take_images_and_calculate_average(filename_base='output_image', interval=0.5, num_images=100)


main = CameraController()

while True:
    
    main.take_image()
