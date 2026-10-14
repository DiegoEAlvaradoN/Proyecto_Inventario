# Proyecto\_Inventario

### Contexto

El proyecto consiste en desarrollar un sistema básico de inventario utilizando únicamente Python, tomando en cuenta los conocimientos y habilidades adquiridos durante el curso, así como los contenidos establecidos en el plan académico

El programa tiene como objetivo permitir la gestión de productos mediante funciones como consultar el inventario, modificar cantidades, aplicar descuentos, registrar ventas y verificar las existencias disponibles, todo esto a través de la terminal, utilizando herramientas y conceptos básicos de programación en Python

### Objetivo

La idea es crear un programa sencillo que permita llevar un control básico de los productos con ayuda de las funciones que vayamos aprendiendo en clase

# Proyecto Inventario

## Algoritmo (actualmente)

1. Iniciar el programa
2. Registrar los productos, precios, cantidades disponibles y stock mínimo mediante listas
3. Mostrar el menú principal
4. Solicitar al usuario una opción
5. Permitir seleccionar un producto para realizar una compra
6. Mostrar la información y disponibilidad del producto seleccionado
7. Si el producto está agotado, permitir reabastecerlo validando que la cantidad agregada sea mayor que cero
8. Solicitar la cantidad que se desea comprar
9. Validar la cantidad solicitada y comprobar que exista suficiente inventario
10. Aplicar un descuento del 10% cuando se compren cinco o más unidades
11. Actualizar la cantidad disponible del producto en su lista
12. Registrar las unidades vendidas y los ingresos obtenidos en las listas correspondientes
13. Verificar el nivel de stock disponible
14. Permitir continuar realizando compras
15. Permitir consultar el inventario completo con precios, cantidades disponibles y valor de cada producto
16. Mostrar un reporte con las unidades vendidas y los ingresos de cada producto
17. Calcular el ingreso total de todos los productos
18. Repetir el proceso hasta seleccionar la opción de salir
19. Mostrar el resumen final de ventas e ingresos
20. Finalizar el programa

## Incorpora a tu proyecto libre listas (arreglos)

- Se sustituyeron las variables individuales de cada producto por listas para organizar mejor toda la información.
- Se crearon listas para almacenar los nombres, los precios, las cantidades, el stock mínimo, las unidades vendidas y los ingresos de los productos.
- Se modificó la función "comproducto()" para que solo recibiera la posición del producto en la lista.
- Se simplificó la función "menu()" para que no se tenga que recibir y devolver múltiples variables
- Se agregó la función "mostrar_inventario()" para consultar todos los productos, sus precios, cantidades disponibles y valor en inventario
- Se añadió la opción 8 al menú para que el usuario pudiera ver el inventario y la opción de salida pasó a ser el número 9.
- Se separó el reporte de ventas en una nueva función llamada "reporte()"
- Se utilizaron bucles for para recorrer las listas y mostrar todos los productos, las ventas y los ingresos para no repetir tanto código.
- Se modificó el cálculo de ingresos totales para sumar los valores de la lista "ingresos" mediante un ciclo
- Se añadió un control que impedía restar existencias a un producto con una cantidad inferior a cero.
- Se añadió un indicador que muestra si un producto estaba agotado o tiene existencias limitadas en la lista de inventario.
- Todas las listas se actualizaron para reflejar los cambios en las ventas, los ingresos y el stock, sin necesidad de devolver los valores de las funciones.
- Se simplificaron los resúmenes finales de compras e ingresos utilizando ciclos "for"
- Se hizo un cambio menor para mejorar la presentación de los mensajes en la consola con espacios y saltos de línea
