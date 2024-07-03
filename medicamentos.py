# medicamentos.py

from time import localtime

class Temperatura_Medicamentos:
    def __init__(self):
        self.tipo_farmaco = {1: 'Productos refrigerados', 2: 'Productos en ambiente frío', 3: 'Productos en temperatura ambiente'}
        self.rangos = {
            1: (20, 80),  # 2.0°C a 8.0°C
            2: (80, 150),  # 8.0°C a 15.0°C
            3: (150, 250)  # 15.0°C a 25.0°C
        }
        self.tolerancia = 0.10  # 10%
        self.cantidad_total = {1: 0, 2: 0, 3: 0}
        self.fuera_rango = {1: 0, 2: 0, 3: 0}
        self.total_sensores = 0
        self.sensado_por_hora = [0] * 24

    def set_valor(self, temp, producto):
        if producto not in self.tipo_farmaco:
            return
        
        self.cantidad_total[producto] += 1
        self.total_sensores += 1
        
        hora_actual = localtime()[3]
        self.sensado_por_hora[hora_actual] += 1
        
        rango_min, rango_max = self.rangos[producto]
        tolerancia_min = rango_min - (rango_min * self.tolerancia)
        tolerancia_max = rango_max + (rango_max * self.tolerancia)
        
        if temp < tolerancia_min or temp > tolerancia_max:
            self.fuera_rango[producto] += 1

    def get_valores(self):
        return {
            "cantidad_total": self.cantidad_total,
            "fuera_rango": self.fuera_rango,
            "total_sensores": self.total_sensores,
            "sensado_por_hora": self.sensado_por_hora
        }

    def porcentaje_fuera_rango(self):
        total_fuera_rango = sum(self.fuera_rango.values())
        if self.total_sensores == 0:
            return 0
        return (total_fuera_rango / self.total_sensores) * 100

    def farmacos_sin_fuera_rango(self):
        return [k for k, v in self.fuera_rango.items() if v == 0]

    def fuera_rango_0_12(self):
        return sum(self.sensado_por_hora[0:13])
