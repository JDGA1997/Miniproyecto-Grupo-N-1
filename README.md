<div align="center">
  <img src="https://github.com/user-attachments/assets/df02cfe1-dd25-41d8-9cc3-2cea31e60d1a" alt="Logo del Proyecto" width="400"/>


# Organizador de Eventos - Grupo N°1
## Etapa 2: Desarrollo Web

#### Un proyecto de aplicación de escritorio diseñada para la organización, registro y gestión integral de eventos.

---

<div align="left">

## 📋 Acerca del Proyecto

Este proyecto consiste en el desarrollo de una aplicación de escritorio multifuncional creada con Python y la biblioteca Tkinter. El objetivo es unificar las funcionalidades de cuatro miniproyectos individuales en una sola interfaz gráfica, creando una herramienta práctica para la organización y el registro de eventos.

La aplicación final busca ser un organizador de eventos completo, permitiendo al usuario gestionar diferentes tipos de celebraciones (como bodas, fiestas de 15 años, etc.), añadiendo y eliminando tareas o servicios asociados a cada evento

## ✨ Características Principales

### Crear Evento
- Selección de tipo de evento desde lista configurable
- Selector de fecha con calendario visual
- Validación de hora en formato 24 horas
- Selección de cantidad de personas con límites
- Opciones de servicios expandidas

### Ver Eventos
- Lista scrolleable de todos los eventos
- Información completa de cada evento
- Fecha de creación incluida

### Cancelar Eventos
- Selección desde lista
- Confirmación antes de eliminar
- Feedback visual del proceso

### Reloj en Tiempo Real
- Hora actual de Argentina
- Actualización automática cada segundo

---

## 🛠️ Tecnologías Utilizadas

Este proyecto fue construido utilizando las siguientes tecnologías:

- **Python 3.12+:** Lenguaje principal para el desarrollo de la lógica de la aplicación.

- **Tkinter:** Biblioteca estándar de Python utilizada para crear la interfaz gráfica de usuario (GUI).

- **CustomTkinter:** Biblioteca moderna para crear interfaces más atractivas y funcionales.

- **tkcalendar:** Widget de calendario para selección de fechas.

- **Pillow (PIL):** Procesamiento y manejo de imágenes.

- **JSON:** Para persistencia de datos de eventos.

- **Logging:** Sistema integrado de registro de eventos y errores.

## 📂 Estructura del proyecto
```
Miniproyecto-Grupo-N-1/
├── README.md
├── .gitignore
│
├── Mini proyectos (codigos base)/     # Mini proyectos originales
│   ├── 1er mini proyecto Menú desplegable/
│   ├── 2do mini proyecto_ Reloj simple/
│   ├── 3er mini proyecto_ Barra de desplazamiento/
│   └── 4to mini proyecto_ Lista de tareas/
│
├── Plantilla/                         # Plantillas de diseño
│   ├── PlantillaProyecto.drawio
│   └── PlantillaProyecto.drawio.png
│
└── src/                              # Código fuente principal
    ├── main.pyw                      # Punto de entrada de la aplicación
    ├── config.py                     # Configuraciones centralizadas
    ├── eventos.json                  # Persistencia de datos de eventos
    ├── requirements.txt              # Dependencias del proyecto
    │
    ├── models/                       # Modelos de datos
    │   ├── evento.py                 # Clase Evento
    │   ├── coleccion_eventos.py      # Gestión de la colección de eventos
    │   └── __pycache__/              # Archivos compilados de Python
    │
    ├── ui/                           # Interfaces de usuario
    │   ├── ventana_principal.py      # Ventana principal con CustomTkinter
    │   ├── nuevo_evento.py           # Formulario de creación de eventos
    │   ├── eventos_existentes.py     # Vista de eventos registrados
    │   ├── cancelar_evento.py        # Interfaz para eliminar eventos
    │   └── __pycache__/              # Archivos compilados de Python
    │
    ├── utils/                        # Utilidades y herramientas
    │   ├── reloj.py                  # Reloj en tiempo real
    │   ├── logger.py                 # Sistema de logging
    │   ├── validaciones.py           # Validaciones de datos y formularios
    │   ├── __pycache__/              # Archivos compilados de Python
    │   └── logs/                     # Archivos de registro
    │       └── gestor_eventos_YYYYMMDD.log
    │
    └── assets/                       # Recursos multimedia
        ├── logo.png                  # Logo de la aplicación
        └── events_icon.ico           # Ícono de la aplicación
```


## 🚀 Instalación y Ejecución

### 📥 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/JDGA1997/Miniproyecto-Grupo-N-1.git
   cd Miniproyecto-Grupo-N-1
   ```

2. **Verificar versión de Python:**
   ```bash
   python --version
   # Debe mostrar Python 3.8+ (recomendado 3.12+)
   ```

3. **Crear entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Instalar dependencias:**
   ```bash
   pip install -r src/requirements.txt
   ```

### ▶️ Ejecución

1. **Ejecutar la aplicación:**
   ```bash
   python src/main.pyw
   ```

2. **Ejecutar desde VS Code:**
   - Usar la tarea configurada "Ejecutar Gestor de Eventos"
   - Atajo: `Ctrl+Shift+P` → "Tasks: Run Task"

3. **Ejecutar pruebas (si están disponibles):**
   ```bash
   python test_completo.py
   ```

### 🔧 Solución de Problemas Comunes

#### Error: "ModuleNotFoundError: No module named 'customtkinter'"
```bash
pip install --upgrade pip
pip install customtkinter==5.2.2
```

#### Error: "No se pudo cargar el ícono"
- Verificar que `src/assets/events_icon.ico` existe
- La aplicación funcionará sin el ícono, pero mostrará una advertencia

#### Error: "Permission denied" en archivos de log
- Ejecutar como administrador (Windows)
- Verificar permisos de escritura en `src/utils/logs/`

#### Problemas de codificación de caracteres
- Asegurar que el sistema use codificación UTF-8
- En Windows, configurar `PYTHONIOENCODING=utf-8`

#### La aplicación no responde
- Verificar que no hay múltiples instancias ejecutándose
- Revisar los logs en `src/utils/logs/` para errores específicos

---

## 📋 Gestor de Tareas

Para la organización y seguimiento del desarrollo de este proyecto, utilizamos **Trello** como herramienta de gestión de tareas.
Nuestro tablero Kanban está estructurado con un flujo de trabajo completo que incluye desde la lluvia de ideas hasta la finalización de tareas.

**🔗 Accede a nuestro tablero de Trello:**
[![Trello Board](https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white)](https://trello.com/b/U2hvObES/miniproyecto-grupo-n1)

### Estructura del Tablero:
- **💡 Ideas**: Brainstorming y propuestas del equipo
- **📚 Recursos**: Materiales y herramientas de apoyo
- **🆕 Nuevo**: Tareas recién identificadas
- **📝 Por Hacer**: Actividades planificadas y asignadas
- **🔄 En Progreso**: Tareas actualmente en desarrollo
- **🔍 En Revisión**: Entregables en proceso de validación
- **✅ Hecho**: Tareas completadas exitosamente

El tablero nos permite mantener una visibilidad completa del progreso del proyecto y facilita la colaboración entre todos los miembros del equipo.


</div>

---

## 👩‍💻👨‍💻 Nuestro Equipo

Este proyecto fue posible gracias al trabajo colaborativo de nuestro equipo:

| Nombre y Apellido             | Usuario en GitHub                                     | Perfil de GitHub                                                                                                                              |
| ----------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Astrid Viñuela                | `AstridV23`                   | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AstridV23)   |
| Karen Belén Aquino            | `karenbaquino1`               | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/karenbaquino1) |
| Priscila Abril Quintana       | `priscilq`                    | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/priscilq)     |
| Juan Pablo Nuñez              | `Juampinz`                    | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Juampinz)     |
| Valentino André Cabás         | `Valen-cbs`                   | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Valen-cbs)     |
| Abril Silva Fernández         |                               | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/#)            |
| Juan Diego González Antoniazzi | `JDGA1997`                   | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JDGA1997)     |


---

</div>

---

## 💻 Requisitos del Sistema

### Requisitos Mínimos
- **Sistema Operativo:** Windows 10/11, macOS 10.14+, Linux Ubuntu 18.04+
- **Python:** Versión 3.8 o superior (recomendado 3.12+)
- **RAM:** 512 MB disponibles
- **Espacio en disco:** 50 MB para la aplicación y dependencias
- **Resolución:** 1024x768 píxeles mínimo

### Dependencias Principales
```txt
customtkinter==5.2.2          # Interfaz moderna para tkinter
Pillow==11.2.1                # Procesamiento de imágenes
tkcalendar==1.6.1             # Widget de calendario
```

## ⚙️ Características Técnicas

### Sistema de Logging
- **Archivos de log automáticos** con timestamp diario
- **Niveles de logging:** INFO, WARNING, ERROR
- **Ubicación:** `src/utils/logs/gestor_eventos_YYYYMMDD.log`
- **Rotación automática** por día

### 📊 Información de Logs

El sistema genera automáticamente archivos de log que registran:

- **Eventos creados y eliminados** con timestamps
- **Errores de validación** y sus correcciones
- **Operaciones de archivo** (carga/guardado de eventos)
- **Advertencias del sistema** (archivos faltantes, etc.)

**Ubicación de logs:** `src/utils/logs/gestor_eventos_YYYYMMDD.log`

**Ejemplo de entrada de log:**
```
2025-06-27 14:30:15 - gestor_eventos - INFO - Nuevo evento agregado: Baby Shower - 04/07/2025
2025-06-27 14:31:22 - gestor_eventos - INFO - Eventos guardados exitosamente en eventos.json
```

### Validaciones Integradas
- **Validación de fechas y horarios** futuros
- **Verificación de formatos** (DD/MM/YYYY, HH:MM)
- **Límites de capacidad** configurables
- **Sugerencias automáticas** para datos inválidos

### Persistencia de Datos
- **Formato JSON** para almacenamiento
- **Codificación UTF-8** para caracteres especiales
- **Respaldo automático** al guardar cambios
- **Recuperación de errores** en archivos corruptos

### Arquitectura del Proyecto
- **Patrón MVC** (Model-View-Controller)
- **Separación de responsabilidades** por módulos
- **Configuración centralizada** en `config.py`
- **Manejo de errores** robusto con try-catch

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

### Resumen de la Licencia MIT
- ✅ **Uso comercial** permitido
- ✅ **Modificación** permitida  
- ✅ **Distribución** permitida
- ✅ **Uso privado** permitido
- ❌ **Sin garantía** - el software se proporciona "tal como está"
- ⚠️ **Atribución requerida** - debe incluir el aviso de copyright

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡no olvides darle una estrella!

**Desarrollado con ❤️ por el Grupo N°1**

</div>
