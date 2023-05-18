import numpy as np
import matplotlib.pyplot as plt

# Crear una matriz de ceros de tamaño 500x500
image = np.zeros((500, 500))

# Número de círculos concéntricos a dibujar
num_circles = 20

# Ancho de cada círculo
circle_width = 5

# Calcular el radio exterior basado en el número de círculos y el ancho
outer_radius = min(image.shape) // 2 - (num_circles * circle_width // 2)

# Calcular el centro de la imagen
center = np.array(image.shape) // 2

# Iterar sobre cada círculo
for i in range(num_circles):
    # Calcular el radio del círculo actual
    radius = outer_radius - i * circle_width

    # Crear una cuadrícula de coordenadas X e Y
    x, y = np.ogrid[:image.shape[0], :image.shape[1]]

    # Calcular la distancia de cada punto al centro de la imagen
    dist_from_center = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)

    # Crear una máscara para los puntos dentro del círculo actual
    mask = np.abs(dist_from_center - radius) < circle_width // 2

    # Asignar el valor de 255 (blanco) a los puntos dentro del círculo
    image[mask] = 255

# Mostrar la imagen resultante en escala de grises
plt.imshow(image, cmap='gray')

# Mostrar los ejes en el gráfico
plt.axis('on')

# Mostrar el gráfico
plt.show()
