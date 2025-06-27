import json
import os
from models.evento import Evento
from utils.logger import logger

# Clase para manejar la lista de eventos

class ColeccionEventos:
    def __init__(self):
        # Ruta absoluta al archivo eventos.json dentro de /src/
        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        self.archivo = os.path.join(base_dir, "..", "eventos.json") 
        self.archivo = os.path.normpath(self.archivo)
        self.eventos = []
        self.cargar_eventos()

    def agregar_evento(self, evento):
        self.eventos.append(evento)
        self.guardar_eventos()
        logger.info(f"Nuevo evento agregado: {evento.tipo} - {evento.fecha}")

    def guardar_eventos(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([e.to_dict() for e in self.eventos], f, indent=4, ensure_ascii=False)
            logger.info(f"Eventos guardados exitosamente en {self.archivo}")
        except Exception as e:
            logger.error(f"Error al guardar eventos: {e}")

    def cargar_eventos(self):
        self.eventos = []
        logger.info(f"Cargando eventos desde: {os.path.abspath(self.archivo)}")
        if os.path.exists(self.archivo):
            try:
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
                logger.info(f"{len(self.eventos)} eventos cargados exitosamente.")
            except json.JSONDecodeError:
                logger.error("Error: El archivo eventos.json está corrupto.")
            except KeyError as e:
                logger.error(f"Error: Falta el campo {e} en algún evento.")
            except Exception as e:
                logger.error(f"Error inesperado al cargar eventos: {e}")
        else:
            logger.info("Archivo no encontrado. Se creará uno nuevo al guardar.")
    
    def obtener_eventos(self):
        return self.eventos
    
    def eliminar_evento(self, indice):
        if 0 <= indice < len(self.eventos):
            eliminado = self.eventos.pop(indice)
            self.guardar_eventos()
            logger.info(f"Evento eliminado: {eliminado.tipo} - {eliminado.fecha}")
        else:
            logger.warning(f"Índice fuera de rango al eliminar evento: {indice}")
