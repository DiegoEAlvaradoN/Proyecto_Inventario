print()
print("Proyecto Inventario Avance 8")

# Matriz del inventario: cada fila es un producto
# Columnas: 0 = nombre, 1 = precio, 2 = cantidad, 3 = stock minimo, 4 = comprados, 5 = ingresos
# Los nombres se guardan en minusculas ya luego capitalize() los muestra bien
inventario = [
    ["computadora", 15000, 10, 3, 0, 0],
    ["telefono", 8000, 10, 3, 0, 0],
    ["raton", 800, 10, 3, 0, 0],
    ["teclado", 1200, 10, 3, 0, 0],
    ["monitor", 3000, 10, 3, 0, 0],
    ["audifonos", 950, 10, 3, 0, 0]
]

# Matriz del historial de compras, empieza vacia y cada compra agrega una fila
# Columnas: 0 = producto, 1 = unidades, 2 = subtotal
historial = []

# Funcion para comprar un producto,mostrar el precio, revisar el stock, aplicar descuentos y calcular los ingresos
def comproducto(numero):

    # Si se quiere seguir comprando el ciclo se repite
    continuar = "SI"
    while continuar == "SI":

        # Datos del producto seleccionado de la matriz (capitalize deja la primera letra en mayuscula)
        print()
        print("Producto: ", inventario[numero][0].capitalize())
        print("Precio: ", inventario[numero][1])
        print("Cantidad disponible: ", inventario[numero][2])

        # Revisa si ya no quedan productos
        if inventario[numero][2] == 0:
            print()
            print("------ Ya no hay ------")
            print()

            # Pregunta para agregar mas productos
            agregarmas = input("Quieres reabastecer este producto? (si o no): ").strip().upper()
            if agregarmas == "SI":

                # Pide la cantidad que se quiere agregar
                nuevas = int(input("------ Cuantas unidades quieres agregar?: "))

                # Suma lo nuevo al inventario
                if nuevas > 0:
                    inventario[numero][2] = inventario[numero][2] + nuevas
                    print()
                    print("------ Stock actualizado ------")
                    print()
                else:
                    print()
                    print("------ Cantidad no valida ------")
                    return
            else:
                return

        # Calcula el valor total del inventario disponible
        total = inventario[numero][1] * inventario[numero][2]
        print("Total inventario: ", total)

        # Pregunta cuantas unidades se quieren comprar
        print()
        venta = int(input("------ Cuantos compras?: "))

        # Revisa si se quieren comprar mas unidades de las disponibles
        if venta > inventario[numero][2]:
            print()
            print("------ No hay suficientes unidades ------")

        # Revisa si la cantidad es menor o igual a cero
        elif venta <= 0:
            print()
            print("------ Eso no es una cantidad valida ------")

        # Si la cantidad es valida se realiza la compra
        else:

            # Calcula el precio de las cosas compradas
            costoff = inventario[numero][1] * venta

            # Si compra 5 o mas unidades se aplica un descuento del 10%
            if venta >= 5:
                descuento = (costoff / 100) * 10
                costoff = costoff - descuento
                print()
                print("------ Tienes descuento por comprar 5+ ------")
                print("------ Descuento aplicado: ", descuento, " ------")
                print()

            # Elimina del inventario la cantidad comprada
            inventario[numero][2] = inventario[numero][2] - venta

            # Suma las unidades vendidas
            inventario[numero][4] = inventario[numero][4] + venta

            # Suma el dinero obtenido por la venta
            inventario[numero][5] = inventario[numero][5] + costoff

            # Agrega una fila nueva al historial con esta compra
            historial.append([inventario[numero][0], venta, costoff])

            # Muestra las unidades que quedan
            print("------ Unidades restantes: ", inventario[numero][2])

            # Muestra el precio de la compra
            print("------ Subtotal de esta compra: ", costoff)

            # Si ya no quedan unidades se termina la funcion
            if inventario[numero][2] == 0:
                print()
                print("------ Ya no hay ------")
                return

            # Revisa si quedan pocas unidades
            if inventario[numero][2] <= inventario[numero][3]:
                print()
                print("------ Quedan pocos ------")

            # Pregunta si el cliente quiere seguir comprando
            print()
            continuar = input("Quieres seguir comprando? (si o no): ").strip().upper()
            if continuar == "NO":
                return
            elif continuar != "SI":
                print()
                print("------ Eso es un no ------")
                return

# Funcion para mostrar todos los productos del inventario
def mostrar_inventario():
    print()
    print("========== INVENTARIO ==========")

    # Recorre las filas de la matriz para mostrar cada producto
    for i in range(6):
        print()
        print("Producto: ", inventario[i][0].capitalize())
        print("Precio: ", inventario[i][1])
        print("Cantidad disponible: ", inventario[i][2])

        # Calcula el valor de cada producto en el inventario
        total = inventario[i][1] * inventario[i][2]
        print("Valor del inventario: ", total)

        # Revisa si quedan pocos productos
        if inventario[i][2] == 0:
            print("------ Agotado ------")
        elif inventario[i][2] <= inventario[i][3]:
            print("------ Quedan pocos ------")

# Funcion para buscar un producto por su nombre
def buscar_producto():
    print()
    print("========== BUSCAR PRODUCTO ==========")

    # Pide el nombre 
    print()
    texto = input("Que producto buscas?: ").strip().lower()

    # Si no se escribe nada no se busca
    if texto == "":
        print()
        print("------ Nada entonces ------")
        return

    # Guarda si se encontro algun producto
    encontrado = False

    # Recorre las filas de la matriz y busca el texto dentro del nombre
    for i in range(6):

        # regresa -1 cuando el texto no esta dentro del nombre
        if inventario[i][0].find(texto) != -1:
            encontrado = True
            print()
            print("Producto: ", inventario[i][0].capitalize())
            print("Precio: ", inventario[i][1])
            print("Cantidad disponible: ", inventario[i][2])

    # Si ningun producto coincidio
    if encontrado == False:
        print()
        print("------ No hay ese producto ------")

# Funcion para mostrar las ventas e ingresos
def reporte():
    print()
    print("========== REPORTE ==========")

    # Recorre las filas de la matriz para mostrar las ventas de cada producto
    for i in range(6):
        print()
        print("Producto: ", inventario[i][0].capitalize())
        print("Unidades vendidas: ", inventario[i][4])
        print("Ingreso: ", inventario[i][5])

    # Calcula los ingresos totales de la tienda
    ingreso_total = 0
    for i in range(6):
        ingreso_total = ingreso_total + inventario[i][5]
    print()
    print("Ingreso total de la tienda: ", ingreso_total)

# Funcion para mostrar el historial de compras (recorre la matriz con dos ciclos)
def mostrar_historial():
    print()
    print("========== HISTORIAL ==========")

    # Si no hay compras todavia
    if len(historial) == 0:
        print()
        print("------ Todavia no hay compras ------")
        return

    # Ciclo de afuera: recorre cada fila (cada compra)
    for i in range(len(historial)):
        print()
        print("Compra numero: ", i + 1)

        # Ciclo de adentro: recorre cada columna de esa compra
        for j in range(3):
            if j == 0:
                print("Producto: ", historial[i][j].capitalize())
            elif j == 1:
                print("Unidades: ", historial[i][j])
            else:
                print("Subtotal: ", historial[i][j])

    # Suma la columna de subtotales
    suma = 0
    for i in range(len(historial)):
        suma = suma + historial[i][2]
    print()
    print("Total de todas las compras: ", suma)

# Funcion que muestra el menu principal y permite elegir un producto
def menu():

    # Guarda la opcion que eligieron
    opcion = ""

    # El menu se repite hasta que el usuario decida salir
    while opcion != "11":
        print()
        print("========== MENU ==========")
        print("1. Comprar computadora")
        print("2. Comprar telefono")
        print("3. Comprar raton")
        print("4. Comprar teclado")
        print("5. Comprar monitor")
        print("6. Comprar audifonos")
        print("7. Ver reporte")
        print("8. Ver inventario")
        print("9. Ver historial de compras")
        print("10. Buscar producto")
        print("11. Salir")

        # Pide una opcion 
        print()
        opcion = input("Que quieres hacer?: ").strip()

        # Compra de cada producto usando su fila en la matriz
        if opcion == "1":
            comproducto(0)
        elif opcion == "2":
            comproducto(1)
        elif opcion == "3":
            comproducto(2)
        elif opcion == "4":
            comproducto(3)
        elif opcion == "5":
            comproducto(4)
        elif opcion == "6":
            comproducto(5)

        # Muestra el reporte
        elif opcion == "7":
            reporte()

        # Muestra el inventario
        elif opcion == "8":
            mostrar_inventario()

        # Muestra el historial
        elif opcion == "9":
            mostrar_historial()

        # Busca un producto por su nombre
        elif opcion == "10":
            buscar_producto()

        # Opcion para salir
        elif opcion == "11":
            print()
            print("------ Gracias por usar el inventario ------")

        # Por si se escribe una opcion que no existe
        else:
            print()
            print("------ Esa opcion no existe ------")

# Llama a la funcion del menu
menu()

# Muestra la cantidad total vendida de cada producto
print()
print("========== COMPRA FINAL ==========")
for i in range(6):
    print(inventario[i][0].capitalize(), ": ", inventario[i][4])

# Muestra los ingresos obtenidos por cada producto
print()
print("========== INGRESOS ==========")
for i in range(6):
    print(inventario[i][0].capitalize(), ": ", inventario[i][5])

# Calcula el ingreso total de todos los productos
ingreso_total = 0
for i in range(6):
    ingreso_total = ingreso_total + inventario[i][5]

# Muestra el ingreso total
print("Ingreso total: ", ingreso_total)

# Muestra el ingreso total
print("Ingreso total: ", ingreso_total)
