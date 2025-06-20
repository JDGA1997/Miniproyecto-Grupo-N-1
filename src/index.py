from tkinter import messagebox
import tkinter as tk 
import time
import os
from PIL import Image, ImageTk
import customtkinter as ctk # librearia para un estilo más moderno si quieren


ventana = tk.Tk()

# Configuración de la ventana principal

# Título
ventana.title("Gestor de Eventos")

# Tamaño
ventana.geometry("650x450")
ventana.resizable(False, False)

# Ruta absoluta a la carpeta del script
base_dir = os.path.dirname(__file__)

# Ruta completa al ícono
icon_path = os.path.join(base_dir, "assets/events_icon.ico")

# Asignar el ícono
ventana.iconbitmap(icon_path)

# Cargar imagen
imagen_path = os.path.join(base_dir, "assets/logo.png")
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
descripcion = tk.Label(ventana, text="Gestiona, organiza y controla tus eventos fácilmente\n\n", padx=20)
descripcion.config(font=("Arial", 12))
descripcion.pack(anchor='e', pady=(0, 10), padx=20)

# Reloj en tiempo real
reloj = tk.Label(ventana, font=('Arial', 14), fg='black')
reloj.pack(anchor='e', pady=5, padx=20)

# Función para actualizar el reloj cada segundo
def actualizar_reloj():
    hora_actual = time.strftime('%H:%M:%S')
    reloj.config(text=f"Hora actual en Argentina\n {hora_actual}", font=("Arial", 16))
    ventana.after(1000, actualizar_reloj)

actualizar_reloj()  # Inicia el reloj



# Definir funciones que serán llamadas desde el menú
def nuevo_evento():
    messagebox.showinfo("Nuevo evento", "Aquí puedes crear un nuevo evento.")

def eventos_existentes():
    messagebox.showinfo("Eventos existentes", "Aquí se mostrarán los eventos.")

def cancelar_evento():
    messagebox.showinfo("Cancelar evento", "Aquí puedes cancelar un evento.")

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Menú "Opciones" directamente en la barra principal
menu_opciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Opciones', menu=menu_opciones)

# Agregar comandos directamente a ese menú
menu_opciones.add_command(label='Nuevo evento', command=nuevo_evento)
menu_opciones.add_command(label='Eventos existentes', command=eventos_existentes)
menu_opciones.add_command(label='Cancelar evento', command=cancelar_evento)

ventana.mainloop()