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

def agregar_producto(matriz):
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

            matriz.append(datos)

    return matriz

matriz_productos = agregar_producto(matriz_productos)

productos = [dict(zip(encabezado,fila))for fila in matriz_productos]

print("diccionario:")
for producto in productos:
    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")

def editar_producto(matriz):
    cantidad = int(input("Cuantos productos desea cambiar?\n"))
    bandera = True
    contador = 0

    while bandera:
        if cantidad == contador:
            bandera=False

        else:
            contador+=1

            print("1- Nombre del producto")
            print("2- Precio del producto")
            cambio=int(input("Que desea cambiar?\n"))
            idProducto=int(input("Cual es el ID del producto?\n"))
            if cambio == 1:
                matriz [idProducto-1][cambio]=str(input("Ingrese el nombre del producto\n"))
            
            elif cambio == 2:
                matriz [idProducto-1][cambio]=int(input("Ingrese el precio\n"))

    return matriz

matriz_productos= editar_producto(matriz_productos)

productos=[dict(zip(encabezado, fila))for fila in matriz_productos]

print("diccionario:")
for producto in productos:
    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")

def eliminar_producto(matriz):
    id_a_eliminar = input("Ingrese el ID del producto que desea eliminar \n").strip()

    nueva_matriz = []
    eliminado = False

    for fila in matriz:
        if fila[0] != id_a_eliminar:
            nueva_matriz.append(fila)
        else:
            eliminado = True

    if eliminado:
        print(f"El prducto con ID {id_a_eliminar} fue eliminado correctamente")
    else:
        print(f"No se encontró un prodcuto con ID {id_a_eliminar}")
    
    for i in range(len(nueva_matriz)-1):
        if nueva_matriz[i+1][0] > id_a_eliminar:
            nueva_matriz[i+1][0] = str(int(nueva_matriz[i+1][0])-1).zfill(2)

    return nueva_matriz

matriz_productos = eliminar_producto(matriz_productos)

productos = [dict(zip(encabezado, fila)) for fila in productos]
print("diccionario:")
for producto in productos:
    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")