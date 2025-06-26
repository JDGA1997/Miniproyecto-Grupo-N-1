from datetime import datetime

# Clase Evento

class Evento:
    def __init__(self, tipo, fecha, hora, cantidad_personas, servicios):
        self.tipo = tipo
        self.fecha = fecha
        self.hora = hora
        self.cantidad_personas = cantidad_personas
        self.servicios = servicios
        self.creado_el = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def to_dict(self):
        return {
            "tipo": self.tipo,
            "fecha": self.fecha,
            "hora": self.hora,
            "cantidad_personas": self.cantidad_personas,
            "servicios": self.servicios,
            "creado_el": self.creado_el
        }

    def __str__(self):
        return (
                f"Evento: {self.tipo} - {self.fecha} {self.hora} | "
                f"{self.cantidad_personas} personas | Servicios: {self.servicios} "
                f"(Creado el {self.creado_el})"
                )
