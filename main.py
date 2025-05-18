# main.py
from multiprocessing import Queue, Event, Lock
from sensor import Sensor
from servidor import Servidor
import multiprocessing
import signal
import sys

SENSOR_TYPES = ['temperatura', 'humedad', 'presion']

def main():
    queue = Queue()
    stop_event = Event()
    lock = Lock()
    sensores = []

    # Crear sensores
    for tipo in SENSOR_TYPES:
        sensor = Sensor(tipo, queue, stop_event)
        sensor.start()
        sensores.append(sensor)

    servidor = Servidor(queue, stop_event, lock)

    def finalizar_gracefully(sig, frame):
        print("\n[Sistema] Finalizando...")
        stop_event.set()
        for s in sensores:
            s.join()
        print("[Sistema] Apagado completo.")
        sys.exit(0)

    # Manejo de Ctrl+C
    signal.signal(signal.SIGINT, finalizar_gracefully)

    # Ejecutar servidor
    servidor.ejecutar()

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    main()
