import psutil
import sys

# Esta funcion es encargada de obtener todos los datos relacionados al proceso. 
def obtener_informacion_proceso():
    try:
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

    # Manejo de la excepción si el proceso no existe
    except psutil.NoSuchProcess as e:
        print(f"Error: No existe un proceso con el ID {pid}")

    # Manejo de otras excepciones 
    except Exception as e:
        print(f"Error inesperado: {e}")



# Funcion Main.
def main():
    if len(sys.argv) != 2:
        print("Uso: python script.py <ID_del_proceso>")
    else:
        pid_proceso = int(sys.argv[1])    # Obtiene el ID del proceso desde los argumentos de la línea de comandos
        obtener_informacion_proceso(pid_proceso)  # Llama a la función para obtener información del proceso
main()
