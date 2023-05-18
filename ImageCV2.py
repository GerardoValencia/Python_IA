from __future__ import print_function
import cv2

# image path
image_path = "C:\\Users\\jerry\\ImgPrueba\\YourMori.png"

# Read or load image from its path
image = cv2.imread(image_path)

# image is a NumPy array
print("Dimensions of the image: ", image.ndim)
print("Image height: ", format(image.shape[0]))
print("Image width: ", format(image.shape[1]))
print("Image channels: ", format(image.shape[2]))
print("Size of the image array: ", image.size)

# Display the image and wait until a key is pressed
cv2.imshow("My Image", image)


# image path
image_path = "C:\\Users\\jerry\\ImgPrueba\\YourMori.png"

# Read or load image from its path
image = cv2.imread(image_path)

# Set start and end coordinates
start = (0, 0)
end = (image.shape[1], image.shape[0])

# Set the color in BGR
color = (255, 0, 0)

# Set thickness in pixel
thicknes = 4
cv2.line(image, start, end, color, thicknes)

# Display the modified image
cv2.imshow("Modified Image", image)


# image path
image_path = "C:\\Users\\jerry\\ImgPrueba\\YourMori.png"

# Read or load image from its path
image = cv2.imread(image_path)

# Set start and end coordinates
# of the top-left and bottom-right corners of the rectangle
start = (100, 70)
end = (350, 380)

# Set the color and thickness of the outline
color = (0, 255, 0)
thickness = 5

# Draw the rectangle
cv2.rectangle(image, start, end, color, thickness)

# Save the modified image with the rectangle drawn to it
cv2.imwrite("rectangle.jpg", image)

# Display the modified image
cv2.imshow("Rectangle", image)


# Load image
image_path = "C:\\Users\\jerry\\ImgPrueba\\YourMori.png"
image = cv2.imread(image_path)
(h,w) = image.shape[:2]

# Define translation matrix
center = (h//2, w//2)
angle = -45
scale = 1.0

rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)

# Rotate the image
rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1], image.shape[0]))

cv2.imshow("Rotated image", rotatedImage)
cv2.waitKey(0)