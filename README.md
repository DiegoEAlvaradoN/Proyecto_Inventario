# Proyecto\_Inventario

### Contexto

El proyecto consiste en desarrollar un sistema básico de inventario utilizando únicamente Python, tomando en cuenta los conocimientos y habilidades adquiridos durante el curso, así como los contenidos establecidos en el plan académico.

El programa tiene como objetivo permitir la gestión de productos mediante funciones como consultar el inventario, modificar cantidades, aplicar descuentos, registrar ventas y verificar las existencias disponibles, todo esto a través de la terminal, utilizando herramientas y conceptos básicos de programación en Python.

Se cambió el enfoque inicial del proyecto debido a haber entendido mejor el objetivo de la clase, pudiendo ver que la propuesta inicialmente planteada era una meta inalcanzable y poco realista si se toma en cuenta lo que realmente se planeó como el contenido educativo del plan académico, por eso el proyecto pasó a ser un sistema básico de inventario utilizando únicamente Python (la propuesta original se conserva al final)

El programa permite registrar productos, consultar el inventario, modificar cantidades, añadir descuentos, eliminar productos y verificar las existencias disponibles, todo mediante la terminal y Python.

A partir del Avance 9, el inventario se guarda en un archivo de texto ("inventario.txt") y se carga al iniciar el programa, para que los cambios no se pierdan al cerrarlo.

### Objetivo

La meta es crear un programa sencillo que permita llevar un control básico de los productos con ayuda de las funciones y conceptos que vayamos aprendiendo en clase.

## Algoritmo (actualmente)

1. Iniciar el programa
2. Registrar los productos, precios, cantidades disponibles, stock mínimo, unidades vendidas e ingresos mediante una matriz (cada fila es un producto)
3. Crear una matriz vacía para el historial de compras
4. Cargar desde el archivo "inventario.txt" los datos guardados de cada producto y actualizar la matriz del inventario
5. Mostrar el menú principal
6. Solicitar al usuario una opción, eliminando los espacios innecesarios que escriba al principio y al final
7. Permitir seleccionar un producto para realizar una compra
8. Mostrar la información y disponibilidad del producto seleccionado, con su nombre con la primera letra en mayúscula
9. Si el producto está agotado, permitir reabastecerlo validando que la cantidad agregada sea mayor que cero y guardar el cambio en el archivo
10. Solicitar la cantidad que se desea comprar
11. Validar la cantidad solicitada y comprobar que exista suficiente inventario
12. Aplicar un descuento del 10% cuando se compren cinco o más unidades
13. Actualizar la cantidad disponible del producto en su fila de la matriz
14. Registrar las unidades vendidas y los ingresos obtenidos en las columnas correspondientes de la matriz
15. Agregar una fila nueva al historial con el producto, las unidades y el costo de la compra
16. Guardar el inventario actualizado en el archivo "inventario.txt"
17. Verificar el nivel de stock disponible
18. Permitir continuar realizando compras, aceptando las respuestas de "si" o "no" sin importar si se escriben con mayúsculas, minúsculas o espacios de más
19. Permitir consultar el inventario completo con precios, cantidades disponibles y valor de cada producto
20. Mostrar un reporte con las unidades vendidas y los ingresos de cada producto
21. Permitir consultar el historial de compras, mostrando cada compra y el total acumulado
22. Permitir buscar un producto por su nombre y consultar su precio y cantidad disponible
23. Calcular el ingreso total de todos los productos
24. Repetir el proceso hasta seleccionar la opción de salir
25. Mostrar el resumen final de ventas e ingresos
26. Finalizar el programa

## Incorpora a tu proyecto libre ...

### Avance 9 — Manejo de archivos

* Se creó el archivo "inventario.txt" para guardar el inventario, con una línea por producto y los datos separados por comas en este orden: nombre, precio, cantidad disponible, stock mínimo, unidades vendidas e ingresos (por ejemplo `raton,800,10,3,0,0`)
* Se creó la función "guardar\_inventario()", que abre el archivo en modo escritura con `open()` y el modo `"w"`, recorre la matriz con un ciclo "for", arma cada línea uniendo los datos con comas (convirtiendo los números a texto con `str()`), la escribe con `write()` agregando un salto de línea y cierra el archivo con `close()`
* Se creó la función "cargar\_inventario()", que abre el archivo en modo lectura con el modo `"r"` y recorre sus líneas con un ciclo "for"
* Dentro de "cargar\_inventario()" se usa `strip()` para quitar el salto de línea y `split(",")` para separar cada línea en una lista con sus datos
* Los datos leídos del archivo (que llegan como texto) se convierten a número con `int()` para precio, cantidad, stock mínimo y unidades vendidas, y con `float()` para los ingresos, ya que con el descuento del 10% pueden tener decimales
* Los datos convertidos se guardan en la fila correspondiente de la matriz "inventario", usando una variable "i" que avanza una fila por cada línea leída
* Se llama a "cargar\_inventario()" antes de mostrar el menú, para que al iniciar el programa se recupere el precio, las existencias, las unidades vendidas y los ingresos de cada producto
* Se llama a "guardar\_inventario()" dentro de "comproducto()" después de reabastecer un producto y después de cada compra, para que los cambios se guarden en el archivo en cuanto ocurren
* Gracias a esto el inventario se conserva al cerrar y volver a ejecutar el programa, y el reporte y los resúmenes finales muestran las ventas acumuladas
* El historial de compras no se guarda en el archivo, por lo que empieza vacío cada vez que se ejecuta el programa
* El archivo "inventario.txt" debe estar en la misma carpeta que el programa y conservar el orden de los productos, de lo contrario el programa no puede cargar los datos
* Se agregó un comentario en la matriz "inventario" explicando qué contiene cada columna y se cambió el comentario de la columna 2 del "historial" de "subtotal" a "costo"
* Se actualizó el título del programa a "Avance 9"
* Se mantuvieron los comentarios en el código explicando qué hace cada parte de la lectura y escritura del archivo

## Avances anteriores

Resumen de lo incorporado en cada avance previo, ya integrado en el programa actual.

### Avance 2 — Operaciones con operadores

Se incorporaron operaciones básicas para indicar el funcionamiento esencial de los procesos esperados dentro del programa, haciendo la prueba con un stock de computadoras.

### Avance 3 — Uso de funciones

(Actualización en "PROYECTO\_INVENTARIO")

* Se amplió el inventario de 1 a 3 productos (computadora, teléfono y ratón) para mostrar el aprovechamiento del uso de la función
* Se implementó el uso de funciones con la función "comproducto()" para reutilizar el proceso de compra
* Se agregó un detalle a la experiencia mostrando el registro de unidades compradas, la cantidad restante y un resumen final de compras por producto

### Avance 4 — Estructuras de decisión

* Se agregaron más productos al inventario: teclado, monitor y audífonos
* Se agregó una variable de ingreso a cada producto para almacenar el dinero obtenido por sus ventas
* Se modificó la función de comproducto para que pueda manejar más información durante el proceso de compra
* Se agregó un menú principal para facilitar la navegación del programa
* Se agregó la opción de reabastecer productos cuando alguno llega a 0 unidades, permitiendo ingresar una nueva cantidad al inventario
* Se agregó una validación para evitar realizar compras con cantidades menores o iguales a cero
* Se agregó un descuento del 10% en compras de 5 o más unidades
* Se agregó el cálculo y acumulación de los ingresos generados por cada compra
* Se agregó un reporte con los productos vendidos, el ingreso generado por cada producto y el ingreso total de la tienda
* Se mejoró el control de las compras, permitiendo seleccionar y comprar cada producto desde el menú sin tener que seguir un orden específico
* Se agregó un resumen final con la información de las compras realizadas
* Se agregaron comentarios y documentación al código tomando como referencia el documento proporcionado **"Convenciones de Estilo en Python.pdf"**

### Avance 5 — Estructuras de repetición (ciclos)

En este avance se cambió el enfoque del proyecto (ver Contexto) y se conservó la lista de cambios del avance 4, ya que este README llevaba ambos encabezados: *"estructuras de decisión"* y *"estructuras de repetición (ciclos)"*.

<details>
<summary>Algoritmo que tenía el proyecto en este avance</summary>

1. Iniciar el programa.
2. Registrar los productos, precios, cantidades disponibles y stock mínimo.
3. Mostrar el menú principal.
4. Solicitar al usuario una opción.
5. Permitir seleccionar un producto para realizar una compra.
6. Mostrar la información y disponibilidad del producto seleccionado.
7. Solicitar la cantidad que se desea comprar.
8. Validar la cantidad solicitada y comprobar que exista suficiente inventario.
9. Aplicar el descuento correspondiente cuando se compren cinco o más unidades.
10. Actualizar la cantidad disponible del producto.
11. Registrar las unidades vendidas y los ingresos obtenidos.
12. Verificar el nivel de stock disponible.
13. Permitir continuar realizando compras.
14. Mostrar un reporte con las unidades vendidas y los ingresos de cada producto.
15. Calcular el ingreso total de todos los productos.
16. Repetir el proceso hasta seleccionar la opción de salir.
17. Mostrar el resumen final de ventas e ingresos.
18. Finalizar el programa.

</details>

### Avance 6 — Listas (arreglos)

* Se reemplazaron las variables individuales de cada producto por listas para organizar mejor la información
* Se crearon listas para almacenar los nombres, precios, cantidades, stock mínimo, unidades vendidas e ingresos de los productos
* Se modificó la función "comproducto()" para recibir únicamente la posición del producto en las listas
* Se implementó el uso de índices para consultar y actualizar directamente los datos de cada producto
* Se simplificó la función "menu()", eliminando la necesidad de recibir y devolver múltiples variables
* Se agregó la función "mostrar\_inventario()" para consultar todos los productos, sus precios, cantidades disponibles y valor en inventario
* Se añadió la opción 8 del menú para visualizar el inventario y se cambió la opción de salida al número 9
* Se separó el reporte de ventas en una nueva función llamada "reporte()"
* Se implementaron ciclos "for" para recorrer las listas y mostrar los productos, las ventas y los ingresos, evitando repetir tanto código
* Se modificó el cálculo de ingresos totales para sumar los valores de la lista "ingresos" mediante un ciclo
* Se agregó una validación para impedir que se reabastezca un producto con cantidades menores o iguales a cero
* Se añadieron indicadores de productos agotados o con pocas unidades en la nueva vista del inventario
* Se actualizaron los datos de ventas, ingresos y existencias directamente en las listas, sin necesidad de devolverlos desde las funciones
* Se simplificaron los resúmenes finales de compras e ingresos utilizando ciclos "for"
* Se mejoró la presentación de los mensajes en consola mediante espacios y saltos de línea

### Avance 7 — Listas anidadas (matrices)

* Se reemplazaron las seis listas independientes (nombres, precios, cantidades, stock mínimo, unidades vendidas e ingresos) por una sola matriz llamada "inventario", donde cada fila es un producto
* Se definieron las columnas de la matriz: 0 = nombre, 1 = precio, 2 = cantidad, 3 = stock mínimo, 4 = comprados y 5 = ingresos
* Se modificó la función "comproducto()" para consultar y actualizar los datos con doble índice, por ejemplo `inventario[numero][2]` para la cantidad disponible del producto
* Se actualizaron las funciones "mostrar\_inventario()" y "reporte()" para recorrer las filas de la matriz y leer cada dato por su columna
* Se creó una segunda matriz llamada "historial", que empieza vacía y a la que se le agrega una fila nueva con cada compra realizada (columnas: 0 = producto, 1 = unidades y 2 = subtotal)
* Se utiliza `append()` dentro de "comproducto()" para agregar al historial una lista con el producto, las unidades y el subtotal (ya con el descuento aplicado, si corresponde)
* Se agregó la función "mostrar\_historial()", que recorre la matriz con dos ciclos "for" anidados: el de afuera recorre cada compra (fila) y el de adentro recorre sus columnas
* Se agregó un mensaje cuando todavía no hay compras en el historial
* Se calcula el total de todas las compras sumando la columna de subtotales del historial
* Se añadió la opción 9 del menú para ver el historial de compras y se cambió la opción de salida al número 10
* Se actualizaron los resúmenes finales de compras e ingresos para leer los datos directamente de las columnas de la matriz "inventario"
* Se mantuvieron los comentarios en el código explicando qué contiene cada columna y cada ciclo

### Avance 8 — Manejo de cadenas

* Se agregó "strip()" para eliminar los espacios innecesarios al principio y al final de la opción del menú y de las respuestas de "si o no", evitando errores cuando el usuario escribe de más
* Se agregó "upper()" para convertir las respuestas de "si o no" a mayúsculas, así el programa acepta "si", "Si" o "SI" sin generar problemas
* Se modificaron las comparaciones en "comproducto()" para que ahora compare en mayusculas "SI" y "NO", y se cambió el valor inicial de "continuar" a "SI" para que el ciclo funcione igual
* Se agregó "lower()" para convertir a minúsculas el texto que escribe el usuario al buscar un producto y poder buscarlo mas facil
* Se cambiaron los nombres de los productos en inventario a minúsculas para poder compararlos de forma sencilla
* Se agregó "capitalize()" para mostrar los nombres de los productos con la primera letra en mayúscula y las demás en minúsculas para que se vea mejor en "comproducto()", "mostrar\_inventario()", "reporte()", "mostrar\_historial()" y en los resúmenes finales
* Se creó la función "buscar\_producto()", para buscar el nombre de un producto en la matriz usando "find()" para saber si el texto está dentro de cada nombre
* Se utiliza el valor que regresa "find()" para decidir si se muestra el precio y la cantidad disponible del producto o un mensaje de que no se encontró
* Se permite buscar con solo una parte del nombre, por ejemplo "tecla" encuentra el teclado
* Se agregó una validación para cuando el usuario no escribe nada en la búsqueda, ya que `find()` con un texto vacío encontraría todos los productos
* Se añadió la opción 10 del menú para buscar un producto y se cambió la opción de salida al número 11
* Se mantuvieron los comentarios en el código explicando qué hace cada método de cadenas
