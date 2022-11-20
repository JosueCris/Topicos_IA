import cv2
import numpy as np
from statistics import median, mean, mode, harmonic_mean, geometric_mean

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


##  MAX     ##
def get_max(kernel):
    return round(max(get_list(kernel, no_zeros=True)))

def filtro_maximo(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_max(kernel_matriz)
    return aux


##  MIN    ##
def get_min(kernel):
    return round(min(get_list(kernel, no_zeros=True)))

def filtro_minimo(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_min(kernel_matriz)
    return aux 


##  MEDIANA   ##
def get_median(kernel):
    return round(median(get_list(kernel)))

def filtro_mediana(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_median(kernel)
    return aux


##  MEDIA    ##
def get_mean(kernel):
    return round(mean(get_list(kernel)))

def filtro_media(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_mean(kernel_matriz)
    return aux


##  MODA    ##
def get_mode(kernel):
    return round(mode(get_list(kernel, no_zeros=True)))

def filtro_moda(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_mode(kernel_matriz)
    return aux    


##  HARMONIC    ##
def get_harmonic(kernel):
    return round(harmonic_mean(get_list(kernel, no_zeros=True)))

def filtro_harmonic(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_harmonic(kernel_matriz)
    return aux      


##  GEOMETRIC   ##
def get_geometric(kernel):
    return round(geometric_mean(get_list(kernel, no_zeros=True)))

def filtro_geometric(image, size):
    aux = image.copy()
    for i in range(len(image)):
        for j in range(len(image[0])):
            kernel_matriz = get_kernel_matriz(image, i, j, size)
            aux[i][j][2] = get_geometric(kernel_matriz)
    return aux          


##  MAIN    ##
img = cv2.imread("ei.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
minimo = filtro_minimo(hsv, 5)
result = cv2.cvtColor(minimo, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", img)
cv2.imshow("HSV", hsv)
cv2.imshow("minimo", result)
cv2.waitKey(0)