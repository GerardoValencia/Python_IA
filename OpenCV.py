import numpy as np
import cv2

# Leer una imagen
img = cv2.imread('C:\\Users\ISND89\Documents\ISND\IA\objetos.jpg', 1)

# Mostrar imagen
cv2.imshow('Objetos', img)

# Imagen en escala de grises
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gris', img_gris)

# Filtro para eliminar ruido
filtro_gauss = cv2.GaussianBlur(img_gris, (5, 5), 0)
cv2.imshow('Suavizado', filtro_gauss)
cv2.waitKey(0)

# Detección de borde
Bordes_canny = cv2.Canny(filtro_gauss, 50, 150)
cv2.imshow('Bordes', filtro_gauss)

