# Laboratorio 7

## Introducción

En este informe, se discutirán los resultados obtenidos mediante el monitoreo de procesos utilizando tres scripts en Python. Los códigos implementados utilizan las bibliotecas `psutil`, `subprocess`, `time`, `matplotlib`, y `datetime` para realizar tareas específicas relacionadas con el monitoreo de procesos.

### Primer ejercicio:

El primer script proporciona información detallada sobre un proceso dado a través de su ID. La función `obtener_informacion_proceso(pid)` utiliza la biblioteca `psutil` para obtener detalles como el nombre del proceso, ID del proceso, ID del proceso padre, usuario propietario, uso de CPU, consumo de memoria, estado del proceso y la ruta del ejecutable.

**Discusión de Resultados:**
- La información detallada brindada por el script es útil para comprender el estado y comportamiento del proceso en ejecución.
- Se proporciona manejo de excepciones para casos en los que el proceso no existe, lo cual mejora la robustez del script.

### Segundo ejercicio:

El segundo script crea la clase `MonitorProceso`, que inicia un proceso y lo monitorea continuamente. Si el proceso se cierra, el script lo reinicia automáticamente.

**Discusión de Resultados:**
- La clase `MonitorProceso` demuestra un enfoque práctico para garantizar que un proceso específico se mantenga en ejecución.
- El uso de `subprocess.Popen` para iniciar el proceso y el monitoreo continuo proporcionan una solución automatizada y resiliente.

### Tercer ejercicio:

El tercer script utiliza la biblioteca `psutil` para monitorear el uso de CPU y memoria de un proceso durante un período específico. Luego, genera un gráfico y guarda los datos en un archivo de registro.

**Discusión de Resultados:**
- El gráfico generado proporciona una visualización clara del comportamiento del proceso en términos de uso de CPU y memoria a lo largo del tiempo.
- La capacidad de guardar datos en un archivo de registro facilita un análisis más detallado y la revisión de tendencias.

## Conclusiones

- Los tres scripts demuestran diferentes enfoques para el monitoreo de procesos en Python, cada uno con sus ventajas y casos de uso específicos.
- La combinación de bibliotecas como `psutil`, `subprocess` y `matplotlib` facilita la implementación de soluciones de monitoreo y análisis de procesos.
- La elección del script a utilizar dependerá de los requisitos específicos, como la necesidad de información detallada, el reinicio automático del proceso o la generación de gráficos visuales.

En general, estos scripts proporcionan herramientas valiosas para el monitoreo y análisis de procesos en entornos de desarrollo y producción.

