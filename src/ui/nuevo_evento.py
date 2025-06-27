import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from models.evento import Evento
from models.coleccion_eventos import ColeccionEventos
from config import TIPOS_EVENTOS, SERVICIOS_DISPONIBLES, UI_CONFIG
from utils.validaciones import validar_evento_completo, sugerir_fecha_hora_valida
from utils.logger import logger

# Instancia de la colección de eventos
coleccion = ColeccionEventos()

def nuevo_evento(ventana, icon_path):
    
    nv = tk.Toplevel(ventana)
    nv.title("Nuevo Evento")
    nv.geometry("400x400")
    nv.iconbitmap(icon_path)
    
    # Aquí va el formulario de la ventana
    # Estilo general para etiquetas y widgets
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TLabel', background="#514f58", foreground='white')
    style.configure('TCombobox', padding=5)
    style.configure('TSpinbox', padding=5)

    # Contenedor principal
    frame = ttk.Frame(nv, padding=20)
    frame.pack(padx=20, pady=20)
    
    # Información importante sobre fecha y hora
    info_frame = ttk.Frame(frame)
    info_frame.grid(column=0, row=0, columnspan=2, sticky='ew', pady=(0, 10))
    
    info_label = ttk.Label(info_frame, 
                          text="⚠️ Importante: La fecha y hora del evento deben ser futuras",
                          font=("Arial", 9, "bold"),
                          foreground="orange")
    info_label.pack()

    # Tipo de evento
    ttk.Label(frame, text="Tipo de evento:").grid(column=0, row=1, sticky='w')
    tipo_evento = ttk.Combobox(frame, values=TIPOS_EVENTOS)
    tipo_evento.grid(column=1, row=1)

    # Fecha de realización con tkcalendar
    ttk.Label(frame, text="Fecha de Realización:").grid(column=0, row=2, sticky='w')
    fecha = DateEntry(frame, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
    fecha.grid(column=1, row=2)
    
    # Etiqueta de ayuda para la fecha
    ttk.Label(frame, text="(Fecha futura)", font=("Arial", 8)).grid(column=1, row=2, sticky='e', padx=(0, 5))

    # Hora de realización
    ttk.Label(frame, text="Hora de Realización:").grid(column=0, row=3, sticky='w')
    hora = ttk.Entry(frame, width=10)
    hora.insert(0, UI_CONFIG["default_time"])  # Usar configuración
    hora.grid(column=1, row=3)
    
    # Etiqueta de ayuda para el formato de hora
    ttk.Label(frame, text=f"({UI_CONFIG['time_format']} - Futuro)", font=("Arial", 8)).grid(column=1, row=3, sticky='e', padx=(0, 5))

    # Cantidad de personas
    ttk.Label(frame, text="Cantidad de personas:").grid(column=0, row=4, sticky='w')
    cantidad = tk.Spinbox(frame, from_=UI_CONFIG["default_guests"], to=UI_CONFIG["max_guests"], increment=1, width=10)
    cantidad.grid(column=1, row=4)

    # Servicios requeridos
    ttk.Label(frame, text="Servicios Requeridos:").grid(column=0, row=5, sticky='w')
    servicios = ttk.Combobox(frame, values=SERVICIOS_DISPONIBLES)
    servicios.grid(column=1, row=5)

    # Función para crear un nuevo evento
    def crear_evento():
        try:
            tipo = tipo_evento.get()
            fecha_valor = fecha.get()
            hora_valor = hora.get()
            cantidad_valor = cantidad.get()
            servicio = servicios.get()

            # Usar el sistema de validación centralizado
            es_valido, errores = validar_evento_completo(tipo, fecha_valor, hora_valor, cantidad_valor, servicio)
            
            if not es_valido:
                # Generar sugerencia si el error está relacionado con fecha/hora
                fecha_sugerida, hora_sugerida = sugerir_fecha_hora_valida()
                
                error_msg = "Se encontraron los siguientes errores:\n\n" + "\n".join(f"• {error}" for error in errores)
                error_msg += f"\n\n💡 Sugerencia: Pruebe con {fecha_sugerida} a las {hora_sugerida}"
                
                respuesta = messagebox.askyesno("Errores de validación", 
                                              error_msg + "\n\n¿Desea usar la fecha y hora sugeridas?")
                
                if respuesta:
                    # Aplicar sugerencias automáticamente
                    from datetime import datetime
                    fecha_obj = datetime.strptime(fecha_sugerida, "%d/%m/%Y").date()
                    fecha.set_date(fecha_obj)
                    hora.delete(0, tk.END)
                    hora.insert(0, hora_sugerida)
                    messagebox.showinfo("Sugerencia aplicada", 
                                      f"Se ha establecido la fecha {fecha_sugerida} y hora {hora_sugerida}. "
                                      "Verifique los demás campos y presione 'Crear Evento' nuevamente.")
                return

            # Convertir cantidad a entero después de validar
            cantidad_valor = int(cantidad_valor)
            
            nuevo = Evento(tipo, fecha_valor, hora_valor, cantidad_valor, servicio)
            coleccion.agregar_evento(nuevo)
            logger.info(f"Evento creado exitosamente: {tipo} - {fecha_valor} {hora_valor}")
            messagebox.showinfo("Evento creado", f"Evento agregado exitosamente:\n{nuevo}")
            
            # Limpiar campos después de crear el evento
            tipo_evento.set('')
            servicios.set('')
            hora.delete(0, tk.END)
            hora.insert(0, UI_CONFIG["default_time"])
            cantidad.delete(0, tk.END)
            cantidad.insert(0, str(UI_CONFIG["default_guests"]))
            
        except Exception as e:
            logger.error(f"Error inesperado al crear evento: {e}")
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {str(e)}")

    # Botón para enviar
    boton = ttk.Button(frame, text="Crear Evento", command=crear_evento)
    boton.grid(column=0, row=7, columnspan=2, pady=10)