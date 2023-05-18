import cv2

# Leer la imagen
image = cv2.imread('C:\\Users\\jerry\\ImgPrueba\\YourMori.png')

# Convertir la imagen a escala de grises
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar filtro para eliminar ruido
image_filtered = cv2.GaussianBlur(image_gray, (5, 5), 0)

# Aplicar detector de bordes
image_edges = cv2.Canny(image_filtered, 50, 150)

# Buscar contornos
contours, _ = cv2.findContours(image_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pintar los contornos en la imagen original
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos
cv2.imshow('Contornos', image)
cv2.waitKey(0)

# Contabilizar contornos (objetos)
num_objetos = len(contours)
print("Número de objetos: ", num_objetos)

# Cerrar todas las ventanas
cv2.destroyAllWindows()