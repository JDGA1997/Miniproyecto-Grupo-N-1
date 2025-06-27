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
    coleccion.cargar_eventos()
    eventos = coleccion.obtener_eventos()
    
    if eventos:
        for evento in eventos:
            lista.insert(tk.END, str(evento))
    else:
        lista.insert(tk.END, "No hay eventos registrados")
        lista.config(state='disabled')  # Deshabilitar selección cuando no hay eventos
    
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar.config(command=lista.yview)
    