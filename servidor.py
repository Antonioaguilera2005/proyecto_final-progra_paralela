# servidor.py
import asyncio
import time
from alerta import enviar_alerta
from utils import UMBRAL, log_event

class Servidor:
    def __init__(self, queue, stop_event, lock):
        self.queue = queue
        self.stop_event = stop_event
        self.lock = lock

    async def procesar_dato(self, mensaje):
        tipo = mensaje['tipo']
        valor = mensaje['valor']
        sensor_id = mensaje['id']
        if valor > UMBRAL.get(tipo, float('inf')):
            await enviar_alerta(mensaje, self.lock)
        log_event(f"[Servidor] Procesado {tipo}={valor} de Sensor {sensor_id}", self.lock)

    def ejecutar(self):
        print("[Servidor] Iniciado y esperando datos...")
        loop = asyncio.get_event_loop()
        while not self.stop_event.is_set():
            if not self.queue.empty():
                mensaje = self.queue.get()
                loop.run_until_complete(self.procesar_dato(mensaje))
            else:
                time.sleep(0.1)
