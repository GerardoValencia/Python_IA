from __future__ import print_function
import cv2

# Leer una imagen
image = cv2.imread('C:\\Users\\ISND89\\Documents\\ISND\\IA\\chargers.jpg')

# Mostrar la imagen
cv2.imshow("Image", image)

# Mostrar las dimensiones de la imagen
print("Dimensiones de la imagen: ", image.ndim)

# Mostrar el tamaño de la imagen
print("Alto de la imagen: ", format(image.shape[0]))
print("Ancho de la imagen: ", format(image.shape[1]))

# Dibujar una línea en la imagem
start = (0, 0)
end = (image.shape[1], image.shape[0])
color = (255, 255, 255)
thickness = 4

cv2.line(image, start, end, color, thickness)

# Mostrar la imagen
cv2.imshow("Line", image)

# Dibujar un rectangulo en la imagen
start = (100, 100)
end = (800, 800)
color = (255, 255, 255)
thickness = 4

cv2.rectangle(image, start, end, color, thickness)

# Mostrar la imagen
cv2.imshow("Rectangle", image)

# Dibujar un circulo en la imagen
center = (700, 600)
radius = 400
color = (255, 0, 255)
thickness = -1

cv2.circle(image,center, radius, color, thickness)

# Mostrar la imagen
cv2.imshow("Circle", image)

# Pasar la imagen a escala de grises
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', grayImage)

# Grabar la imagen en disco duro
cv2.imwrite("Gris.jpg", grayImage)

# Rotar la imagen
(h,w) = image.shape[:2]
center = (h//2, w//2)
angle = -90
scale = 1.0

rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)
rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1], image.shape[0]))

cv2.imshow("Rotated image", rotatedImage)

# Filtro para eliminar ruido
gaussFilter = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Filtered', gaussFilter)

# Detectar bordes de la imagen
edgesImage = cv2.Canny(gaussFilter, 50, 150)
cv2.imshow('Edges', edgesImage)

# Detectar contornos
contours, _ = cv2.findContours(edgesImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Remarcar contornos
cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', image)
cv2.waitKey(0)

# Contabilizar contornos (objetos)
num_objetos = len(contours)
print("Número de objetos: ", num_objetos)

# Cerrar todas las ventanas
cv2.destroyAllWindows()