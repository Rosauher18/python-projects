import time  


def temporizador(tiempo_segundos):
    while tiempo_segundos > 0: 
        minutos, segundos = divmod(tiempo_segundos, 60)  
        tiempo_formateado = f'{minutos:02d}:{segundos:02d}'  
        print(tiempo_formateado, end='\r') 
        time.sleep(1) 
        tiempo_segundos -= 1 

    print("\nEl tiempo ha terminado!") 


tiempo_total = int(input("Ingresa el tiempo en segundos para la cuenta regresiva: "))


temporizador(tiempo_total)