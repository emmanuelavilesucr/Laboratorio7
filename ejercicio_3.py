import psutil
import subprocess
import time
import matplotlib.pyplot as plt
from datetime import datetime

# Clase del monitoreo del proceso.
class MonitorProceso():
    def __init__(self, executable, intervalo_segundos, duracion_segundos):
        self.executable = executable
        self.intervalo_segundos = intervalo_segundos
        self.duracion_segundos = duracion_segundos

        # Listas para almacenar los datos de la gráfica
        self.tiempos = []
        self.uso_cpu = []
        self.uso_memoria = []
        self.proceso = None


    # Funcion encargada de la fase inicial del proceso.
    def iniciar_proceso(self):



    # Funcion encargada del monitoreo del proceso
    def monitorear(self):




    # Funcion encargada de generar el grafico con los datos obtenidos en el proceso. 
    def generar_grafico(self):




    # Funcion encargada de guardar los datos generados en el proceso.
    def guardar_registro(self):





# Funcion Main.
def main():



main()
