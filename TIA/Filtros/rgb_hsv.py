## Tarea 1
## Investigar el Algoritmo para pasar del modelo RGB al HSV y viceversa
import colorsys
import math
import cv2

def RGB_to_HSV(red, green, blue):
    red = red/255.0
    green = green/255.0
    blue = blue/255.0

    minimo = min(red, green, blue)
    maximo = max(red, green, blue)
    diference = maximo - minimo

    if minimo == maximo:
        hue = 0
    elif maximo == red:
        hue = (60 * ((green-blue)/diference) +  360) % 360
    elif maximo == green:
        hue = (60 * ((blue-red)/diference) +  120) % 360
    elif maximo == blue:
        hue = (60 * ((red-green)/diference) +  240) % 360

    if maximo == 0:
        saturation = 0
    else:
        saturation = (diference/maximo) * 100

    value = maximo * 100
    return hue, saturation, value



def HSV_to_RGB(hue, saturation, value):
## if saturation == 0.0 :
##      return (value,value,value)

    c = value * saturation
    x = c * (1 - abs(((hue/60) % 2) - 1)) 
    m = value - c

    red = green = blue = 0
    if hue >= 0 and hue < 60:
        red, green, blue = (c, x, 0)        
    elif hue >= 60 and hue < 120:
        red, green, blue = (x, c, 0)
    elif hue >= 120 and hue < 180:
        red, green, blue = (0, c, x)
    elif hue >= 180 and hue < 240:
        red, green, blue = (0, x, c)
    elif hue >= 240 and hue < 300:
        red, green, blue = (x, 0, c)
    elif hue >= 300 and hue < 360:
        red, green, blue = (c, 0, x)

    (red, green, blue) = (math.ceil((red+m) * 255), math.ceil((green+m) * 255), math.ceil((blue+m) * 255))
    return red, green, blue


def BGR_to_HSV(b, g, r):
    return RGB_to_HSV(r, g, b)


def HSV_to_BGR(h, s, v):
    aux = HSV_to_RGB(h, s, v)
    return [aux[2], aux[1], aux[0]]


def BGR_to_RGB(b, g, r):
    return [r, g, b]


COLOR_HSV_RGB = 1
COLOR_BGR_HSV = 2
COLOR_HSV_BGR = 3


def conversion(image, option):
    aux = image.copy()
    for i in range(len(aux)):
        for j in range(len(aux[0])):
            if option == 1:
                aux[i][j] = HSV_to_RGB(aux[i][j][0], aux[i][j][1], aux[i][j][2])
            elif option == 2:
                aux[i][j] = BGR_to_HSV(aux[i][j][0], aux[i][j][1], aux[i][j][2])
            elif option == 3:
                aux[i][j] = HSV_to_BGR(aux[i][j][0], aux[i][j][1], aux[i][j][2])
    return aux



## "MAIN"
print("RGB - HSV")
print(RGB_to_HSV(255, 0, 0)) ## ROJO
print(RGB_to_HSV(0, 255, 0)) ## VERDE
print(RGB_to_HSV(0, 0, 255)) ## AZUL

print("\nHSV - RGB")
print(HSV_to_RGB(100, 1, .25))
##print(HSV_to_RGB(50, 5, 5))

## Funciones de la libreria colorsys

print("\nRGB - HSV (colorsys)")
print(colorsys.rgb_to_hsv(255, 0, 0))
print(colorsys.rgb_to_hsv(0, 255, 0))
print(colorsys.rgb_to_hsv(0, 0, 255))

## Solo para probar
print("\nHSV - RGB (colorsys)")
print(colorsys.hsv_to_rgb(100, 1, 1))