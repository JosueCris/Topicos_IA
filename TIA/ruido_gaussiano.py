import cv2
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import matplotlib.image  as nping

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
                kernel[it2].append(matriz[it][jt][0], matriz[it][jt][1], matriz[it][jt][2])
        it2 += 1
    return kernel

# Definimos tamaño del nuevo filtro
k = 3 # Este valor es el tamaño del kernel y puede variar si queremos
tam = 2*k+1

media = [0, 0]
covarianza = [[3, 0], [0, 3]]   ## Esto nos indica que tan centrado se encuentra nuestro kernel

# Cargamos la imagen en una variable
imagen = cv2.imread("image_noise-example.jpg")
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Creamos nuestro kernel
##kernel = np.ones((tam,tam), np.float32)/(tam**2)
kernel_gaussiano = np.zeros((tam,tam), np.float32) # Generamos nuestro kernel con ceros

# Llenamos nuestro kernel recorriendo cada posicion
for i in range(tam):
    for j in range(tam):
        x = [-k+i, -k+j] # Coordenadas donde queremos evaluar
        w = multivariate_normal.pdf(x, media, covarianza)
        kernel_gaussiano[i][j] = w

##plt.imshow(kernel_gaussiano)
##plt.show()

difuminado = cv2.filter2D(grises, -1, kernel_gaussiano)

cv2.imshow("Original", grises)
cv2.imshow("Filtrado Gaussiano", difuminado)
cv2.waitKey(0)
