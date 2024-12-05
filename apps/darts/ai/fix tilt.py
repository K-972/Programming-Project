import cv2
import numpy as np

# Load the image
image = cv2.imread(r"dartboard_images\WIN_20241205_22_25_17_Pro.jpg")

# Define the center (x, y) and radius (r) of the dartboard circle
center = (500, 500)  # Example coordinates, change this to match your dartboard center
radius = 400         # Example radius, adjust based on the actual size of the dartboard

# Draw the outer circle (dartboard)
cv2.circle(image, center, radius, (0, 255, 0), 4)  # Green circle with thickness 4

# Draw the center of the circle
cv2.circle(image, center, 2, (0, 0, 255), 3)  # Red center with thickness 3

# Display the result
cv2.imshow("Dartboard with Defined Circles", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
