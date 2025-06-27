#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de validación para el Gestor de Eventos
"""

import re
from datetime import datetime, timedelta

def validar_hora(hora_str):
    """
    Valida que la hora esté en formato HH:MM y sea válida
    """
    if not hora_str:
        return False, "La hora no puede estar vacía"
    
    patron = r'^([01]?[0-9]|2[0-3]):[0-5][0-9]$'
    if not re.match(patron, hora_str):
        return False, "La hora debe estar en formato HH:MM (24 horas). Ejemplo: 14:30"
    
    return True, ""

def validar_fecha(fecha_str):
    """
    Valida que la fecha sea válida y no sea anterior a hoy
    """
    try:
        fecha_evento = datetime.strptime(fecha_str, '%d/%m/%Y')
        fecha_hoy = datetime.now()
        
        # No permitir fechas anteriores a hoy
        if fecha_evento.date() < fecha_hoy.date():
            return False, "La fecha del evento no puede ser anterior a hoy"
        
        return True, ""
    except ValueError:
        return False, "Formato de fecha inválido. Debe ser DD/MM/YYYY"

def validar_fecha_hora_futuras(fecha_str, hora_str):
    """
    Valida que la combinación de fecha y hora sea futura
    """
    try:
        # Validar formatos individuales primero
        es_valida_fecha, error_fecha = validar_fecha(fecha_str)
        if not es_valida_fecha:
            return False, error_fecha
            
        es_valida_hora, error_hora = validar_hora(hora_str)
        if not es_valida_hora:
            return False, error_hora
        
        # Combinar fecha y hora
        fecha_evento = datetime.strptime(fecha_str, '%d/%m/%Y')
        hora_evento = datetime.strptime(hora_str, '%H:%M').time()
        
        # Crear datetime completo del evento
        datetime_evento = datetime.combine(fecha_evento.date(), hora_evento)
        
        # Comparar con el momento actual
        ahora = datetime.now()
        
        if datetime_evento <= ahora:
            diferencia = ahora - datetime_evento
            if diferencia.days > 0:
                return False, f"El evento no puede ser {diferencia.days} día(s) en el pasado. Seleccione una fecha futura."
            elif diferencia.seconds > 3600:  # Más de 1 hora
                horas = diferencia.seconds // 3600
                return False, f"El evento no puede ser {horas} hora(s) en el pasado. Seleccione una hora futura."
            else:
                minutos = diferencia.seconds // 60
                return False, f"El evento debe programarse al menos 10 minutos en el futuro (faltan {minutos + 10} minutos)."
        
        return True, ""
        
    except ValueError as e:
        return False, f"Error en formato de fecha u hora: {str(e)}"

def sugerir_fecha_hora_valida():
    """
    Sugiere una fecha y hora válida para un evento (1 hora en el futuro)
    """
    fecha_sugerida = datetime.now() + timedelta(hours=1)
    fecha_str = fecha_sugerida.strftime("%d/%m/%Y")
    hora_str = fecha_sugerida.strftime("%H:%M")
    return fecha_str, hora_str

def obtener_mensaje_tiempo_minimo():
    """
    Retorna el tiempo mínimo requerido desde ahora para programar un evento
    """
    return "Los eventos deben programarse al menos 10 minutos en el futuro"

def validar_cantidad_personas(cantidad):
    """
    Valida que la cantidad de personas sea un número válido
    """
    try:
        num = int(cantidad)
        if num <= 0:
            return False, "La cantidad de personas debe ser mayor a 0"
        if num > 10000:
            return False, "La cantidad de personas parece excesiva (máximo 10,000)"
        return True, ""
    except ValueError:
        return False, "La cantidad de personas debe ser un número entero"

def validar_evento_completo(tipo, fecha, hora, cantidad, servicio):
    """
    Valida todos los campos de un evento
    """
    errores = []
    
    if not tipo:
        errores.append("Debe seleccionar un tipo de evento")
    
    if not servicio:
        errores.append("Debe seleccionar un servicio")
    
    # Validar que fecha y hora sean futuras (validación más estricta)
    es_valida_fecha_hora, error_fecha_hora = validar_fecha_hora_futuras(fecha, hora)
    if not es_valida_fecha_hora:
        errores.append(error_fecha_hora)
    
    # Validar cantidad (si la fecha/hora son válidas)
    es_valida_cantidad, error_cantidad = validar_cantidad_personas(cantidad)
    if not es_valida_cantidad:
        errores.append(error_cantidad)
    
    return len(errores) == 0, errores
