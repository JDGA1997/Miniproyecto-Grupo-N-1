from ui.ventana_principal import iniciar_ventana
from models.coleccion_eventos import ColeccionEventos

# función para ejecutar la ventana principal del gestor de eventos
#__name__ nos dice desde donde se está ejecutando el script
#__main__ indica que un archivo está siendo ejecutado directamente ≠ nombre del archivo

if __name__ == "__main__":
    coleccion = ColeccionEventos()
    iniciar_ventana()