import openpyxl
import os

ARCHIVO_EXCEL = "tareas.xlsx"

def verificar_archivo():
    """Verifica si el archivo existe, si no, lo crea con estructura inicial."""
    if not os.path.exists(ARCHIVO_EXCEL):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Tareas"
        headers = ["ID", "Nombre", "Descripción", "Fecha Límite", "Estado"]
        sheet.append(headers)
        wb.save(ARCHIVO_EXCEL)

def cargar_tareas():
    """Carga las tareas desde el archivo Excel."""
    wb = openpyxl.load_workbook(ARCHIVO_EXCEL)
    sheet = wb.active
    tareas = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        tareas.append(list(row))
    return tareas

def guardar_tareas(tareas):
    """Guarda la lista de tareas en el archivo Excel."""
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Tareas"
    headers = ["ID", "Nombre", "Descripción", "Fecha Límite", "Estado"]
    sheet.append(headers)
    for tarea in tareas:
        sheet.append(tarea)
    wb.save(ARCHIVO_EXCEL)

from datetime import datetime
import openpyxl

def agregar_tarea(nombre, descripcion, fecha_limite):
    """Agrega una nueva tarea al archivo Excel."""
    tareas = cargar_tareas()
    nueva_tarea = [len(tareas) + 1, nombre, descripcion, fecha_limite, "Pendiente"]
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("✅ Tarea agregada con éxito.")

def listar_tareas():
    """Lista todas las tareas."""
    tareas = cargar_tareas()
    if not tareas:
        print("📂 No hay tareas registradas.")
    else:
        print("\n📋 Lista de tareas:")
        for tarea in tareas:
            print(f"{tarea[0]}. {tarea[1]} - {tarea[2]} (Fecha límite: {tarea[3]}) - Estado: {tarea[4]}")

def buscar_tarea(nombre):
    """Busca tareas por nombre."""
    tareas = cargar_tareas()
    resultados = [t for t in tareas if nombre.lower() in t[1].lower()]
    if resultados:
        print("\n🔍 Resultados:")
        for t in resultados:
            print(f"{t[0]}. {t[1]} - {t[2]} (Fecha límite: {t[3]}) - Estado: {t[4]}")
    else:
        print("🚫 No se encontraron tareas con ese nombre.")

        import pandas as pd

def completar_tarea(id_tarea):
    """Marca una tarea como completada."""
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea[0] == id_tarea:
            tarea[4] = "Completada"
            guardar_tareas(tareas)
            print("✅ Tarea marcada como completada.")
            return
    print("🚫 No se encontró la tarea.")

def eliminar_tarea(id_tarea):
    """Elimina una tarea por su ID."""
    tareas = cargar_tareas()
    tareas = [t for t in tareas if t[0] != id_tarea]
    guardar_tareas(tareas)
    print("🗑️ Tarea eliminada.")

def generar_reporte():
    """Genera un reporte de tareas usando pandas."""
    df = pd.read_excel(ARCHIVO_EXCEL)
    print("\n📊 Reporte de tareas:")
    print(df)
    print(f"\nTotal tareas: {len(df)}")
    print(f"Tareas pendientes: {len(df[df['Estado'] == 'Pendiente'])}")
    print(f"Tareas completadas: {len(df[df['Estado'] == 'Completada'])}")
