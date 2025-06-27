#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo de configuración para el Gestor de Eventos
"""

# Configuración de la aplicación
APP_CONFIG = {
    "title": "Gestor de Eventos",
    "version": "1.0.0",
    "window_size": "650x450",
    "icon": "events_icon.ico",
    "logo": "logo.png"
}

# Tipos de eventos disponibles
TIPOS_EVENTOS = [
    "Cumpleaños",
    "Baby Shower", 
    "15 años",
    "Recepción",
    "Boda",
    "Aniversario",
    "Graduación",
    "Despedida",
    "Otro"
]

# Servicios disponibles
SERVICIOS_DISPONIBLES = [
    "Catering",
    "Música",
    "Decoración", 
    "Fotografía",
    "Bebidas",
    "Cotillón",
    "Seguridad",
    "Limpieza"
]

# Configuración de archivos
FILES_CONFIG = {
    "eventos_json": "eventos.json",
    "encoding": "utf-8"
}

# Configuración de la interfaz
UI_CONFIG = {
    "default_time": "14:00",
    "default_guests": 1,
    "max_guests": 1000,
    "time_format": "HH:MM"
}
