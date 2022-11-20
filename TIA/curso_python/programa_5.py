#Programa 5 procesamiento de imágenes con python
import cv2
import numpy as np
import matplotlib.pyplot as plt

video1= cv2.VideoCapture(0)
video1.set(3,640)#Largo
video1.set(4,360) #Ancho
while True:
	_,imagen = video1.read()
	img_recortada=imagen[0:300,0:300] #y0,yf,x0,xf
	size=imagen.shape[::-1]
	print(size)

	cv2.imshow("Camara", imagen)
	cv2.imshow("Camara chikita", img_recortada)
	

	if cv2.waitKey(1) == ord("s"):
		break
video1.release()
cv2.destroyAllWindows()