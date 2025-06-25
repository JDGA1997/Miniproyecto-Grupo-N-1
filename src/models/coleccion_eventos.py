import json
import os
from models.evento import Evento

# Clase para manejar la lista de eventos

class ColeccionEventos:
    def __init__(self, archivo="eventos.json"):
        self.archivo = archivo
        self.eventos = []
        self.cargar_eventos()

    def agregar_evento(self, evento):
        self.eventos.append(evento)
        self.guardar_eventos()

    def guardar_eventos(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.eventos], f, indent=4, ensure_ascii=False)

    def cargar_eventos(self):
        self.eventos = []
        print("Cargando eventos desde:", os.path.abspath(self.archivo))
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for d in datos:
                    e = Evento(
                        tipo=d["tipo"],
                        fecha=d["fecha"],
                        hora=d["hora"],
                        cantidad_personas=d["cantidad_personas"],
                        servicios=d["servicios"]
                    )
                    e.creado_el = d.get("creado_el", "Desconocido")
                    self.eventos.append(e)
            print(f"{len(self.eventos)} eventos cargados.")
        else:
            print("Archivo no encontrado.")
        
    def obtener_eventos(self):
        return self.eventos
