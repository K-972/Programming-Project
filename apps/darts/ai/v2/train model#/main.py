from ultralytics import YOLO
import os

# Configuration
model_name = "yolov8s.pt"  # Pre-trained YOLOv8 model
config_file = "dart.yaml"  # Path to your dataset YAML configuration file
output_dir = "runs/detect/train"  # Output directory for the trained model
num_epochs = 50  # Number of epochs
image_size = 640  # Image size for training

# Ensure configuration file exists
if not os.path.exists(config_file):
    raise FileNotFoundError(f"Configuration file not found: {config_file}")

# Train the model
try:
    print("Starting YOLOv8 training...")
    model = YOLO(model_name)  # Load the pre-trained model
    model.train(
        data=config_file,
        epochs=num_epochs,
        imgsz=image_size,
        project=output_dir,
        name="dart_detection"
    )
    print("Training completed successfully!")
    print(f"Best model saved at: {os.path.join(output_dir, 'dart_detection/weights/best.pt')}")

except Exception as e:
    print(f"Error during training: {e}")
