#importing the openCV package
import cv2


# to read an image
#syntax : cv2.imread(path_to_image,flag)
var_image = cv2.imread("boruto.jpg",0)


#display details about image
#width,height
print(var_image.shape)


# to display the image which was read
#syntax : cv2.imshow(window_name,image)
cv2.imshow("Image", var_image)
# cv2.waitKey pauses the execution of the script until we press a key on our keyboard.
# Using a parameter of 0 indicates that any keypress will un-pause the execution
cv2.waitKey(0)
cv2.destroyAllWindows()


# to write/save the image
# syntax: cv2.imwrite(to_save_as,image)
cv2.imwrite("newimage.png", var_image)