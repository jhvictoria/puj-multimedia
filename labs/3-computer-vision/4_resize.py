import cv2
import numpy as np
import time

image = cv2.imread('images/lena.jpg')

# Imagen 3/4 del tamaño original
image_scaled = cv2.resize(image, None, fx=0.75, fy=0.75)
cv2.imshow('Scaling - Linear Interpolation', image_scaled) 
cv2.waitKey()

# Duplicar el tamaño
img_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Scaling - Cubic Interpolation', img_scaled)
cv2.waitKey()

# Redimensionar a un tamaño exacto
img_scaled = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
cv2.imshow('Scaling - Skewed Size', img_scaled) 
cv2.waitKey()
cv2.destroyAllWindows()


# image pyramids
smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(image)

cv2.imshow('Original', image )
cv2.waitKey()
cv2.imshow('Smaller ', smaller )
cv2.waitKey()
cv2.imshow('Larger ', larger )
cv2.waitKey()
cv2.destroyAllWindows()
