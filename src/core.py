import os

# Mapeo de Extensiones a Carpetas
# Mapping Extensions to Folders (English)
EXTENSION_MAP = {
    # IMAGES & DESIGN
    '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', 
    '.gif': 'Images', '.webp': 'Images', '.svg': 'Images',
    '.bmp': 'Images', '.tiff': 'Images', '.ico': 'Images',
    '.heic': 'Images', '.psd': 'Design', '.ai': 'Design',

    # DOCUMENTS
    '.pdf': 'Documents', '.txt': 'Documents', 
    '.doc': 'Documents', '.docx': 'Documents',
    '.xls': 'Spreadsheets', '.xlsx': 'Spreadsheets', '.csv': 'Spreadsheets',
    '.ppt': 'Presentations', '.pptx': 'Presentations',
    '.epub': 'Books', '.mobi': 'Books',

    # AUDIO & VIDEO
    '.mp3': 'Audio', '.wav': 'Audio', '.aac': 'Audio', '.flac': 'Audio',
    '.mp4': 'Video', '.mov': 'Video', '.avi': 'Video', 
    '.mkv': 'Video', '.flv': 'Video', '.wmv': 'Video',

    # ARCHIVES & INSTALLERS
    '.zip': 'Archives', '.rar': 'Archives', 
    '.7z': 'Archives', '.tar': 'Archives', '.gz': 'Archives',
    '.exe': 'Installers', '.msi': 'Installers', '.iso': 'Installers',

    # CODE & WEB
    '.py': 'Code', '.js': 'Code', '.html': 'Code', 
    '.css': 'Code', '.cpp': 'Code', '.java': 'Code',
    '.json': 'Code', '.sql': 'Code'
}


def get_target_folder(filename: str) -> str:

    _, extension = os.path.splitext(filename.lower())

    return EXTENSION_MAP.get(extension, "Others")


