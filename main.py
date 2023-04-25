import numpy
import cv2
import matplotlib


def detect(path):
    img = cv2.imread(path)

    # Pasar la ruta del XML
    cascade = cv2.CascadeClassifier('C:\\Users\ISND89\Documents\ISND\IA\haarcascade_frontalface_alt.xml')

    # Ejecutar la deteccion
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img


def box(rects, img):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
    # Ruta donde guardaremos la imagen con la deteccion de rostros
    cv2.imwrite('C:\\Users\ISND89\Pictures\prueba.jpg', img)

# Pasar la imagem que se quiere detectar
rects, img = detect('C:\\Users\ISND89\Downloads\gente.jpg')
box(rects, img)
