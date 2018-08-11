#importing the openCV and numpy packages
import cv2
import numpy as np

#creating a balck image of 300x300
canvas = np.zeros((300, 300, 3), dtype = "uint8")

#creating a green line from 0,0 to 300,300 and another line with thickness of 3 pixel from 300,0 to 0,300
#syntax: cv2.line(image,starting_point,ending_point,color)
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#syntax: cv2.line(image,starting_point,ending_point,color,thickness)
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#green rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green) 
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#thick red rectangle
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#thcikness as -1 will cause color fill
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#creating circles
white = (255, 255, 255)
centerX = 125
centerY = 125
r=50
cv2.circle(canvas, (centerX, centerY), r, white,2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()