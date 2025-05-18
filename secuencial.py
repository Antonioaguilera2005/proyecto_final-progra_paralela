# secuencial.py
import random
import time
from utils import UMBRAL, log_event

def generar_dato(tipo):
    if tipo == 'temperatura':
        return round(random.uniform(15.0, 45.0), 2)
    elif tipo == 'humedad':
        return round(random.uniform(30.0, 100.0), 2)
    elif tipo == 'presion':
        return round(random.uniform(950, 1050), 2)

def main():
    sensores = ['temperatura', 'humedad', 'presion']
    for i in range(30):  # 10 ciclos por cada tipo
        for tipo in sensores:
            dato = generar_dato(tipo)
            if dato > UMBRAL.get(tipo, float('inf')):
                print(f"[ALERTA] {tipo.upper()} crítica: {dato}")
                log_event(f"[ALERTA - SECUENCIAL] {tipo.upper()} crítica: {dato}")
            print(f"[{tipo.title()}] {dato}")
            log_event(f"[SECUENCIAL] Procesado {tipo}={dato}")
        time.sleep(1)

if __name__ == "__main__":
    main()
