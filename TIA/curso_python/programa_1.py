import cv2
import numpy as np
import time

alto = 600  #   pixeles
largo = 600 #   pixeles

def cartesian_to_pixel(x, y, alto, largo, escala): # Convierte una coordenada cartesiana a su equivalente en el display
        u = int((largo/2) + (x*escala))
        v = int((alto/2) - (y*escala))
        return (u, v)


while True:
    dibujo = np.zeros((alto, largo, 3), np.uint8) # Es la ventana en la que se crea el entrono visual
    ##O = [int(largo/2), int(alto/2)+200]
    ##cv2.circle(dibujo, O, 300, (255,255,255), 0) # parametros: ventana, coordenadas, radio, color, grosor
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

    ##color = (255, 0, 255)
    ##grosor = 2
    ##cv2.line(dibujo, x0, xf, color, grosor) # parametros: ventana, origen, final, color, grosor

    cv2.imshow("Dibujo", dibujo)
    if cv2.waitKey(1) is ord('s'):
        break
cv2.destroyAllWindows()

## mañana ver figuras geometricas, circulo, recta, texto, recorte de una imagen, captura de video



##print("Hello World!!!")

##numero = -1
##palabra = str(numero) 
##print(numero)
##print(palabra)
##print(type(numero))
##print(type(palabra))

##if not numero > 0:
##    print("Si")
##else:
##    print("No")
##print("Sali del if")

##for i in [1, 2, 3, 4, 5, "A", [6, 7, 8]]:
##    if type(i) is list:
##       for j in i:
##           print(j)
##    else:
##        print(i)


##while True:
##    numero += 1
##    print(numero)
##    print("bandera 1")
##  if numero >= 1000:
##        break
##print("bandera 2")