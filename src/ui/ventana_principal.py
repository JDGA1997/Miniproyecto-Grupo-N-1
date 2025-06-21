# importamos las librerias necesarias
import customtkinter as ctk  # Interfaz moderna
from tkinter import messagebox
import tkinter as tk
import os
from PIL import Image, ImageTk

# importamos las funciones de los distintos modulos
from utils.reloj import actualizar_reloj
from ui.nuevo_evento import nuevo_evento
from ui.cancelar_evento import cancelar_evento
from ui.eventos_existentes import eventos_existentes

# Configuración de CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

def iniciar_ventana():
    # Ventana principal con customtkinter
    ventana = ctk.CTk()
    ventana.title("Gestor de Eventos")
    ventana.geometry("650x450")
    ventana.resizable(False, False)

    # Rutas de assets
    base_dir = os.path.dirname(__file__)
    icon_path = os.path.join(base_dir, "../assets/events_icon.ico")
    logo_path = os.path.join(base_dir, "../assets/logo.png")

    # Asignar el ícono
    try:
        ventana.iconbitmap(icon_path)
    except tk.TclError:
        print("No se pudo cargar el ícono 'events_icon.ico'. Asegúrate de que el archivo exista en la carpeta 'assets'.")

    # Frames para organización
    right_frame = ctk.CTkFrame(ventana, fg_color="transparent")
    right_frame.pack(side="right", fill="y", padx=20, pady=20)
    left_frame = ctk.CTkFrame(ventana, fg_color="transparent")
    left_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

    # Imagen principal
    try:
        imagen_pil = Image.open(logo_path)
        imagen_tk = ctk.CTkImage(light_image=imagen_pil, dark_image=imagen_pil, size=(250, 250))
        label_imagen = ctk.CTkLabel(left_frame, image=imagen_tk, text="")
        label_imagen.pack(pady=(10,0))
    except FileNotFoundError:
        label_imagen = ctk.CTkLabel(left_frame, text="Logo no encontrado", font=("Arial", 14))
        label_imagen.pack(pady=(10,0))

    # Texto principal y descripción
    text = ctk.CTkLabel(right_frame, text="Reserva tu Evento", font=("Arial", 28, "bold"))
    text.pack(anchor='e', pady=(10, 0))
    descripcion = ctk.CTkLabel(right_frame, text="Gestiona, organiza y controla tus eventos fácilmente.", font=("Arial", 14), wraplength=250, justify="right")
    descripcion.pack(anchor='e', pady=(10, 20))

    # Reloj en tiempo real (integración directa aquí)
    reloj = ctk.CTkLabel(right_frame, text="", font=('Arial', 16, "bold"))
    reloj.pack(anchor='e', pady=5)
    def actualizar_reloj_ctk():
        import time
        hora_actual = time.strftime('%H:%M:%S')
        reloj.configure(text=f"Hora actual en Argentina\n{hora_actual}")
        ventana.after(1000, actualizar_reloj_ctk)
    actualizar_reloj_ctk()

    # Barra de menú
    barra_menu = tk.Menu(ventana)
    ventana.config(menu=barra_menu)
    menu_opciones = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Opciones', menu=menu_opciones)
    menu_opciones.add_command(label='Nuevo evento', command=lambda: nuevo_evento(ventana, icon_path))
    menu_opciones.add_command(label='Eventos existentes', command=lambda: eventos_existentes(ventana, icon_path))
    menu_opciones.add_command(label='Cancelar evento', command=lambda: cancelar_evento(ventana, icon_path))
    menu_opciones.add_separator()
    menu_opciones.add_command(label='Salir', command=ventana.quit)

    ventana.mainloop()