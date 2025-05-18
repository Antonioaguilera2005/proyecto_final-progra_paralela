# utils.py
import os
import time

# Umbrales críticos
UMBRAL = {
    'temperatura': 35.0,
    'humedad': 90.0,
    'presion': 1020.0
}

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

def log_event(mensaje: str, lock=None):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entrada = f"[{timestamp}] {mensaje}\n"
    if lock:
        with lock:
            with open("logs/sistema.log", "a") as f:
                f.write(entrada)
    else:
        with open("logs/sistema.log", "a") as f:
            f.write(entrada)
