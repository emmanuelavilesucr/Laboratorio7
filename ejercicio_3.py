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
        self.proceso = subprocess.Popen(self.executable)


    # Funcion encargada del monitoreo del proceso
    def monitorear(self):
        tiempo_inicio = datetime.now()
        try:
            while (datetime.now() - tiempo_inicio).total_seconds() < self.duracion_segundos:
                    # Obtiene el uso de CPU y memoria del proceso
                    uso_cpu_actual = self.proceso.cpu_percent(interval=1)
                    uso_memoria_actual = self.proceso.memory_info().rss / 1024 / 1024  # Convertir a MB

                    tiempo_actual = datetime.now()
                    self.tiempos.append(tiempo_actual)
                    self.uso_cpu.append(uso_cpu_actual)
                    self.uso_memoria.append(uso_memoria_actual)
                    time.sleep(self.intervalo_segundos)          # Espera el intervalo

        # Finalizar el proceso
        finally:
            self.proceso.terminate()
            self.proceso.wait()


    # Funcion encargada de generar el grafico con los datos obtenidos en el proceso. 
    def generar_grafico(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.tiempos, self.uso_cpu, label='CPU')
        plt.plot(self.tiempos, self.uso_memoria, label='Memoria')
        plt.xlabel('Tiempo')
        plt.ylabel('Uso (%) / Memoria (MB)')
        plt.title('Monitoreo de CPU y Memoria')
        plt.legend()
        plt.grid(True)
        plt.show()

    # Funcion encargada de guardar los datos generados en el proceso.
    def guardar_registro(self):
        with open('registro.txt', 'w') as archivo:
            for tiempo, cpu, memoria in zip(self.tiempos, self.uso_cpu, self.uso_memoria):
                archivo.write(f'{tiempo}: CPU={cpu}%, Memoria={memoria}MB\n')

def main():
    executable_path = 'Agregar ruta del ejecutable aqui'
    monitor = MonitorProceso(executable_path, intervalo_segundos=5, duracion_segundos=60)
    monitor.iniciar_proceso()
    monitor.monitorear()
    monitor.generar_grafico()
    monitor.guardar_registro()
main()
