import cv2
import numpy as np

image = cv2.imread('images/lena.jpg')
height, width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
print(rotation_matrix)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()




flipped = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', flipped) 
cv2.waitKey()
cv2.destroyAllWindows()

