# importamos las librerias necesarias
import tkinter as tk 
import os
from PIL import Image, ImageTk

# importamos las funciones de los distintos modulos
from utils.reloj import actualizar_reloj
from ui.nuevo_evento import nuevo_evento
from ui.cancelar_evento import cancelar_evento
from ui.eventos_existentes import eventos_existentes


# Configuración de la ventana principal

def iniciar_ventana():

    ventana = tk.Tk()

    # Título
    ventana.title("Gestor de Eventos")

    # Tamaño
    ventana.geometry("450x450")
    ventana.resizable(False, False)

    # Ruta absoluta a la carpeta del script
    base_dir = os.path.dirname(__file__)

    # Ruta completa al ícono
    icon_path = os.path.join(base_dir, "../assets/events_icon.ico")

    # Asignar el ícono
    ventana.iconbitmap(icon_path)

    # Cargar imagen
    imagen_path = os.path.join(base_dir, "../assets/logo.png")
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((150, 150))  # cambia el tamaño
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Mostrar imagen
    label_imagen = tk.Label(ventana, image=imagen_tk)
    label_imagen.image = imagen_tk  # mantener referencia
    label_imagen.pack(anchor='e', pady=(10, 0), padx=20)

    # Texto principal
    text = tk.Label(ventana, text="Reserva tu Evento", padx=20, pady=20)
    text.config(font=("Arial", 20), fg="blue")
    text.pack(anchor='e', pady=(10, 0), padx=20)

    # Descripción
    descripcion = tk.Label(ventana, text="Gestiona, organiza y controla tus eventos fácilmente\n", padx=20, wraplength=250)
    descripcion.config(font=("Arial", 12))
    descripcion.pack(anchor='e', pady=(0, 10), padx=20)

    # Reloj en tiempo real
    reloj = tk.Label(ventana, font=('Arial', 14), fg='black')
    reloj.pack(anchor='e', pady=5, padx=20, side='right')
    actualizar_reloj(ventana, reloj)  # Inicia el reloj


    # Crear la barra de menú
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)

    # Menú "Opciones" directamente en la barra principal
    menu_opciones = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Opciones', menu=menu_opciones)

    # Agregar comandos directamente a ese menú
    menu_opciones.add_command(label='Nuevo evento', command= lambda: nuevo_evento(ventana, icon_path))
    menu_opciones.add_command(label='Eventos existentes', command= lambda: eventos_existentes(ventana, icon_path))
    menu_opciones.add_command(label='Cancelar evento', command= lambda: cancelar_evento(ventana, icon_path))

    ventana.mainloop()