
import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageTk


# Diccionario de animales en tuplas
ANIMALES = [
    ('Leon', 'Depredador de la sabana.'),
    ('Caballo', 'Animal Equino.'),
    ('Tiburon', 'Depredador marino.'),
    ('Cebra', 'Animal rayado.'),
    ('Ajolote', 'Animal acuático endemico de Mexico.'),
    ('Camello', 'Animal jorobado.'),
    ('Gato', 'Mascota independiente.'),
    ('Serpiente', 'Reptil sin patas.'),
    ('Cocodrilo', 'Reptil que vive en ríos.'),
    ('Perro', 'El mejor amigo del hombre.'),
    ('Pinguino', 'Animal con traje.'),
    ('Ballena', 'Mamífero marino que canta.'),
    ('Elefante', 'Mamífero que jamás olvida.'),
    ('Lobo', 'Canino que caza en manada.'),
    ('Tortuga', 'Reptil acorazado.'),
    ('Tigre', 'Felino de gran tamaño.'),
    ('Capibara', 'Amigo de todos.'),
    ('Canguro', 'Animal boxeador.'),
    ('Aguila', 'Ave rapaz con vista aguda y gran cazadora.'),
    ('Murcielago', 'Mamífero volador.'),
    ('Morsa','Con colmillos prominentes y vive en aguas frías.'),
    ('Flamenco', 'Rosa por su dieta de crustáceos.'),
    ('Halcon','Velocidad y habilidad de caza en vuelo.'),
    ('Rinoceronte','Gran tamaño y piel gruesa.')
    
]


# crear clase para el juego de adivinanza de animales

class AdivinaElAnimal:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Adivinnza dea Animales")
        self.root.geometry("1024x768")
        self.root.configure(bg="SteelBlue4")
        self.usuario = ""
        self.nivel_actual = 0
        self.puntaje_total = 0
        self.palabras_usadas = []
        self.vidas = 5 
        self.palabra_actual = ""
        self.pista_actual = ""
        self.palabra_oculta = []
        self.intentos_fallidos = 0
        self.puntajes_usuarios = {}
        
       # Cambia los valores para el tamaño deseado

##############################################################################################################################
# Aqui se crea la clase, las funcion inicial del juego, y se crea las variables usadas dentro del juego dentro de la clase ###
##############################################################################################################################
##############################################################################################################################
# crear funcion para crear interfaz inicio
        self.crear_interfaz_inicio()
# crear interfaz inicio
    def crear_interfaz_inicio(self):

        for widget in self.root.winfo_children():
            widget.destroy()

                
        main_frame = tk.Frame(self.root, bg="steelblue4")
        main_frame.pack(expand=True, fill='both')

        # Frame para el logo con fondo celeste
        logo_frame = tk.Frame(main_frame, bg="steelblue4")
        logo_frame.pack(pady=(20, 0))  # Espacio arriba del logo

        try:
            logo_image = Image.open("logo.jpg")
            logo_image = logo_image.resize((300, 150))
            self.logo_tk = ImageTk.PhotoImage(logo_image)
            logo_label = tk.Label(logo_frame, 
                                image=self.logo_tk,
                                bg="steelblue4")
            logo_label.pack(padx=20, pady=20)
        except:
            print("No se pudo cargar el logo")

# crear etiqueta para ingresar nombre de usuario
        self.frame_inicio = tk.Frame(self.root,
                                     bg="SteelBlue4",
                                     width=500, 
                                     height=500)
        self.frame_inicio.place(relx=0.5, rely=0.5, anchor='center') 
        tk.Label(self.frame_inicio, 
                 text="Ingrese su nombre:", 
                 bg="cyan4",
                 border=4,
                 font=("Times New Roman", 12),
                 width=30).pack(pady=10)
        self.entry_usuario = tk.Entry(self.frame_inicio,
                                      background="LightSteelBlue1",
                                      border=4 ,
                                      foreground="black", 
                                      width=30, 
                                      font=("Times New Roman", 12))
        
        self.entry_usuario.pack(pady=10)
# crear boton para comenzar nuevo juego
        btn_nuevo_juego = tk.Button(self.frame_inicio, 
                                    text=" Nuevo Juego", 
                                    command=self.nuevo_juego, 
                                    border=4, 
                                    width=30 ) 
        btn_nuevo_juego.pack(pady=10)
# crear boton para mostrar instrucciones
        btn_instrucciones = tk.Button(self.frame_inicio, 
                                      text="Instrucciones", 
                                      command=self.mostrar_instrucciones, 
                                      border=4, 
                                      width=30)
        btn_instrucciones.pack(pady=10)

# crear boton para ver puntuacion
        btn_puntuacion = tk.Button(self.frame_inicio, 
                                   text="Ver Puntuación", 
                                   command=self.mostrar_puntuacion, 
                                   border=4,
                                   width=30)
        btn_puntuacion.pack(pady=10)
        


# crear funcion para mostrar instrucciones
    def mostrar_instrucciones(self):

        messagebox.showinfo("Instrucciones", "Adivina el animal letra por letra. Tienes 5 vidas por palabra.")
# crear funcion para mostrar puntuacion
    def mostrar_puntuacion(self):
        puntuacion_texto = "Puntuación de usuarios:\n"
        if self.puntajes_usuarios:
            for usuario, puntajes in self.puntajes_usuarios.items():
                puntuacion_texto += f"\nUsuario: {usuario}\n"
                puntuacion_texto += "Puntuación por nivel:\n"
                for i, puntaje in enumerate(puntajes["niveles"], 1):
                    puntuacion_texto += f"Nivel {i}: {puntaje} puntos\n"
                puntuacion_texto += f"Puntuación total: {puntajes['total']} puntos\n"
        else:
            puntuacion_texto += (f"perdon no hay puntuaciones registradas aún.")

        messagebox.showinfo("Puntuación", puntuacion_texto)
# crear funcion para comenzar nuevo juego
    def nuevo_juego(self):
        self.usuario = self.entry_usuario.get()
        if self.usuario:
            self.mostrar_instrucciones()
            self.nivel_actual = 1
            self.puntaje_total = 0
            self.palabras_usadas = []
            self.vidas = 5
            self.intentos_fallidos = 0
            self.frame_inicio.pack_forget()
            self.jugar_nivel()

# verificar si el usuario ingresado ya existe en la lista de usuarios
            if self.usuario not in self.puntajes_usuarios:
                self.puntajes_usuarios[self.usuario] = {"niveles": [], "total": 0}
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre de usuario.")
# crear funcion para jugar nivel
    def jugar_nivel(self):

        if self.nivel_actual <= 5:
            self.palabra_actual, self.pista_actual = random.choice(
                [p for p in ANIMALES if p[0] not in self.palabras_usadas])
            self.palabras_usadas.append(self.palabra_actual)
            self.palabra_oculta = ["_" for _ in self.palabra_actual]
            self.vidas = 5
            self.crear_interfaz_juego()
        else:
            messagebox.showinfo("Juego Terminado", f"¡Felicidades {self.usuario}! Has completado el juego.")
            self.regresar_inicio()
# crear funcion para crear interfaz juego
    def crear_interfaz_juego(self):

        self.frame_juego = tk.Frame(self.root,
                                    bg="steelblue4" ,
                                    width=500, 
                                    height=500,
                                    padx=50, 
                                    pady=70)
        self.frame_juego.place(relx=0.5, rely=0.6, anchor='center') 
# crear etiqueta para mostrar nivel y pista
        tk.Label(self.frame_juego, text=f"Nivel {self.nivel_actual}",
                background="lightblue1",
                border=4,
                foreground="black", 
                width=50, 
                font=("Times New Roman", 11)
                 ).pack(pady=20)
        tk.Label(self.frame_juego, text=f"Pista: {self.pista_actual}",
                background="lightblue1",
                border=4,
                foreground="black", 
                width=50, 
                font=("Times New Roman", 11)
                 ).pack(pady=20)
        self.lbl_palabra_oculta = tk.Label(self.frame_juego, text=' '.join(self.palabra_oculta) ,
                                           background="seagreen1",
                                           border=4 ,
                                           foreground="black", 
                                           width=50, 
                                           font=("Times New Roman", 11))
        self.lbl_palabra_oculta.pack(pady=20)

# crear etiqueta para mostrar vidas restantes
        self.lbl_vidas = tk.Label(self.frame_juego, text=f"Vidas restantes: {self.vidas}",
                                  background="lightblue1",
                                  border=4,
                                  foreground="black", 
                                  width=50, 
                                  font=("Times New Roman", 11))
        self.lbl_vidas.pack(pady=20)

        self.entry_letra = tk.Entry(self.frame_juego,
                                    background="lightblue1",
                                    border=4,
                                    foreground="black", 
                                    width=50, 
                                    font=("Times New Roman", 11))
        self.entry_letra.pack(pady=20, 
                              padx=50, 
                              )
# crear etiqueta para ingresar letra
        btn_adivinar = tk.Button(self.frame_juego, text="Adivinar Letra", command=self.adivinar_letra,
                                 border=4,
                                 foreground="black", 
                                 width=50, 
                                 font=("Times New Roman", 11),
                                )
        btn_adivinar.pack(pady=20)
# crear funcion para adivinar letra
    def adivinar_letra(self):
        letra = self.entry_letra.get().upper()

# verificar si la letra ingresada es correcta
        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Advertencia", "Por favor, ingresa solo una letra.")
            self.entry_letra.delete(0, tk.END)
            return

# borrar letra ingresada
        self.entry_letra.delete(0, tk.END)

        if letra in self.palabra_actual.upper():
            self.actualizar_palabra_oculta(letra)
        else:
            self.intentos_fallidos += 1
            self.vidas -= 1


        self.lbl_vidas.config(text=f"Vidas restantes: {self.vidas}")
# verificar si la letra es correcta
        if "_" not in self.palabra_oculta:
            messagebox.showinfo(f"Correcto {self.usuario}", "¡Has adivinado la palabra!")
            puntaje_nivel = (10 - self.intentos_fallidos) * 10
            self.puntajes_usuarios[self.usuario]["niveles"].append(puntaje_nivel)
            self.puntajes_usuarios[self.usuario]["total"] += puntaje_nivel
            self.nivel_actual += 1
            self.frame_juego.pack_forget()
            self.jugar_nivel()
        elif self.vidas == 0:
            messagebox.showinfo(f"Perdiste {self.usuario}", "¡Te has quedado sin vidas!")
            self.puntajes_usuarios[self.usuario]["niveles"].append(0)
            self.frame_juego.pack_forget()
            self.regresar_inicio()
# actualizar palabra oculta
    def actualizar_palabra_oculta(self, letra):
        for idx, char in enumerate(self.palabra_actual.upper()):
            if char == letra:
                self.palabra_oculta[idx] = letra
        self.lbl_palabra_oculta.config(text=' '.join(self.palabra_oculta))
# regresar al inicio
    def regresar_inicio(self):

        messagebox.showinfo("Juego Terminado", f"Juego terminado, regresando al menú de inicio")
        self.crear_interfaz_inicio()
    

# ejecutar el juego
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaElAnimal(root) 
    root.mainloop()






