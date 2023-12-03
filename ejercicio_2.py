import os
import subprocess  
import time 
import sys 

# Clase del Proceso
class MonitorProceso:
    def __init__(self, nombre_proceso, comando):
        self.nombre_proceso = nombre_proceso
        self.comando = comando

    # Funcion encargada de llevar a cabo el proceso
    def ejecutar_proceso(self):
        try:
            subprocess.Popen(self.comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Proceso {self.nombre_proceso} iniciado.")
        except Exception as e:
            print(f"Error al iniciar el proceso {self.nombre_proceso}: {e}")


    # Funcion encargada de monitorear el proceso
    def monitorear(self):

        # Verifica si el proceso está en ejecución consultando la lista de procesos del sistema
        while True:
            proceso_en_ejecucion = any(self.nombre_proceso in linea for linea in os.popen('tasklist'))
            
            # Si el proceso se ha cerrado, imprime un mensaje y reinicia el proceso
            if not proceso_en_ejecucion:
                print(f"¡Atención! El proceso {self.nombre_proceso} ha sido cerrado. Reiniciando...")
                self.ejecutar_proceso()

            time.sleep(5)  # Delay de 5 segundos


# Funcion del main
def main():

    if len(sys.argv) != 3:
        print("Uso: python script.py <nombre_proceso> <comando>")
        sys.exit(1)

    nombre_proceso = sys.argv[1]
    comando = sys.argv[2]
    monitor = MonitorProceso(nombre_proceso, comando)   
    monitor.ejecutar_proceso()
    monitor.monitorear()

main()
