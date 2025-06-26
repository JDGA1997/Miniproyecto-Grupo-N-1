import tkinter as tk
from tkinter import messagebox
from models.coleccion_eventos import ColeccionEventos

# Instancia de la colección de eventos
coleccion = ColeccionEventos()

def cancelar_evento(ventana, icon_path):
    nv = tk.Toplevel(ventana)
    nv.title("Cancelar Eventos")
    nv.geometry("700x300")
    nv.resizable(False, False)
    nv.iconbitmap(icon_path)
    
    # Aquí va la lista de eventos
    marco = tk.Frame(nv, bg="#f59999")
    
    marco.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    scrollbar = tk.Scrollbar(marco)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    lista = tk.Listbox(marco, yscrollcommand=scrollbar.set)
    for evento in coleccion.obtener_eventos():
        lista.insert(tk.END, str(evento))
    
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)
    
    def eliminar_evento(lista):
        seleccion = lista.curselection()
        if seleccion:
            indice = seleccion[0]
            evento_texto = lista.get(indice)
            confirmado = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro que querés eliminar este evento?\n\n{evento_texto}")
            if confirmado:
                coleccion.eliminar_evento(indice)
                lista.delete(indice)
                messagebox.showinfo("Eliminado", "El evento ha sido eliminado con éxito.")
        else:
            messagebox.showwarning("Sin selección", "Por favor seleccioná un evento para eliminar.")

    
    boton_eliminar = tk.Button(nv, text="Eliminar Evento", bg="#d9534f", fg="white", font=("Arial", 10, "bold"), command=lambda: eliminar_evento(lista))
    boton_eliminar.pack(pady=10, side=tk.BOTTOM)
