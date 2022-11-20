import cv2
import numpy as np
from scipy.signal import convolve2d

imagen = cv2.imread("lenna.jpg")

##  CREAMOS NUESTRO KERNEL
kernelX = np.array([[-1], [1]])

bordesX = convolve2d(imagen, kernelX)

cv2.imshow("Bordes", bordesX)
