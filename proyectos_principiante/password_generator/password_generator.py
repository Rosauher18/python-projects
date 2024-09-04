import random 
import string 


# Definimos los conjuntos de caracteres
letras_minusculas = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
letras_mayusculas = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
numeros = string.digits  # 0123456789
simbolos = string.punctuation  #!@#$%^&*()_+-=[]{}|;:'",.<>?/ etc.


def password_generator(longitud):
    all_character = letras_minusculas + letras_mayusculas + numeros + simbolos
    # Generamos la contraseña seleccionando caracteres aleatorios
    password = ''.join(random.choice(all_character) for _ in range(longitud))
    return password


longitud_password = int(input("Cuantos caracteres debe tener la contrasena?: "))


contrasena_generada = password_generator(longitud_password)


print(f'Tu nueva contrasena es: {contrasena_generada}')
