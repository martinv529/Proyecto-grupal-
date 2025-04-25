matriz_productos =[
    ["01", "silla", "10000"], 
    ["02","mesa","30000"],
    ["03","escritorio","25000"],
    ["04","sillon","50000"],
    ["05","mesa de luz","20000"]
    ]

encabezado = ["IDarticulo", "articulo", "precio"]

for fila in matriz_productos:
    id_, articulo, precio = fila
    print(f"{id_:<5} | {articulo:<15} | ${precio:>10}")

productos = [dict(zip(encabezado,fila))for fila in matriz_productos]

for producto in productos:
    print(producto)

def agregar_dato(matriz):
    columnas = len(encabezado)
    cantidad = int(input("Cuantos productos desea agregar?\n"))
    bandera = True
    contador = 0
    
    while bandera:
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            
            IDanterior = matriz[len(matriz)-1][0]
            IDnuevo = str(int(IDanterior) + 1).zfill(2) 
            producto = input(f"Ingrese el nombre del producto numero {contador}\n")
            precio = input(f"Ingrese el precio del producto numero {contador}\n")
            
            datos = [IDnuevo, producto, precio]

            matriz_productos.append(datos)

    return matriz_productos

productos = agregar_dato(matriz_productos)

for fila in productos:
    id_, articulo, precio = fila
    print(f"{id_:<5} | {articulo:<15} | ${precio:>10}")





        
            



