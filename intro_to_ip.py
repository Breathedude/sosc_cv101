import cv2
import imutils

image = cv2.imread("boruto.jpg")

#translation 
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 100, 0)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, 100, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

cv2.destroyAllWindows()

#translation 
shifted = imutils.translate(image, 0, -100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, -100, 0)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

shifted = imutils.translate(image, -100, -100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

cv2.destroyAllWindows()

#rotation
#syntax: imutils.rotate(image_name,angle)
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

rotated = imutils.rotate(image, 45)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)



#resizing
#syntax: imutils.resize(image,height/width=pixel_length)
resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height = 1000)
cv2.imshow("Resized via Function", resized)
cv2.waitKey(0)

cv2.destroyAllWindows()

#flipping

cv2.imshow("Original", image)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped) 

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

cv2.destroyAllWindows()

####################################################################################################################################################