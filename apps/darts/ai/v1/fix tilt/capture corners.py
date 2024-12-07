import cv2
import numpy as np

# Initialize a list to store points
points = []

# Mouse callback function to capture clicks
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
        points.append([x, y])
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow("Select Perimeter Points", image)
        if len(points) == 4:
            cv2.destroyAllWindows()

# Load the image
image = cv2.imread(r"dartboard_images\WIN_20241205_22_25_17_Pro.jpg")
clone = image.copy()
cv2.imshow("Select Perimeter Points", image)
cv2.setMouseCallback("Select Perimeter Points", click_event)
cv2.waitKey(0)

# Define source points
src_points = np.float32(points)

print("Selected source points:", src_points)