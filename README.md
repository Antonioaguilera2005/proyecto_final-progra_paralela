# 🌦️ Estación Meteorológica Simulada

Este proyecto simula el funcionamiento de una estación meteorológica virtual que obtiene lecturas de sensores de **temperatura**, **humedad** y **presión atmosférica**. Los datos se procesan de forma **secuencial** o **concurrente**, y se registran en un archivo de log.

Además, se generan **alertas automáticas** si se detectan valores fuera de los rangos definidos.

---

##  Estructura del proyecto

├── main.py # Ejecuta el modo concurrente por defecto
├── sensor.py # Define sensores virtuales
├── servidor.py # Lógica concurrente (multihilo)
├── alerta.py # Generación de alertas por valores anómalos
├── utils.py # Funciones auxiliares como el logger
├── secuencial.py # Lógica de ejecución secuencial
├── logs/
│ └── sistema.log # Archivo de log generado automáticamente


---

## ▶ ¿Cómo se ejecuta?

1. Abre una terminal en la carpeta raíz del proyecto.
2. Ejecuta:

python main.py
Esto ejecuta la versión concurrente del sistema (procesamiento en paralelo con hilos).

Si deseas ejecutar la versión secuencial manualmente:
python secuencial.py

Puedes modificar la frecuencia de las lecturas en el módulo de sensores.
El archivo main.py solo termina cuando usas ctrl-c en la consola.
El archivo secuencial termina despues de 30 lecturas de sensores.
Con el log se pueden comparar las dos versiones, además este debe vaciarse antes de cada uso para no acumular datos inutiles.

Programación Concurrente: se usa threading en servidor.py para leer sensores en paralelo.

Programación Secuencial: secuencial.py ejecuta los sensores uno por uno.

Logging: uso del módulo logging para guardar eventos, datos y alertas en logs/sistema.log.

Estructura modular: el código está dividido en módulos claros (sensor, alerta, utils...), siguiendo buenas prácticas.

Detección de condiciones críticas: se generan alertas si los sensores superan umbrales predefinidos.

El archivo sistema.log se genera automáticamente al iniciar cualquier modo.

Los umbrales para alertas están definidos en alerta.py.
