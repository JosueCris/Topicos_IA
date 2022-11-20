# Este es el ruido sal y pimienta
import cv2
import random

def sal_pimienta(imagen, porcentaje):
    cant = int(porcentaje * imagen.shape[0] * imagen.shape[1])  # Número de puntos de ruido de sal y pimienta
    random.randint(0, imagen.shape[0])
    
    ruido = imagen.copy()

    for i in range(cant):
        x = random.randint(0, ruido.shape[0] - 1)   # Un número entero aleatorio desde 0 hasta la longitud de la imagen, porque es un intervalo cerrado, -1
        y = random.randint(0, ruido.shape[1] - 1)
        
        if random.randint(0, 1) == 0:   # Probabilidad en blanco y negro 55 abierto
            ruido[x, y] = (255, 255, 255)   # Blanco
        else:
            ruido[x, y] = (0, 0, 0)   # Negro
    return ruido


img = cv2.imread("lenna.jpg")
grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##porciento = float(input("Ingresa el porcentaje de ruido: "))    # Con escala de decimales 
img2 = sal_pimienta(img, 0.05)  # 5 por ciento de ruido de sal y pimienta
grises2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", grises)
cv2.imshow("Con ruido", grises2)
cv2.waitKey(0)

