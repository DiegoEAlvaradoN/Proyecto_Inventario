print("Proyecto Inventario Avance 5")
print()

"""Datos de los productos que se venden"""
producto = "Computadora"
precio = 15000
cantidad = 10
stock_minimo = 3
comprado = 0
ingreso = 0

producto2 = "Telefono"
precio2 = 8000
cantidad2 = 10
stock_minimo2 = 3
comprado2 = 0
ingreso2 = 0

producto3 = "Raton"
precio3 = 800
cantidad3 = 10
stock_minimo3 = 3
comprado3 = 0
ingreso3 = 0

producto4 = "Teclado"
precio4 = 1200
cantidad4 = 10
stock_minimo4 = 3
comprado4 = 0
ingreso4 = 0

producto5 = "Monitor"
precio5 = 3000
cantidad5 = 10
stock_minimo5 = 3
comprado5 = 0
ingreso5 = 0

producto6 = "Audifonos"
precio6 = 950
cantidad6 = 10
stock_minimo6 = 3
comprado6 = 0
ingreso6 = 0

"""Funcion para comprar un producto, su precio, revisar el stock que queda, aplicar descuentos mediante la cantidad comprada y calcular los ingresos"""
def comproducto(producto, precio, cantidad, stock_minimo, comprado, ingreso):

    """Si se quiere seguir comprando el ciclo se repite"""
    continuar = "si"
    while continuar == "si":

        """Datos del producto"""
        print()
        print("Producto: ", producto)
        print("Precio: ", precio)
        print("Cantidad disponible: ", cantidad)

        """Cantidad de productos"""
        if cantidad == 0:
            print("------ Ya no hay ------")

            """Pregunta para agregar mas productos"""
            agregarmas = input("Quieres reabastecer este producto? (si o no): ")

            if agregarmas == "si":
                
                """Si si, pide la cantidad que se quiere agregar"""
                nuevas = int(input("------ Cuantas unidades quieres agregar?: "))

                """Suma lo nuevo agregado al inventario"""
                cantidad = cantidad + nuevas
                print("------ Stock ------")
            else:
                
                """Si no se quiere agregar cosas termina la funcion"""
                return cantidad, comprado, ingreso

        """Calcula el valor total del inventario disponible"""
        total = precio * cantidad
        print("Total inventario: ", total)

        """Pregunta cuantas unidades del producto qieres comprar"""
        venta = int(input("------ Cuantos compras?: "))

        """Revisa si quieres comprar mas unidades de las disponibles"""
        if venta > cantidad:
            print("------ No hay suficientes unidades ------")

        """Revisa si la cantidad es menor o igual a cero"""
        elif venta <= 0:
            print("------ Eso no es una cantidad valida  ------")

        """Si la cantidad es valida se realiza la compra"""
        else:
            
            """Calcula el precio de las coss compradas"""
            costoff = precio * venta

            """Si compra 5 o mas unidades se aplica un descuento del 10%"""
            if venta >= 5:
                descuento = (costoff / 100) * 10
                costoff = costoff - descuento
                print("------ Tienes descuento por comprar 5+ ------")
                print("------ Descuento aplicado: ", descuento, " ------")

            """Elimina del inventario la cantidad de cosas compradas"""
            cantidad = cantidad - venta

            """Suma las cosas compradas"""
            comprado = comprado + venta

            """Suma el dinero obtenido por la venta"""
            ingreso = ingreso + costoff

            """Muestra las unidades que quedan"""
            print("------ Unidades restantes: ", cantidad)

            """Muestra el precio de la compra"""
            print("------ Subtotal de esta compra: ", costoff)

            """Si ya no quedan unidades se termina la funcion"""
            if cantidad == 0:
                print("------ Ya no hay ;( ------")
                return cantidad, comprado, ingreso

            """Revisa si quedan pocas unidades"""
            if cantidad <= stock_minimo:
                print("------ Quedan pocos ------")

            """Pregunta si el cliente quiere seguir comprando"""
            continuar = input("Quieres seguir comprando? (si o no): ")
            if continuar == "no":
                return cantidad, comprado, ingreso
            elif continuar != "si":
                print("------ Eso es un no ------")
                return cantidad, comprado, ingreso

    """Regresa los datos ya actualizados del producto"""
    return cantidad, comprado, ingreso

"""Esta muestra el menu principal y permite elegir un producto"""
def menu(cantidad, comprado, ingreso, cantidad2, comprado2, ingreso2, cantidad3, comprado3, ingreso3,
         cantidad4, comprado4, ingreso4, cantidad5, comprado5, ingreso5, cantidad6, comprado6, ingreso6):

    """Guarda la opcion que eligieron"""
    opcion = ""

    """La funcion del menu es reusable porque se repite hasta que el usuario le de a salir"""
    while opcion != "8":
        print()
        print("========== MENU ==========")
        print("1. Comprar computadora")
        print("2. Comprar telefono")
        print("3. Comprar raton")
        print("4. Comprar teclado")
        print("5. Comprar monitor")
        print("6. Comprar audifonos")
        print("7. Ver reporte")
        print("8. Salir")

        """Te pide una opcion"""
        opcion = input("Que quieres hacer?: ")

        """Compra de cada producto"""
        if opcion == "1":
            cantidad, comprado_ahora, ingreso_ahora = comproducto(
                producto, precio, cantidad, stock_minimo, 0, 0)

            """Actualiza el total del producto vendido"""
            comprado = comprado + comprado_ahora

            """Actualiza el ingreso del producto"""
            ingreso = ingreso + ingreso_ahora

        elif opcion == "2":
            cantidad2, comprado_ahora, ingreso_ahora = comproducto(
                producto2, precio2, cantidad2, stock_minimo2, 0, 0)
            comprado2 = comprado2 + comprado_ahora
            ingreso2 = ingreso2 + ingreso_ahora

        elif opcion == "3":
            cantidad3, comprado_ahora, ingreso_ahora = comproducto(
                producto3, precio3, cantidad3, stock_minimo3, 0, 0)
            comprado3 = comprado3 + comprado_ahora
            ingreso3 = ingreso3 + ingreso_ahora

        elif opcion == "4":
            cantidad4, comprado_ahora, ingreso_ahora = comproducto(
                producto4, precio4, cantidad4, stock_minimo4, 0, 0)
            comprado4 = comprado4 + comprado_ahora
            ingreso4 = ingreso4 + ingreso_ahora

        elif opcion == "5":
            cantidad5, comprado_ahora, ingreso_ahora = comproducto(
                producto5, precio5, cantidad5, stock_minimo5, 0, 0)
            comprado5 = comprado5 + comprado_ahora
            ingreso5 = ingreso5 + ingreso_ahora

        elif opcion == "6":
            cantidad6, comprado_ahora, ingreso_ahora = comproducto(
                producto6, precio6, cantidad6, stock_minimo6, 0, 0)
            comprado6 = comprado6 + comprado_ahora
            ingreso6 = ingreso6 + ingreso_ahora

        """Muestra el reporte"""
        elif opcion == "7":
            print()
            print("========== REPORTE ==========")

            """Muestra las ventas e ingresos de cada producto"""
            print("Computadoras vendidas: ", comprado, " - Ingreso: ", ingreso)
            print("Telefonos vendidos: ", comprado2, " - Ingreso: ", ingreso2)
            print("Ratones vendidos: ", comprado3, " - Ingreso: ", ingreso3)
            print("Teclados vendidos: ", comprado4, " - Ingreso: ", ingreso4)
            print("Monitores vendidos: ", comprado5, " - Ingreso: ", ingreso5)
            print("Audifonos vendidos: ", comprado6, " - Ingreso: ", ingreso6)

            """Calcula todos los ingresos de la tienda"""
            ingreso_total = ingreso + ingreso2 + ingreso3 + ingreso4 + ingreso5 + ingreso6
            print("Ingreso total de la tienda: ", ingreso_total)

        """Opcion para salir"""
        elif opcion == "8":
            print("------ Gracias por usar el inventario ------")

        """Por si se escribe una opcion que no existe"""
        else:
            print()
            print("------ Esa opcion no existe ------")

    """Regresa todos los datos actualizados"""
    return (cantidad, comprado, ingreso, cantidad2, comprado2, ingreso2,
            cantidad3, comprado3, ingreso3, cantidad4, comprado4, ingreso4,
            cantidad5, comprado5, ingreso5, cantidad6, comprado6, ingreso6)

"""Se llama de vuelta al menu y guarda todos los datos actualizados"""
(cantidad, comprado, ingreso, cantidad2, comprado2, ingreso2, cantidad3, comprado3, ingreso3,
 cantidad4, comprado4, ingreso4, cantidad5, comprado5, ingreso5, cantidad6, comprado6, ingreso6) = menu(
    cantidad, comprado, ingreso, cantidad2, comprado2, ingreso2, cantidad3, comprado3, ingreso3,
    cantidad4, comprado4, ingreso4, cantidad5, comprado5, ingreso5, cantidad6, comprado6, ingreso6)


"""Muestra la cantidad total vendida de cada producto"""
print()
print("========== COMPRA FINAL ==========")
print("Computadoras: ", comprado)
print("Telefonos: ", comprado2)
print("Ratones: ", comprado3)
print("Teclados: ", comprado4)
print("Monitores: ", comprado5)
print("Audifonos: ", comprado6)

"""Muestra los ingresos obtenidos por cada producto"""
print()
print("========== INGRESOS ==========")
print("Computadoras: ", ingreso)
print("Telefonos: ", ingreso2)
print("Ratones: ", ingreso3)
print("Teclados: ", ingreso4)
print("Monitores: ", ingreso5)
print("Audifonos: ", ingreso6)

"""Calcula el ingreso total de todos los productos"""
ingreso_total = ingreso + ingreso2 + ingreso3 + ingreso4 + ingreso5 + ingreso6

"""Muestra el ingreso total"""
print("Ingreso total: ", ingreso_total)
