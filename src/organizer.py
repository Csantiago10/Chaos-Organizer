import os
import shutil
from src import core # Importamos tu cerebro de extensiones

def organize_directory(folder_path):
    # 1. Validar que la carpeta exista
    if not os.path.exists(folder_path):
        print(f"Error: La carpeta '{folder_path}' no existe.")
        return

    print(f"--- Iniciando limpieza en: {folder_path} ---")
    
    # 2. Obtener lista de archivos
    files = os.listdir(folder_path)

    for filename in files:
        # RUTA ORIGEN: (Tu tarea: Usa os.path.join con folder_path y filename)
        source_path = os.path.join(folder_path, filename) 

        # Si es una carpeta, saltarla (continue)
        if os.path.isdir(source_path):
            continue

        # Obtener nombre de carpeta destino (Usando core.get_target_folder)
        target_folder = core.get_target_folder(filename)

        # RUTA DESTINO DE LA CARPETA: (Usa os.path.join con folder_path y target_folder)
        target_path = os.path.join(folder_path, target_folder)

        # Crear carpeta si no existe (Investiga: os.makedirs con exist_ok=True)
        os.makedirs(target_path, exist_ok=True)

        # RUTA FINAL DEL ARCHIVO: (Usa os.path.join con target_path y filename)
        destination_path = os.path.join(target_path, filename)

        # MOVER:
        try:
            print(f"Moviendo {filename} a {target_folder}...")
            shutil.move(source_path, destination_path)
        except Exception as e:
            print(f"Error al mover {filename}: {e}")

    print("--- ¡Organización completada! ---")