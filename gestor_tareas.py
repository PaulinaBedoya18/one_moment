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
