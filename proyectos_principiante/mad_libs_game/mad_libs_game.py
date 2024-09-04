"""
Crea un mad libs y al final lea en voz alta la historia final
"""
import pyttsx3

def texto_a_voz(historia):
    engine = pyttsx3.init()  
    engine.say(historia)  
    engine.runAndWait()  


print("Bienvenido al juego de Mad Libs")

# Pedir al usuario las palabras
nombre = input('Dime cual es tu nombre: ')
lugar = input('Dime un lugar: ')
accion = input('Dime una accion (Verbo): ')
adjetivo = input('Dime un adjetivo: ')

historia = (
    f"En un misterioso dia, {nombre} decidio aventurarse en el {lugar} mas peligroso del mundo. "
    f"Con valentia, comenzo a {accion}, sin saber lo que le esperaba. "
    f"De repente, todo se volvio {adjetivo} y la aventura tomo un giro inesperado."

    )

# Mostrar la historia
print("\nAqui tienes tu historia:")  
print(historia)

# Convertir la historia a voz
texto_a_voz(historia)