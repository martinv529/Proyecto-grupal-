idClientes = ["01", "02", "03", "04", "05"]
nombresClientes = ["lionel messi", "diego armando maradona", "martin palermo", "juan Roman Riqueleme", "clemente rodriguez"]

# Crear el diccionario con zip
clientes = dict(zip(idClientes, nombresClientes))

# Función para agregar nuevos clientes
def agregar_cliente(diccionario, listaID):
    cantidad = int(input("\n¿Cuántos clientes nuevos desea ingresar?\n"))
    contador = 0
    bandera = True
    while bandera:
        if cantidad == contador:
            bandera = False
        else:
            contador += 1

            # Calcular el nuevo ID
            idAnterior = listaID[-1]  # Último ID actual
            idNuevo = str(int(idAnterior) + 1).zfill(2)  # Sumar 1 y mantener formato "01", "02", etc.

            # Pedir el nombre del nuevo cliente
            nombre = input(f"Ingrese el nombre y apellido del nuevo cliente número {contador}\n")

            #agrega el nombre al diccionario
            diccionario.setdefault(idNuevo, nombre)
            #agrega el nuevo ID a la lista de IDs
            listaID.append(idNuevo)

    return diccionario

def eliminar_cliente(dicclientes):
    listanombres = []
    id = str(input("ingrese el id del cliente para eliminarlo\n"))
    idnumero = int(id)
    largo = len(dicclientes)
    while idnumero > largo or idnumero <= 0:
        id = str(input("ingrese un id de cliente dentro del rango para eliminarlo\n"))
        idnumero = int(id)
        if idnumero<largo and idnumero > 0:
            del dicclientes[id]
    lista_Clientes = list(dicclientes)#lista con las keys

    for i in range (largo): #reemplaza los nombres en su posicion
        if idnumero<int(lista_Clientes[i]):
            lista_Clientes[i] = str(int(lista_Clientes[i])-1).zfill(2)

    listanombres = dicclientes.values()

    nuevodic = dict(zip(lista_Clientes,listanombres ))
    return nuevodic

def modificar_cliente(dicclientes):
    id = str(input("ingrese el id del cliente para cambiarlo\n"))
    idint = int(id)
    largo = len(dicclientes)
    while idint > largo or idint <= 0:
        id = str(input("ingrese un id dentro del rango para el reemplazo\n"))
        idint = int(id)
    cambio = str(input("ingrese el nuevo nombre para el reemplazo\n"))
    dicclientes[id] = cambio
    return dicclientes

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Módulo clientes ejecutado directamente")