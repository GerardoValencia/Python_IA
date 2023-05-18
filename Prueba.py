import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((500, 500))
num_circles = 20
circle_width = 5

outer_radius = min(image.shape) // 2
center = np.array(image.shape) // 2

for i in range(num_circles):
    radius = outer_radius - i * circle_width
    x, y = np.ogrid[:image.shape[0], :image.shape[1]]
    dist_from_center = np.sqrt((x - center[0]) ** 2 + (y - center[1]) ** 2)
    mask = np.abs(dist_from_center - radius) <= circle_width // 2  # Cambio aquí
    image[mask] = 255

plt.imshow(image, cmap='gray')
plt.axis('on')
plt.show()
