import os

# DEFINIMOS LA JERARQUÍA: Categoría / Subcarpeta
# Usamos os.path.join para que Windows ponga "\" y Linux ponga "/"
EXTENSION_MAP = {
    # IMAGES
    '.jpg': os.path.join('Images', 'JPG_JPEG'), 
    '.jpeg': os.path.join('Images', 'JPG_JPEG'),
    '.png': os.path.join('Images', 'PNG'),
    '.gif': os.path.join('Images', 'GIF'),
    '.webp': os.path.join('Images', 'WebP'),
    '.svg': os.path.join('Images', 'Vector'),
    '.psd': os.path.join('Images', 'Design_Files'),
    '.ai': os.path.join('Images', 'Design_Files'),

    # DOCUMENTS
    '.pdf': os.path.join('Documents', 'PDFs'),
    '.txt': os.path.join('Documents', 'Text_Files'),
    '.doc': os.path.join('Documents', 'Word'),
    '.docx': os.path.join('Documents', 'Word'),
    '.xls': os.path.join('Documents', 'Excel'),
    '.xlsx': os.path.join('Documents', 'Excel'),
    '.csv': os.path.join('Documents', 'Excel'),
    '.ppt': os.path.join('Documents', 'PowerPoint'),
    '.pptx': os.path.join('Documents', 'PowerPoint'),

    # AUDIO & VIDEO
    '.mp3': os.path.join('Media', 'Audio_MP3'),
    '.wav': os.path.join('Media', 'Audio_WAV'),
    '.mp4': os.path.join('Video', 'Video_MP4'),
    '.mov': os.path.join('Video', 'Video_MOV'),
    '.avi': os.path.join('Video', 'Video_AVI'),
    '.mkv': os.path.join('Video', 'Video_MKV'),

    # ARCHIVES
    '.zip': os.path.join('Archives', 'Zip'),
    '.rar': os.path.join('Archives', 'Rar'),
    '.exe': os.path.join('Installers', 'Executables'),
    '.msi': os.path.join('Installers', 'MSI'),
    
    # CODE
    '.py': os.path.join('Developer', 'Python'),
    '.js': os.path.join('Developer', 'JavaScript'),
    '.html': os.path.join('Developer', 'HTML'),
    '.css': os.path.join('Developer', 'CSS')
}

def get_target_folder(filename: str) -> str:
    """
    Devuelve la ruta relativa de destino basada en la extensión.
    Ej: 'Documents/PDFs'
    """
    # 1. Separamos nombre y extensión
    _, extension = os.path.splitext(filename.lower())
    
    # 2. Buscamos en el mapa. 
    # Si no existe, lo mandamos a la carpeta 'Others' en la raíz.
    return EXTENSION_MAP.get(extension, "Others")