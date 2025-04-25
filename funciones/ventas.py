encabezado = ["IDventa", "cantidad", "articulo", "importe", "IDcliente"] 

matriz_ventas = [
    ["IDventa", "cantidad", "articulo", "importe", "IDcliente"],
    ["001", "4", "silla", "40000", "03"],
    ["002", "2", "mesa de luz", "40000", "02"],
    ["003", "5", "escritorios", "125000", "05"],
    ["004", "1", "mesa", "30000", "01"],
    ["005", "3", "sillon","150000", "04"]
    ]

def agregar_dato(matriz):
    columnas = len(encabezado)
    cantidad = int(input("Cuantos registros de venta desea agregar?\n"))
    bandera = True
    contador = 0
    
    while bandera:
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            
            IDanterior = matriz[len(matriz)-1][0]
            IDnuevo = str(int(IDanterior) + 1).zfill(3) 
            cantidadProductos = input(f"Ingrese la cantidad de productos vendidos de la venta {contador}\n")
            producto = input(f"Ingrese el nombre del articulo vendido {contador}\n")
            precio = input(f"Ingrese el precio del producto {contador}\n")
            IDcliente = input(f"Ingrese el ID del comprador de la venta {contador}\n")

            importe = str(int(precio) * int(cantidadProductos))
            
            datos = [IDnuevo, cantidadProductos, producto, importe, IDcliente]

            matriz_ventas.append(datos)

    return matriz_ventas

ventas = agregar_dato(matriz_ventas)

for fila in ventas:
    IDnuevo, cantidadProductos, producto, importe, IDcliente = fila
    print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {producto:<15} | ${importe:<15} | {IDcliente:>10}")