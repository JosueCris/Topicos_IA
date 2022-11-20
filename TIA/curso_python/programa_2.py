import cv2
import numpy as np
import time

alto = 600  #   pixeles
largo = 600 #   pixeles

def cartesian_to_pixel(x, y, alto, largo, escala): # Convierte una coordenada cartesiana a su equivalente en el display
        u = int((largo/2) + (x*escala))
        v = int((alto/2) - (y*escala))
        return (u, v)

def F_de_X (x):
    Y = x*x
    return Y


while True:
    dibujo = np.zeros((alto, largo, 3), np.uint8) # Es la ventana en la que se crea el entrono visual
    x0 = [0, 0]
    xf = [600, 600]
    O = [0, 0]
    
    Y0 = [0, 1000]
    YF = [0, -1000]
    X0 = [1000, 0]
    XF = [-1000, 0]
    O_uv = cartesian_to_pixel(O[0], O[1], alto, largo, 1)
    Y0_uv = cartesian_to_pixel(Y0[0], Y0[1], alto, largo, 1)
    YF_uv = cartesian_to_pixel(YF[0], YF[1], alto, largo, 1)
    X0_uv = cartesian_to_pixel(X0[0], X0[1], alto, largo, 1)
    XF_uv = cartesian_to_pixel(XF[0], XF[1], alto, largo, 1)

    ## Dibujamos los ejes
    #   eje x
    cv2.line(dibujo, X0_uv, XF_uv, (0, 0, 255), 1)
    #   eje y
    cv2.line(dibujo, Y0_uv, YF_uv, (255, 0, 0), 1)
    cv2.circle(dibujo, O_uv, 1, (255, 255, 255), 0)


## GRAFICACION DE PARABOLA
    ##vector = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10]

    ##for i in vector:
    for i in range(-10000, 10000, 1):
        ##print(i)
        x = i*.01
        y = F_de_X(x)
        U = cartesian_to_pixel(x, y, alto, largo, 2)
        cv2.circle(dibujo, U, 1, (0, 255, 0), -1)


    cv2.imshow("Dibujo", dibujo)
    if cv2.waitKey(1) is ord('s'):
        break
cv2.destroyAllWindows()
