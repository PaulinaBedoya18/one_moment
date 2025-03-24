Gestor de Tareas (Consola)

Descripción

Este es un sistema de gestión de tareas desarrollado en Python para la materia de Nuevas Tecnologías. Permite a los usuarios agregar, listar, actualizar y eliminar tareas desde la línea de comandos.

El proyecto se desarrolló en equipo aplicando el uso de entornos virtuales, gestión de dependencias y control de versiones con GitHub.

Características

✅ Agregar tareas con título y descripción
✅ Listar tareas pendientes y completadas
✅ Marcar tareas como completadas
✅ Eliminar tareas
✅ Guardado de datos en un archivo Excel (tareas.xlsx)
✅ Estadísticas de tareas completadas usando gráficos con Matplotlib

Instalación y Configuración

1️⃣ Clonar el repositorio

git clone https://github.com/PaulinaBedoya18/one_moment.git
cd one_moment

2️⃣ Crear y activar el entorno virtual

python -m venv .venv  # Crear entorno virtual

Windows: source .venv/Scripts/activate

Mac/Linux: source .venv/bin/activate

3️⃣ Instalar dependencias

pip install -r requirements.txt

Uso

Para ejecutar la aplicación, usa el siguiente comando:

python main.py

Aparecerá un menú interactivo en la consola donde podrás realizar las siguientes acciones:
1️⃣ Agregar tarea
2️⃣ Listar tareas
3️⃣ Marcar tarea como completada
4️⃣ Eliminar tarea
5️⃣ Ver estadísticas
6️⃣ Salir

Dependencias utilizadas

📌 openpyxl - Para manipular archivos Excel
📌 pandas - Para análisis de datos
📌 matplotlib - Para generar gráficos estadísticos

Contribuciones

El equipo se dividió las tareas de la siguiente manera:

Persona 1: Configuración del entorno virtual, repositorio Git y archivo requirements.txt 📂

Persona 2: Implementación del sistema CRUD de tareas en Python 📝

Persona 3: Integración con archivos Excel y reportes 📊

Persona 4: Implementación de estadísticas con Matplotlib y documentación 🖊️

Licencia

Este proyecto es de uso académico y fue desarrollado como parte de la materia Nuevas Tecnologías.

🚀 ¡Esperamos que te sea útil! 🚀

