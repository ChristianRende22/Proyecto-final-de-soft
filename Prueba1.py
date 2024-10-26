import tkinter as tk
import random

# Categorías, preguntas y pistas
categorias = {
    "Animales": [
        {"pregunta": "¿Cuál es el animal terrestre más rápido?", "respuesta": "Guepardo", "pistas": ["Vive en África", "Tiene manchas en su piel", "Es un felino"]},
        {"pregunta": "¿Cuál es el mamífero más grande?", "respuesta": "Ballena Azul", "pistas": ["Vive en el océano", "Se alimenta de krill", "Es azul"]},
        {"pregunta": "¿Cuál es el ave más grande?", "respuesta": "Avestruz", "pistas": ["No puede volar", "Tiene patas largas", "Pone los huevos más grandes"]},
        {"pregunta": "¿Cuál es el animal más venenoso?", "respuesta": "Rana dardo dorado", "pistas": ["Es muy pequeña", "Vive en selvas tropicales", "Su piel tiene toxinas"]},
        {"pregunta": "¿Cuál es el animal más pequeño?", "respuesta": "Ratón", "pistas": ["Es muy pequeño", "Vive en selvas tropicales", "Su piel tiene toxinas"]},
        {"pregunta": "¿Cuál es el animal más grande?", "respuesta": "Toro", "pistas": ["Es muy pequeño", "Vive en selvas tropicales", "Su piel tiene toxinas"]},
    ],
    "Números": [
        {"pregunta": "¿Cuál es el primer número primo?", "respuesta": "2", "pistas": ["Es el único número primo par", "Es menor que 3", "Es el primer número después del 1"]},
        {"pregunta": "¿Cuánto es 9 x 8?", "respuesta": "72", "pistas": ["Es un número compuesto", "Es el resultado de multiplicar dos números de un solo dígito", "Es mayor que 70"]},
        {"pregunta": "¿Cuál es el número de pi redondeado a dos decimales?", "respuesta": "3.14", "pistas": ["Es un número irracional", "Comienza con un 3", "Está relacionado con el círculo"]},
        {"pregunta": "¿Cuál es el resultado de 15 - 7?", "respuesta": "8", "pistas": ["Es un número menor que 10", "Es el doble de 4", "Es mayor que 7"]},
    ],
}

class JuegoAdivinanza(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Juego de Adivinanza")
        self.geometry("400x400")
        self.preguntas_ya_hechas = []
        self.preguntas_acertadas = []
        self.preguntas_incorrectas = []
        self.num_rondas = 0
        self.jugar_nuevo()

    def jugar_nuevo(self):
        if self.num_rondas == 10:
            self.mostrar_resultados()
            return

        self.num_rondas += 1
    
        
        # Seleccionar una pregunta que no haya sido hecha ya
        categoria = random.choice(list(categorias.keys()))
        preguntas_restantes = [p for p in categorias[categoria] if p not in self.preguntas_ya_hechas]
        
        if not preguntas_restantes:
            self.label_categoria.config(text="Todas las preguntas de esta categoría han sido respondidas.")
            return
        
        pregunta_dict = random.choice(preguntas_restantes)
        self.pregunta = pregunta_dict["pregunta"]
        self.respuesta_correcta = pregunta_dict["respuesta"]
        self.pistas = pregunta_dict["pistas"]
        self.pistas_mostradas = 0
        
        self.preguntas_ya_hechas.append(pregunta_dict)

        self.label_categoria = tk.Label(self, text=f"Categoría: {categoria}")
        self.label_categoria.pack(pady=10)
        
        self.label_pregunta = tk.Label(self, text=f"Pregunta: {self.pregunta}")
        self.label_pregunta.pack(pady=10)
        
        self.entry_respuesta = tk.Entry(self)
        self.entry_respuesta.pack(pady=10)
        
        self.button_enviar = tk.Button(self, text="Enviar", command=self.verificar_respuesta)
        self.button_enviar.pack(pady=10)
        
        self.button_pista = tk.Button(self, text="Mostrar pista", command=self.mostrar_pista)
        self.button_pista.pack(pady=10)
        
        self.label_pista = tk.Label(self, text="")
        self.label_pista.pack(pady=10)

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack(pady=10)
    
    def verificar_respuesta(self):
        respuesta_usuario = self.entry_respuesta.get()
        if respuesta_usuario.lower() == self.respuesta_correcta.lower():
            self.label_resultado.config(text="¡Correcto!")
            self.preguntas_acertadas.append(self.pregunta)
        else:
            self.label_resultado.config(text=f"Incorrecto. La respuesta correcta es {self.respuesta_correcta}")
            self.preguntas_incorrectas.append((self.pregunta, self.respuesta_correcta))

        # Limpiar la pantalla y generar nueva pregunta
        for widget in self.winfo_children():
            widget.destroy()
        self.jugar_nuevo()

    def mostrar_pista(self):
        if self.pistas_mostradas < len(self.pistas):
            self.label_pista.config(text=f"Pista: {self.pistas[self.pistas_mostradas]}")
            self.pistas_mostradas += 1
        else:
            self.label_pista.config(text="No hay más pistas disponibles")

    def mostrar_resultados(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        resultados_texto = "Preguntas acertadas:\n"
        for pregunta in self.preguntas_acertadas:
            resultados_texto += f"- {pregunta}\n"
        
        resultados_texto += "\nPreguntas incorrectas:\n"
        for pregunta, respuesta in self.preguntas_incorrectas:
            resultados_texto += f"- {pregunta} (Respuesta: {respuesta})\n"
        
        label_resultados = tk.Label(self, text=resultados_texto)
        label_resultados.pack(pady=10)

if __name__ == "__main__":
    app = JuegoAdivinanza()
    app.mainloop()