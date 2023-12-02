import psutil
import sys

# Esta funcion es encargada de obtener todos los datos relacionados al proceso. 
def obtener_informacion_proceso():

    proceso = psutil.Process(pid)   # Obtiene el objeto del proceso utilizando psutil

    # Las siguientes lineas se encargan de obtener la información del proceso
    nombre_proceso = proceso.name()
    pid_proceso = proceso.pid
    ppid_proceso = proceso.ppid()
    usuario_propietario = proceso.username()
    uso_cpu = proceso.cpu_percent(interval=1)
    consumo_memoria = proceso.memory_info().rss
    estado_proceso = proceso.status()
    path_ejecutable = proceso.exe()


    # En esta seccion se imprime la información del proceso
    print("a) Nombre del proceso:", nombre_proceso)
    print("b) ID del proceso:", pid_proceso)
    print("c) Parent process ID:", ppid_proceso)
    print("d) Usuario propietario:", usuario_propietario)
    print("e) Porcentaje de uso de CPU:", uso_cpu, "%")
    print("f) Consumo de memoria:", consumo_memoria, "bytes")
    print("g) Estado (status):", estado_proceso)
    print("h) Path del ejecutable:", path_ejecutable)





# Funcion Main.
def main():




main()
