import os
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import tkinter as tk
from tkinter import filedialog

root = tk.Tk() 
root.withdraw()  

#Abrir el explorador de archivos para seleccionar una imagen
image_path = filedialog.askopenfilename(title="Selecciona una imagen QR", 
                                         filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")])

# Verificar si el usuario ha seleccionado un archivo
if not image_path:
    print("No se selecciono ninguna imagen.")
else:
    #  Leer la imagen del QR
    img = cv2.imread(image_path)

    # Decodificar el código QR
    decoded_objects = decode(img)

    # Verificar si se encontraron códigos QR
    if not decoded_objects:
        print('No se detecto ningun QR.')
    else:
        # Extraer y mostrar los datos decodificados
        for obj in decoded_objects:
            print('Tipo: ', obj.type)  # Tipo de código (en este caso, QR Code)
            print("Datos: ", obj.data.decode("utf-8"))