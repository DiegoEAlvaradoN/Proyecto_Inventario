print()
print("Proyecto Inventario Avance 6")

# Listas de los productos que se venden
productos = ["Computadora", "Telefono", "Raton", "Teclado", "Monitor", "Audifonos"]
precios = [15000, 8000, 800, 1200, 3000, 950]
cantidades = [10, 10, 10, 10, 10, 10]
stock_minimo = [3, 3, 3, 3, 3, 3]
comprados = [0, 0, 0, 0, 0, 0]
ingresos = [0, 0, 0, 0, 0, 0]

# Funcion para comprar un producto,mostrar el precio, revisar el stock, aplicar descuentos y calcular los ingresos
def comproducto(numero):

    # Si se quiere seguir comprando el ciclo se repite
    continuar = "si"
    while continuar == "si":

        # Datos del producto seleccionado de las listas
        print()
        print("Producto: ", productos[numero])
        print("Precio: ", precios[numero])
        print("Cantidad disponible: ", cantidades[numero])

        # Revisa si ya no quedan productos
        if cantidades[numero] == 0:
            print()
            print("------ Ya no hay ------")
            print()

            # Pregunta para agregar mas productos
            agregarmas = input("Quieres reabastecer este producto? (si o no): ")
            if agregarmas == "si":

                # Pide la cantidad que se quiere agregar
                nuevas = int(input("------ Cuantas unidades quieres agregar?: "))

                # Suma lo nuevo al inventario
                if nuevas > 0:
                    cantidades[numero] = cantidades[numero] + nuevas
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
        total = precios[numero] * cantidades[numero]
        print("Total inventario: ", total)

        # Pregunta cuantas unidades se quieren comprar
        print()
        venta = int(input("------ Cuantos compras?: "))

        # Revisa si se quieren comprar mas unidades de las disponibles
        if venta > cantidades[numero]:
            print()
            print("------ No hay suficientes unidades ------")

        # Revisa si la cantidad es menor o igual a cero
        elif venta <= 0:
            print()
            print("------ Eso no es una cantidad valida ------")

        # Si la cantidad es valida se realiza la compra
        else:

            # Calcula el precio de las cosas compradas
            costoff = precios[numero] * venta

            # Si compra 5 o mas unidades se aplica un descuento del 10%
            if venta >= 5:
                descuento = (costoff / 100) * 10
                costoff = costoff - descuento
                print()
                print("------ Tienes descuento por comprar 5+ ------")
                print("------ Descuento aplicado: ", descuento, " ------")
                print()

            # Elimina del inventario la cantidad comprada
            cantidades[numero] = cantidades[numero] - venta

            # Suma las unidades vendidas en la lista
            comprados[numero] = comprados[numero] + venta

            # Suma el dinero obtenido por la venta en la lista
            ingresos[numero] = ingresos[numero] + costoff

            # Muestra las unidades que quedan
            print("------ Unidades restantes: ", cantidades[numero])

            # Muestra el precio de la compra
            print("------ Subtotal de esta compra: ", costoff)

            # Si ya no quedan unidades se termina la funcion
            if cantidades[numero] == 0:
                print()
                print("------ Ya no hay ------")
                return

            # Revisa si quedan pocas unidades
            if cantidades[numero] <= stock_minimo[numero]:
                print()
                print("------ Quedan pocos ------")

            # Pregunta si el cliente quiere seguir comprando
            print()
            continuar = input("Quieres seguir comprando? (si o no): ")
            if continuar == "no":
                return
            elif continuar != "si":
                print()
                print("------ Eso es un no ------")
                return

# Funcion para mostrar todos los productos del inventario
def mostrar_inventario():
    print()
    print("========== INVENTARIO ==========")

    # Recorre las listas para mostrar cada producto
    for i in range(6):
        print()
        print("Producto: ", productos[i])
        print("Precio: ", precios[i])
        print("Cantidad disponible: ", cantidades[i])

        # Calcula el valor de cada producto en el inventario
        total = precios[i] * cantidades[i]
        print("Valor del inventario: ", total)

        # Revisa si quedan pocos productos
        if cantidades[i] == 0:
            print("------ Agotado ------")
        elif cantidades[i] <= stock_minimo[i]:
            print("------ Quedan pocos ------")

# Funcion para mostrar las ventas e ingresos
def reporte():
    print()
    print("========== REPORTE ==========")

    # Recorre las listas para mostrar las ventas de cada producto
    for i in range(6):
        print()
        print("Producto: ", productos[i])
        print("Unidades vendidas: ", comprados[i])
        print("Ingreso: ", ingresos[i])

    # Calcula los ingresos totales de la tienda
    ingreso_total = 0
    for i in range(6):
        ingreso_total = ingreso_total + ingresos[i]
    print()
    print("Ingreso total de la tienda: ", ingreso_total)

# Funcion que muestra el menu principal y permite elegir un producto
def menu():

    # Guarda la opcion que eligieron
    opcion = ""

    # El menu se repite hasta que el usuario decida salir
    while opcion != "9":
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
        print("9. Salir")

        # Pide una opcion
        print()
        opcion = input("Que quieres hacer?: ")

        # Compra de cada producto usando su posicion en las listas
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

        # Opcion para salir
        elif opcion == "9":
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
    print(productos[i], ": ", comprados[i])

# Muestra los ingresos obtenidos por cada producto
print()
print("========== INGRESOS ==========")
for i in range(6):
    print(productos[i], ": ", ingresos[i])

# Calcula el ingreso total de todos los productos
ingreso_total = 0
for i in range(6):
    ingreso_total = ingreso_total + ingresos[i]

# Muestra el ingreso total
print("Ingreso total: ", ingreso_total)
