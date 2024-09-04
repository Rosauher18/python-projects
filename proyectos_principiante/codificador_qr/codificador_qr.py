import os
import qrcode


folder_name = "codigosqr"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


data = input("Introduce un mensaje (maximo 250 caracteres): ")


if len(data) > 250:
    print("El mensaje excede el limite de 250 caracteres.")
else:
  
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

  
    qr.add_data(data)
    qr.make(fit=True)

   
    img = qr.make_image(fill="black", back_color="white")

   
    existing_files = os.listdir(folder_name)
    # Filtrar los archivos que siguen el patrón 'qrcode_X.png'
    qr_numbers = [int(f.split('_')[1].split('.')[0]) for f in existing_files if f.startswith("qrcode_") and f.endswith(".png")]
    next_number = max(qr_numbers, default=0) + 1  # Obtener el siguiente número
    img_path = os.path.join(folder_name, f"qrcode_{next_number}.png")  # Crear la ruta

    # 8. Guardar la imagen en la carpeta 'codigosqr'
    img.save(img_path)

    print(f"QR generado y guardado en '{img_path}'.")
