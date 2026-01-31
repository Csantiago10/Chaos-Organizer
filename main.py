from src import organizer

if __name__ == "__main__":
    # Pedir al usuario que ingrese la ruta de la carpeta a organizar
    user_input = input("Ingresa la ruta de la carpeta a organizar: ")
    organizer.organize_directory(user_input)