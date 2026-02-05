import customtkinter as ctk
from tkinter import filedialog
import threading
import time
import os
import sys
import traceback

# --- BLOQUE DE IMPORTACIÓN ROBUSTA ---
# Esto asegura que encuentre 'organizer.py' sin importar desde dónde ejecutes
try:
    # Intento 1: Importación directa (si están en la misma carpeta)
    import organizer
except ImportError:
    try:
        # Intento 2: Importación como paquete (si ejecutas desde fuera de src)
        from src import organizer
    except ImportError:
        # Intento 3: Agregamos la carpeta actual al path de Python a la fuerza
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        try:
            import organizer
        except ImportError as e:
            print(
                f"❌ ERROR CRÍTICO: No encuentro el archivo organizer.py. Detalles: {e}"
            )
            organizer = None  # Marcamos como fallido


class ChaosApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de ventana
        self.title("Chaos Organizer Pro")
        self.geometry("800x650")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # INTENTA CARGAR EL ICONO
        # Usamos try/except para que no explote si por alguna razón no encuentra el archivo
        try:
            self.iconbitmap("icon.ico")
        except:
            pass  # Si falla, usa el default, pero no cierres la app

        # Variables de estado
        self.worker_thread = None
        self.organizing = False
        self.result_message = ""
        self.result_color = "white"
        self.current_folder = ""

        # --- ESTRUCTURA DE CENTRADO ---

        # 1. Creamos un "Marco Invisible" que siempre estará en el centro absoluto y se ajuste al tamaño de la ventana
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # --- WIDGETS (Ahora todos viven dentro de self.main_frame) ---

        # 2. Título
        self.label_title = ctk.CTkLabel(
            self.main_frame, text="Chaos Organizer 📂", font=("Roboto", 80, "bold")
        )
        self.label_title.pack(pady=(0, 10))  # Un poco de margen arriba

        # 3. Descripción
        self.label_desc = ctk.CTkLabel(
            self.main_frame,
            text="Selecciona una carpeta para organizar\ntus archivos automáticamente.",
            font=("Arial", 24),
        )
        self.label_desc.pack(pady=(0, 60))

        # 4. Botón Principal
        self.btn_action = ctk.CTkButton(
            self.main_frame,
            text="Seleccionar Carpeta",
            command=self.select_folder,
            height=60,
            font=("Arial", 24, "bold"),
        )
        self.btn_action.pack(pady=(60, 10))

        # 5. Barra de Progreso (Oculta)
        self.progress = ctk.CTkProgressBar(
            self.main_frame,
            width=400,
            height=20,
            corner_radius=10,
            progress_color="#00E676",
            mode="determinate",
        )
        self.progress.set(0)
        self.progress.pack_forget()

        # 6. Etiqueta de Estado
        self.label_status = ctk.CTkLabel(
            self.main_frame, text="Listo para trabajar", font=("Arial", 18)
        )
        self.label_status.pack(pady=10)

        # 7. Botón Abrir Carpeta (Oculto)
        self.btn_open = ctk.CTkButton(
            self.main_frame,
            text="📂 Abrir Carpeta Resultante",
            state="disabled",
            fg_color="gray",
            command=self.open_result_folder,
        )
        self.btn_open.pack_forget()

        # --- FOOTER (Este sí lo dejamos fuera para que se quede abajo del todo) ---
        self.footer = ctk.CTkLabel(
            self,
            text="Powered by Santi.Automata",
            font=("Arial", 10),
            text_color="gray",
        )
        self.footer.pack(side="bottom", pady=15)

    def select_folder(self):
        """Paso 1: Seleccionar carpeta e iniciar proceso"""

        # Verificación de seguridad antes de empezar
        if organizer is None:
            self.label_status.configure(
                text="Error: Falta organizer.py", text_color="red"
            )
            return

        folder_selected = filedialog.askdirectory()

        if not folder_selected:
            return  # Usuario canceló

        self.current_folder = folder_selected

        # --- RESETEAR UI ---
        self.btn_action.configure(state="disabled", text="Organizando...")
        self.btn_open.pack_forget()
        self.progress.pack(pady=20)
        self.progress.set(0)
        self.label_status.configure(text="Iniciando motores...", text_color="cyan")

        # Estado interno
        self.organizing = True
        self.result_message = ""

        # --- LANZAR HILO (THREAD) ---
        # Daemon=True asegura que si cierras la ventana, el hilo se muere y no queda zombie
        self.worker_thread = threading.Thread(
            target=self.run_logic_in_background, args=(folder_selected,), daemon=True
        )
        self.worker_thread.start()

        # --- INICIAR MONITOR ---
        self.monitor_process()

    def run_logic_in_background(self, folder_path):
        """Paso 2: Lógica pesada (NO TOCAR UI AQUÍ)"""
        try:
            print(f"🔧 HILO: Iniciando organización en {folder_path}")

            # Verificamos que la función exista
            if hasattr(organizer, "organize_directory"):
                organizer.organize_directory(folder_path)
            else:
                raise AttributeError(
                    "La función 'organize_directory' no existe en organizer.py"
                )

            # Si llega aquí, todo salió bien
            self.result_message = "¡Organización Exitosa! 🚀"
            self.result_color = "#00E676"  # Verde

        except Exception as e:
            # Capturamos error
            error_text = str(e)
            print(f"❌ ERROR EN HILO: {traceback.format_exc()}")
            self.result_message = f"Error: {error_text}"
            self.result_color = "#FF5252"  # Rojo

        finally:
            # Avisamos que el hilo terminó
            self.organizing = False

    def monitor_process(self):
        """Paso 3: Actualizar UI constantemente"""

        if self.organizing:
            # A) Si sigue trabajando
            current_val = self.progress.get()

            # Truco de animación: Subir hasta 90% lento
            if current_val < 0.90:
                self.progress.set(current_val + 0.005)

            # Volver a chequear en 50ms
            self.after(50, self.monitor_process)

        else:
            # B) Si terminó (Variable organizing es False)
            self.label_status.configure(
                text=self.result_message, text_color=self.result_color
            )

            if "Error" in self.result_message:
                self.progress.set(0)  # Vaciar barra si falló
            else:
                self.progress.set(1)  # Llenar barra si tuvo éxito
                # Mostrar botón para abrir carpeta
                self.btn_open.configure(
                    state="normal",
                    fg_color="#00E676",
                    text_color="black",
                    hover_color="#00C853",
                )
                self.btn_open.pack(pady=10)

            # Reactivar botón principal
            self.btn_action.configure(state="normal", text="Seleccionar otra carpeta")

    def open_result_folder(self):
        """Abrir carpeta en Windows"""
        if self.current_folder:
            try:
                os.startfile(self.current_folder)
            except Exception as e:
                print(f"No se pudo abrir: {e}")


# Código para ejecutar la app si se llama directamente
if __name__ == "__main__":
    app = ChaosApp()
    app.mainloop()
