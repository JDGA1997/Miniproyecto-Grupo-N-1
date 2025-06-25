import tkinter as tk
from models.coleccion_eventos import ColeccionEventos

# Instancia de la colección de eventos
coleccion = ColeccionEventos()

def eventos_existentes(ventana, icon_path):
    nv = tk.Toplevel(ventana)
    nv.title("Lista de Eventos")
    nv.geometry("700x200")
    nv.iconbitmap(icon_path)
    
    # Aquí va la lista de eventos
    marco = tk.Frame(nv, bg="#ffffff")
    
    marco.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    scrollbar = tk.Scrollbar(marco)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    lista = tk.Listbox(marco, yscrollcommand=scrollbar.set)
    for evento in coleccion.obtener_eventos():
        lista.insert(tk.END, str(evento))
    
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=lista.yview)
    