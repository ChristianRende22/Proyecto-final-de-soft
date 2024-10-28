# Definición de las listas
ExtraJumbo = [25,30,27,28,14,35,40,50,10,60,40,29]
Jumbo = [35,50,47,55,52,24,59,42,79,12,81,25]
Grande = [28,39,67,81,60,14,88,65,58,14,46,19]
Meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
Medidas = ["ExtraJumbo","Jumbo","Grande"]
PreciosCarton = [6.00,5.75,4.85]

# Obtener el mes actual
mes_valido = False
while mes_valido == False:
    print("\nMeses disponibles:")
    for i, mes in enumerate(Meses):
        print(f"{i+1}. {mes}")
    
    mes_seleccionado = input("\nSeleccione el número del mes (1-12): ")
    if mes_seleccionado.isdigit():
        mes_seleccionado = int(mes_seleccionado) - 1
        if 0 <= mes_seleccionado <= 11:
            mes_valido = True
        else:
            print("Por favor, seleccione un número entre 1 y 12")
    else:
        print("Por favor, ingrese un número válido")

# Mostrar medidas disponibles
print("\nMedidas disponibles:")
for i, medida in enumerate(Medidas):
    print(f"{i+1}. {medida} - Precio: ${PreciosCarton[i]:.2f}")

# Solicitar medida
medida_valida = False
while medida_valida == False:
    medida_seleccionada = input("\nSeleccione el número de la medida (1-3): ")
    if medida_seleccionada.isdigit():
        medida_seleccionada = int(medida_seleccionada) - 1
        if 0 <= medida_seleccionada <= 2:
            medida_valida = True
        else:
            print("Por favor, seleccione un número entre 1 y 3")
    else:
        print("Por favor, ingrese un número válido")

# Solicitar cantidad de cartones
cantidad_valida = False
while cantidad_valida == False:
    cantidad = input("\nIngrese la cantidad de cartones que desea: ")
    if cantidad.isdigit():
        cantidad = int(cantidad)
        if cantidad > 0:
            cantidad_valida = True
        else:
            print("Por favor, ingrese una cantidad mayor a 0")
    else:
        print("Por favor, ingrese un número válido")

# Verificar inventario disponible según la medida seleccionada
if medida_seleccionada == 0:
    inventario_disponible = ExtraJumbo[mes_seleccionado]
    precio_unitario = PreciosCarton[0]
elif medida_seleccionada == 1:
    inventario_disponible = Jumbo[mes_seleccionado]
    precio_unitario = PreciosCarton[1]
else:
    inventario_disponible = Grande[mes_seleccionado]
    precio_unitario = PreciosCarton[2]

# Verificar disponibilidad y mostrar resultado
if cantidad <= inventario_disponible:
    total = cantidad * precio_unitario
    
    print("\n=== RESUMEN DEL PEDIDO ===")
    print(f"Mes: {Meses[mes_seleccionado]}")
    print(f"Medida: {Medidas[medida_seleccionada]}")
    print(f"Cantidad: {cantidad} cartones")
    print(f"Precio por cartón: ${precio_unitario:.2f}")
    print(f"Total a pagar: ${total:.2f}")
    print(f"Inventario restante: {inventario_disponible - cantidad}")
    print("======================")
else:
    print(f"\nLo sentimos, no hay suficiente inventario.")
    print(f"Inventario disponible: {inventario_disponible} cartones")
    print(f"Cantidad solicitada: {cantidad} cartones")