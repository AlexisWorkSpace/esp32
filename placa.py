# placa.py

import random
from machine import Pin, Timer

# Simulación de sincronismo
s1 = 1
s2 = 1

# Configuración del display de 7 segmentos
# Aquí definirías cómo controlar tu display de 7 segmentos con GPIOs del ESP32
display_pins = [Pin(i, Pin.OUT) for i in range(7)]

def update_display(sensor_number):
    # Aquí deberías actualizar los pines del display para mostrar el número del sensor
    pass

# Función para generar datos simulados
def generar_datos():
    global s1, s2
    temp = random.randint(20, 300)  # Temperatura en décimas de grado (2.0°C a 30.0°C)
    producto = random.randint(0, 3)  # Tipo de Producto (1, 2, 3, o 0 para ignorar)
    sensor = random.randint(0, 7)  # Número de Sensor (1 a 7, o 0 para ignorar)
    fin = random.randint(0, 1)  # Fin del sensado (0 para terminar)

    # Sincronismo
    s1 = random.randint(0, 1)
    s2 = random.randint(0, 1) if random.random() > 0.5 else s1

    if s1 == s2:
        return (temp, producto, sensor, fin)
    else:
        return None

# Función para encender el LED al finalizar el testeo
def finalizar_testeo():
    led = Pin(17, Pin.OUT)
    led.on()
