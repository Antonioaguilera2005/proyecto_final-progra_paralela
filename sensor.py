# sensor.py
import random
import time
from multiprocessing import Process
import uuid

class Sensor(Process):
    def __init__(self, tipo_sensor, queue, stop_event, intervalo=1.0):
        super().__init__()
        self.tipo_sensor = tipo_sensor
        self.queue = queue
        self.intervalo = intervalo
        self.stop_event = stop_event
        self.sensor_id = str(uuid.uuid4())[:8]

    def generar_dato(self):
        if self.tipo_sensor == 'temperatura':
            return round(random.uniform(15.0, 45.0), 2)
        elif self.tipo_sensor == 'humedad':
            return round(random.uniform(30.0, 100.0), 2)
        elif self.tipo_sensor == 'presion':
            return round(random.uniform(950, 1050), 2)

    def run(self):
        while not self.stop_event.is_set():
            dato = self.generar_dato()
            mensaje = {
                'id': self.sensor_id,
                'tipo': self.tipo_sensor,
                'valor': dato,
                'timestamp': time.time()
            }
            print(f"[Sensor {self.sensor_id}] {self.tipo_sensor.title()}: {dato}")
            self.queue.put(mensaje)
            time.sleep(self.intervalo)
