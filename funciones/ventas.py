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

matriz_ventas = agregar_dato(matriz_ventas)

def cambiar_dato(matriz):
    columnas = len(encabezado)
    cantidad = int(input("Cuantos registros de venta desea cambiar?\n"))
    bandera = True
    contador = 0

    while bandera:
        if cantidad == contador:
            bandera=False

        else:
            contador+=1

            print("1- Cantidad")
            print("2- articulo")
            print("3- Importe")
            print("4- ID Cliente")
            cambio=int(input("Que desea cambiar?"))
            IdCiente=int(input("Cual es el numero de venta?"))
            if cambio == 1:
                matriz [IdCiente][cambio]=int(input("Ingrese la cantidad de articulos"))
            
            elif cambio == 2:
                matriz [IdCiente][cambio]=int(input("Ingrese el articulo"))
            
            elif cambio == 3:
                matriz [IdCiente][cambio]=int(input("Ingrese el importe total"))
            
            elif cambio == 4:
                matriz [IdCiente][cambio]=int(input("Ingrese el id del cliente"))

    return matriz

matriz_ventas= cambiar_dato(matriz_ventas)

for fila in matriz_ventas:
    IDnuevo, cantidadProductos, producto, importe, IDcliente = fila
    print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {producto:<15} | ${importe:<15} | {IDcliente:>10}")