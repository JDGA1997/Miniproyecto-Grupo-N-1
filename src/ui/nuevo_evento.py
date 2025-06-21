import tkinter as tk

def nuevo_evento(ventana, icon_path):
    nv = tk.Toplevel(ventana)
    nv.title("Nuevo Evento")
    nv.geometry("300x200")
    nv.iconbitmap(icon_path)
    
    # Aquí va el formulario de la ventana
    
    #
    