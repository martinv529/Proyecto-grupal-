matriz_productos =[
    ["01", "silla", "10000.00"], 
    ["02","mesa","30000.00"],
    ["03","escritorio","25000.00"],
    ["04","sillon","50000.00"],
    ["05","mesa de luz","20000.00"]
    ]

encabezado = ["IDarticulo", "articulo", "precio"]

productos = [dict(zip(encabezado,fila))for fila in matriz_productos]

def agregar_producto(matriz):
    cantidad = int(input("Cuantos productos desea agregar?\n"))
    bandera = True
    contador = 0
    
    while bandera:
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            
            idAnterior = matriz[len(matriz)-1][0]
            idNuevo = str(int(idAnterior) + 1).zfill(2) 
            producto = input(f"Ingrese el nombre del producto numero {contador}\n")
            precio = input(f"Ingrese el precio del producto numero {contador}\n")
            precio += ".00"
            
            datos = [idNuevo, producto, precio]

            matriz.append(datos)

    return matriz

productos = [dict(zip(encabezado,fila))for fila in matriz_productos]

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
            while cambio > 2 or cambio < 1:
                cambio=int(input("Ingrese una opcion valida\n"))
            idProducto=input("Cual es el ID del producto?\n")
            while idProducto > matriz[len(matriz)-1][0] or idProducto < matriz[0][0]:
                idProducto = input("Ingrese un ID dentro del rango\n").strip()

            if cambio == 1:
                matriz [int(idProducto)-1][cambio]=str(input("Ingrese el nombre del producto\n"))
            
            elif cambio == 2:
                matriz [int(idProducto)-1][cambio]=input("Ingrese el precio\n")
                matriz [int(idProducto)-1][cambio] += ".00"

    return matriz

productos=[dict(zip(encabezado, fila))for fila in matriz_productos]


def eliminar_producto(matriz):
    id_a_eliminar = input("Ingrese el ID del producto que desea eliminar \n").strip()

    nueva_matriz = []
    eliminado = False
    
    while id_a_eliminar > matriz[len(matriz)-1][0] or id_a_eliminar < matriz[0][0]:
        id_a_eliminar = input("Ingrese un ID dentro del rango\n").strip()
        

    for fila in matriz:
        if fila[0] != id_a_eliminar:
            nueva_matriz.append(fila)
        else:
            eliminado = True

    if eliminado:
        print(f"El prducto con ID {id_a_eliminar} fue eliminado correctamente")
    else:
        print(f"No se encontró un prodcuto con ID {id_a_eliminar}")
    
    for i in range(len(nueva_matriz)):
        if nueva_matriz[i][0] > id_a_eliminar:
            nueva_matriz[i][0] = str(int(nueva_matriz[i][0])-1).zfill(2)
    
    return nueva_matriz


productos = [dict(zip(encabezado, fila)) for fila in productos]

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")