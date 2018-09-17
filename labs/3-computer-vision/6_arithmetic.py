import cv2
import numpy as np

image = cv2.imread('images/lena.jpg')

M = np.ones(image.shape, dtype = "uint8") * 175 

added = cv2.add(image, M)
cv2.imshow("Added", added)

subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
