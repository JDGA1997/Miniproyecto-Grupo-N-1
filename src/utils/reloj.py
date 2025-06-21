import time

# Función para actualizar el reloj cada segundo
def actualizar_reloj(ventana, reloj):
    hora_actual = time.strftime('%H:%M:%S')
    reloj.config(text=f"Hora actual en Argentina\n {hora_actual}", font=("Arial", 16))
    ventana.after(1000, lambda: actualizar_reloj(ventana, reloj))