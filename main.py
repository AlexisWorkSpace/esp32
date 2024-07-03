# main.py

from placa import generar_datos, update_display, finalizar_testeo
from medicamentos import Temperatura_Medicamentos
import time

def simulacion():
    temp_med = Temperatura_Medicamentos()
    while True:
        data = generar_datos()
        if data:
            temp, producto, sensor, fin = data
            if fin == 0:
                break
            if producto != 0 and sensor != 0:
                update_display(sensor)
                temp_med.set_valor(temp, producto)
                time.sleep(0.05)

    # Encender LED al finalizar
    finalizar_testeo()
    
    # Informar los atributos de la clase
    valores = temp_med.get_valores()
    print("Cantidad total sensada por tipo de fármaco:", valores["cantidad_total"])
    print("Cantidad de valores fuera del rango:", valores["fuera_rango"])
    print("Cantidad total sensada por sensor:", temp_med.total_sensores)
    print("Cantidad sensada total por hora:", valores["sensado_por_hora"])

    # Informar el porcentaje de valores fuera de rango
    porcentaje = temp_med.porcentaje_fuera_rango()
    print(f"Porcentaje de valores fuera de rango: {porcentaje:.2f}%")

    # Fármacos sin valores fuera de rango
    farmacos_ok = temp_med.farmacos_sin_fuera_rango()
    print("Fármacos sin valores fuera de rango:", farmacos_ok)

    # Cantidad total de sensados fuera de rango entre las 0 y 12 hs
    fuera_rango_0_12 = temp_med.fuera_rango_0_12()
    print("Cantidad total de sensados fuera de rango entre las 0 y 12 hs:", fuera_rango_0_12)

if __name__ == "__main__":
    simulacion()
