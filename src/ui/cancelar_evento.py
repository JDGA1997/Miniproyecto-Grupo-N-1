import tkinter as tk

def cancelar_evento(ventana, icon_path):
    nv = tk.Toplevel(ventana)
    nv.title("Cancelar Eventos")
    nv.geometry("300x200")
    nv.iconbitmap(icon_path)
    
    # Aquí va la logica de la ventana
    
    #