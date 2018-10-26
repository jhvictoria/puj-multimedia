import cv2

image = cv2.imread('images/lena.jpg')
cv2.imshow('Translation', image)
cv2.waitKey()
cv2.destroyAllWindows()
