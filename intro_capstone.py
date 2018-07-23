import cv2
import numpy as np
canvas = np.zeros((300, 300, 3), dtype = "uint8")
white = (255, 255, 255)
centerX = 150
centerY = 150
for r in range(10,256,10):
    cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.imwrite("concentric.jpg", canvas)