import cv2
import numpy as np

# Points in the input image
input_pts = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])  # Dartboard corners
# Corresponding points in the output (top-down) image
output_pts = np.float32([[0, 0], [board_width, 0], [board_width, board_height], [0, board_height]])

# Compute the transformation matrix
matrix = cv2.getPerspectiveTransform(input_pts, output_pts)

# Apply the perspective warp
warped = cv2.warpPerspective(image, matrix, (board_width, board_height))
