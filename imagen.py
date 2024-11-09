import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Mostrar imagen sin borde")
root.configure(bg="lightblue")  # Cambia el color de fondo de la ventana si es necesario

# Cargar la imagen usando PIL
imagen = Image.open("Logofinal2.jpg")  # Reemplaza con la ruta de tu imagen si es necesario
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget de etiqueta para mostrar la imagen y configurarle el mismo fondo que la ventana
label_imagen = tk.Label(root, image=imagen_tk, bg="lightblue")  # Cambia el color de fondo si lo necesitas
label_imagen.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
