#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de logging para el Gestor de Eventos
"""

import logging
import os
from datetime import datetime

def setup_logger(name="gestor_eventos"):
    """
    Configura el sistema de logging para la aplicación
    """
    # Crear directorio de logs si no existe
    log_dir = os.path.join(os.path.dirname(__file__), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configurar el archivo de log con timestamp
    log_file = os.path.join(log_dir, f"gestor_eventos_{datetime.now().strftime('%Y%m%d')}.log")
    
    # Configurar el logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler()  # También mostrar en consola
        ]
    )
    
    logger = logging.getLogger(name)
    logger.info("Sistema de logging iniciado")
    return logger

# Logger global para la aplicación
logger = setup_logger()
