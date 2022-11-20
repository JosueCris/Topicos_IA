import cv2
##from cv2 import compare
import numpy as np
import math
##import matplotlib.pyplot as plt
from statistics import median, mean, harmonic_mean, geometric_mean, mode
##from rgb_hsv import RGB_to_HSV

def get_kernel_matriz(matriz, i, j, size):
    kernel = []
    for a in range(size):
        kernel.append(list())
    aux = int(size/2)
    it2 = 0
    for it in range(i-aux, i+aux+1):
        for jt in range(j-aux, j+aux+1):
            if not ((0 <= it < len(matriz)) and (0 <= jt < len(matriz[0]))):    
                kernel[it2].append([0, 0, 0])
            else:
                kernel[it2].append([matriz[it][jt][0], matriz[it][jt][1], matriz[it][jt][2]])
        it2 += 1
    return kernel

def get_list(kernel, no_zeros=False):
    lista1 = list()
    for i in range(len(kernel)):
        for j in range(len(kernel)):
            if kernel[i][j][2]==0 and no_zeros:
                continue
            lista1.append(kernel[i][j][2])
    return lista1


##  MEDIA   ##
def get_media(kernel):
    return round(median(get_list(kernel)))

def medianFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_media(kernel)
    return aux


##  CONVOLUCIONES   ##
def get_sum_cov(kernel1, kernel2):
    suma = 0
    for i in range(len(kernel1)):
        for j in range(len(kernel1)):
            suma += kernel1[i][j] * kernel2[i][j]
    return suma

def convolutionFilter(image, kernel):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, len(kernel))
            value = int (get_sum_cov(kernel_matriz, kernel))
            if value > 255:
                value = 255
            elif value < 255:
                value = 0
            aux[i][j] = value
    return aux


##  GAUSSIANO   ##
def get_gauss(sigma, size):
    matriz = []
    for i in range(size):
        matriz.append(list())
    s = 0
    y = int(size/2)
    temp = -1*y
    for i in range(size):
        x = temp
        for j in range(size):
            part1 = 1/(2 * math.pi * (sigma*sigma))
            part2 = pow(math.e, -1 * ((x*x) + (y*y)) / (2*(sigma*sigma)))
            matriz[i].append(part1 * part2)
            s += part1*part2
            x += 1
        y -= 1
    for i in range(size):
        for j in range(size):
            matriz[i][j] = matriz[i][j]/s
    return matriz

def get_value(gauss, kernel):
    suma = 0
    for i in range(len(gauss)):
        for j in range(len(gauss)):
            suma += gauss[i][j] * gauss[i][j][2]
    return suma

def gaussFilter(image, sigma, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            gauss_matriz = get_gauss(sigma, size)
            aux[i][j][2] = get_value(gauss_matriz, kernel_matriz)
    return aux    


##  MEAN    ##
def get_mean(kernel):
    return round(mean(get_list(kernel)))

def meanFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j] = get_mean(kernel_matriz)
    return aux


##  MAX     ##
def get_max(kernel):
    return round(max(get_list(kernel, no_zeros=True)))

def maxFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_max(kernel_matriz)
    return aux


##  MIN    ##
def get_min(kernel):
    return round(min(get_list(kernel, no_zeros=True)))

def minFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_min(kernel_matriz)
    return aux 


##  HARMONIC MEAN   ##
def get_harmonic_mean(kernel) :
    return round(harmonic_mean(get_list(kernel, no_zeros=True)))

def harmonicMeanFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_harmonic_mean(kernel_matriz)
    return aux


##  GEOMETRIC MEAN  ##
def get_geometric_mean(kernel):
    return round(geometric_mean(get_list(kernel, no_zeros=True)))

def geometricMeanFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_geometric_mean(kernel_matriz)
    return aux


##  MODE    ##
def get_mode(kernel):
    return round(mode(get_list(kernel, no_zeros=True)))

def modeFilter(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image)):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_mode(kernel_matriz)
    return aux      


##  MAIN    ##
img = cv2.imread("lenna.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
median = medianFilter(hsv, 5)
result = cv2.cvtColor(median, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", img)
cv2.imshow("Minimo", result)
cv2.waitKey(0)

##compare = np.concatenate((img, result), axis=1)

##plt.imshow(compare)
##plt.show()