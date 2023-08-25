#Image Resize and Cropping
import cv2
import numpy as np

img = cv2.imread("Resources/00000004.jpg")
print(img.shape)

imgResize = cv2.resize(img, (400,500))
print(imgResize.shape)

imgCropped = img[400:700,300:800]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)