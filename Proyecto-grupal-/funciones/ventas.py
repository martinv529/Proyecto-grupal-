encabezado = ["IDventa", "cantidad", "articulo", "importe", "IDcliente"] 

matriz_ventas = [
    ["IDventa", "cantidad", "articulo", "importe", "IDcliente"],
    ["001", "4", "silla", "40000.00", "03"],
    ["002", "2", "mesa de luz", "40000.00", "02"],
    ["003", "5", "escritorios", "125000.00", "05"],
    ["004", "1", "mesa", "30000.00", "01"],
    ["005", "3", "sillon","150000.00", "04"]
    ]

def agregar_venta(matriz):
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
            importe += ".00"
            
            datos = [IDnuevo, cantidadProductos, producto, importe, IDcliente]

            matriz_ventas.append(datos)

    return matriz_ventas


def editar_venta(matriz):
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
            cambio=int(input("Que desea cambiar?\n"))
            while cambio > 4 or cambio < 1:
                cambio=int(input("Ingrese una opcion valida\n"))
            idVenta=int(input("Cual es el ID de venta?\n"))
            while idVenta < int(matriz[1][0]) or idVenta > int(matriz[len(matriz)-1][0]):
                idVenta = int(input("Ingrese un ID dentro del rango\n"))
            if cambio == 1:
                matriz [idVenta][cambio]=int(input("Ingrese la cantidad de articulos\n"))
            
            elif cambio == 2:
                matriz [idVenta][cambio]=input("Ingrese el articulo\n")
            
            elif cambio == 3:
                matriz [idVenta][cambio]=input("Ingrese el importe total\n")
                matriz [idVenta][cambio] += ".00"
            
            else:
                matriz [idVenta][cambio]=input("Ingrese el id del cliente\n").zfill(2)

            

    return matriz


def eliminar_venta(matriz):
    id_a_eliminar = input("Ingrese el ID de la venta que desea eliminar \n").strip()

    nueva_matriz = []
    eliminado = False

    while id_a_eliminar > matriz[len(matriz)-1][0] or id_a_eliminar < matriz[1][0]:
        id_a_eliminar = input("Ingrese un ID dentro del rango\n").strip()

    for fila in matriz:
        if fila[0] != id_a_eliminar:
            nueva_matriz.append(fila)
        else:
            eliminado = True

    if eliminado:
        print(f"La ventacon con ID {id_a_eliminar} fue eliminado correctamente")
    else:
        print(f"No se encontró una venta con ID {id_a_eliminar}")
    
    for i in range(len(nueva_matriz)-1):
        if nueva_matriz[i+1][0] > id_a_eliminar:
            nueva_matriz[i+1][0] = str(int(nueva_matriz[i+1][0])-1).zfill(3)

    return nueva_matriz

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Find e la ejecucion")