# Juego de Adivinanza de Animales 🐾

Un juego educativo y divertido construido con Python y Tkinter donde los jugadores intentan adivinar nombres de animales basándose en pistas.

## Descripción

El Juego de Adivinanza de Animales es un juego interactivo donde los jugadores deben adivinar nombres de animales letra por letra. Cada nivel proporciona una pista sobre el animal, y los jugadores tienen 5 vidas para adivinar la palabra correcta. El juego cuenta con un sistema de puntuación, múltiples niveles y seguimiento del rendimiento del jugador.

## Características

- 🎮 5 niveles desafiantes
- 💖 5 vidas por nivel
- 🏆 Sistema de puntuación
- 📝 Seguimiento del progreso del jugador
- 🎯 Sistema de pistas para cada animal
- 👥 Soporte para múltiples jugadores con historial de puntuación
- 🎨 Interfaz gráfica amigable construida con Tkinter

## Requisitos

- Python 3.x
- Tkinter (generalmente viene con Python)
- PIL (Biblioteca de Imágenes de Python)

```bash
pip install Pillow
```

## Instalación

1. Clona el repositorio o descarga el código fuente
2. Asegúrate de tener todas las dependencias requeridas instaladas
3. Coloca tu imagen de logo como "logo.jpg" en el mismo directorio que el script
4. Ejecuta el juego usando Python:

```bash
python juego-de-animales.py
```

## Cómo Jugar

1. Inicia el juego e ingresa tu nombre de usuario
2. Cada nivel presenta:
   - Una pista sobre el animal
   - Espacios en blanco que representan las letras del nombre del animal
   - 5 vidas (representadas por corazones)
3. Adivina una letra a la vez
4. Si la letra es correcta, aparecerá en su(s) posición(es) correcta(s)
5. Si la letra es incorrecta, perderás una vida
6. Completa los 5 niveles para ganar el juego

## Sistema de Puntuación

- Los puntos se otorgan según cuántos intentos necesites para adivinar la palabra
- Puntos máximos por nivel = (10 - intentos fallidos) × 10
- Los intentos fallidos reducen tus puntos potenciales
- Tu puntuación total es la suma de todas las puntuaciones de nivel
- Las puntuaciones se registran por usuario

## Interfaz del Juego

- Menú Principal:
  - Nuevo Juego
  - Instrucciones
  - Ver Puntuaciones
- Pantalla de Juego:
  - Nivel actual
  - Pista del animal
  - Visualización de palabra oculta
  - Vidas restantes
  - Campo de entrada de letras

## Controles del Juego

- Ingresa letras individuales usando el teclado
- Haz clic en el botón "Adivinar Letra" o presiona Enter para enviar
- Sigue las instrucciones en pantalla para la navegación

## Estructura de Archivos

- `juego-de-animales.py` - Archivo principal del juego
- `logo.jpg` - Imagen del logo del juego (requerida)

## Desarrollo

El juego está construido usando:
- `tkinter` para la interfaz gráfica
- `PIL` para el manejo de imágenes
- `random` para la selección de animales
- Clases personalizadas para la lógica del juego y gestión de la interfaz de usuario

## Base de Datos de Animales

El juego incluye una variedad de animales con sus respectivas pistas, incluyendo:
- Animales terrestres (león, caballo, cebra)
- Animales marinos (tiburón, ballena)
- Aves (águila, flamenco)
- Reptiles (serpiente, cocodrilo)
- Y muchos más...

## Posibles Mejoras Futuras

- Añadir más animales a la base de datos
- Añadir niveles de dificultad
- Incluir imágenes de los animales
- Modo multijugador en tiempo real

## Solución de Problemas

### Problemas Comunes

1. Si el logo no aparece:
   - Verifica que el archivo "logo.jpg" esté en el directorio correcto
   - Asegúrate de que el archivo sea una imagen válida

2. Si el juego no inicia:
   - Verifica que todas las dependencias estén instaladas
   - Confirma que estás usando una versión compatible de Python

## Autor

[Christian Renderos]



