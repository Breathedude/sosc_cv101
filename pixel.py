#importing the openCV package
import cv2


# to read an image
var_image = cv2.imread("boruto.jpg",1)


# it's important to note that OpenCV stores RGB channels in reverse order.
#  While we normally think in terms of Red, Green, and Blue, 
# OpenCV actually stores them in the order of Blue, Green, and Red.

#we grab the pixel located at (0,0) - the topleft corner of the image. 
# This pixel is represented as a tuple. 
(b, g, r) = var_image[0, 0]
print(r,g,b)
# accessing is easy!

#pixel value manipulation
var_image[0, 0] = (0, 0, 255)
(b, g, r) = var_image[0, 0]
print(r,g,b)

#concept of slicing  can be used for cropping
corner = var_image[0:100, 0:100]
cv2.imshow("Corner", corner)
#and reassigning values
var_image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Updated", var_image)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
