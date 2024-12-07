import cv2
import numpy as np

# Load the image
image = cv2.imread(r"dartboard_images\WIN_20241205_22_25_17_Pro.jpg")

# Define source points (corners of the dartboard)
src_points = np.float32([
    [ 326, 523],
    [ 913, 26],
    [1474, 460],
    [ 927, 1048]
])

# Define destination points for top-down view
dst_width, dst_height = 600, 600
dst_points = np.float32([
    [0, 0],
    [dst_width, 0],
    [dst_width, dst_height],
    [0, dst_height]
])

# Compute the perspective transformation matrix
matrix = cv2.getPerspectiveTransform(src_points, dst_points)

# Apply the perspective transformation
corrected_image = cv2.warpPerspective(image, matrix, (dst_width, dst_height))

# Display the corrected image
cv2.imshow("Corrected Dartboard View", corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()