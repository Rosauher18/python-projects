import random
import pyttsx3

# Funci�n para que el sistema hable
def voz(mensaje):
    engine = pyttsx3.init()  # Inicializa el motor de voz
    voces = engine.getProperty('voices')
    engine.setProperty('voice', voces[1].id)  # Cambiar el �ndice seg�n tu sistema para espa�ol
    engine.say(mensaje)  # Decir el mensaje
    engine.runAndWait()  # Esperar a que termine de hablar

# Opciones del juego
opciones = ['piedra', 'papel', 'tijeras']

# Bucle principal del juego
while True:
    # El sistema dice "Piedra, papel o tijeras"
    voz("Piedra, papel o tijeras")

    # Opci�n del jugador
    jugador = input("Elige: Piedra, papel o tijeras: ").lower()

    # Verificar que la elecci�n sea v�lida
    if jugador not in opciones:
        print('Opcion invalida, intenta de nuevo.')
        continue

    # Opci�n de la computadora
    computadora = random.choice(opciones)
    print(f'La computadora eligio: {computadora}')

    # Comparar las elecciones y determinar el resultado
    if jugador == computadora:
        print('Es un empate.')
    elif (jugador == 'piedra' and computadora == 'tijeras') or \
         (jugador == 'papel' and computadora == 'piedra') or \
         (jugador == 'tijeras' and computadora == 'papel'):
        print("Ganaste!")
    else:
        print('La computadora gano.')

    # Preguntar si el jugador quiere jugar de nuevo
     
    jugar_de_nuevo = input("Quieres jugar de nuevo? (s/n): ").lower()
   
    # Si la respuesta no es 's', el juego termina
    if jugar_de_nuevo != 's':
        print('Gracias por jugar. Hasta luego!')
        break
