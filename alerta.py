# alerta.py
import asyncio
from utils import log_event

async def enviar_alerta(mensaje, lock):
    tipo = mensaje['tipo']
    valor = mensaje['valor']
    sensor_id = mensaje['id']
    alerta = f"[ALERTA] {tipo.upper()} crítica ({valor}) en Sensor {sensor_id}"
    print(alerta)
    log_event(alerta, lock)
    await asyncio.sleep(0.1)  # Simula I/O (correo, red, etc.)
