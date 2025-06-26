import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from models.evento import Evento
from models.coleccion_eventos import ColeccionEventos

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

    # Tipo de evento
    ttk.Label(frame, text="Tipo de evento:").grid(column=0, row=0, sticky='w')
    tipo_evento = ttk.Combobox(frame, values=["Cumpleaños", "Baby Shower", "15 años", "Recepción", "Boda", "Aniversario", "Otro"])
    tipo_evento.grid(column=1, row=0)

    # Fecha de realización con tkcalendar
    ttk.Label(frame, text="Fecha de Realización:").grid(column=0, row=1, sticky='w')
    fecha = DateEntry(frame, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
    fecha.grid(column=1, row=1)

    # Hora de realización
    ttk.Label(frame, text="Hora de Realización:").grid(column=0, row=2, sticky='w')
    hora = ttk.Entry(frame)
    hora.insert(0, "00:00")
    hora.grid(column=1, row=2)

    # Cantidad de personas
    ttk.Label(frame, text="Cantidad de personas:").grid(column=0, row=3, sticky='w')
    cantidad = tk.Spinbox(frame, from_=1, to=1000, increment=1, width=10)
    cantidad.grid(column=1, row=3)

    # Servicios requeridos
    ttk.Label(frame, text="Servicios Requeridos:").grid(column=0, row=4, sticky='w')
    servicios = ttk.Combobox(frame, values=["Catering", "Música", "Decoración", "Fotografía"])
    servicios.grid(column=1, row=4)

    # Función para crear un nuevo evento
    def crear_evento():
        tipo = tipo_evento.get()
        fecha_valor = fecha.get()
        hora_valor = hora.get()
        cantidad_valor = int(cantidad.get())
        servicio = servicios.get()

        if not tipo or not servicio or not hora_valor:
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        nuevo = Evento(tipo, fecha_valor, hora_valor, cantidad_valor, servicio)
        coleccion.agregar_evento(nuevo)
        messagebox.showinfo("Evento creado", f"Evento agregado:\n{nuevo}")

        tipo_evento.set('')
        servicios.set('')
        hora.delete(0, tk.END)
        hora.insert(0, "00:00")
        cantidad.delete(0, tk.END)
        cantidad.insert(0, "1")

    # Botón para enviar
    boton = ttk.Button(frame, text="Crear Evento", command=crear_evento)
    boton.grid(column=0, row=5, columnspan=2, pady=10)
    #

