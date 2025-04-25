IDclientes = ["01", "02", "03", "04", "05"]
nombresClientes = ["lionel messi", "diego armando maradona", "martin palermo", "juan Roman Riqueleme", "clemente rodriguez"]

# Crear el diccionario con zip
clientes = dict(zip(IDclientes, nombresClientes))

# Mostrar los clientes actuales
print("Clientes actuales:")
for id_cliente, nombre_cliente in clientes.items():
    print(f"{id_cliente:10} {nombre_cliente:4}")

# Función para agregar nuevos clientes
def agregar_dato(diccionario, listaID, listaNombres):
    cantidad = int(input("\n¿Cuántos clientes nuevos desea ingresar?\n"))
    contador = 0
    bandera = True
    while bandera:
        if cantidad == contador:
            bandera = False
        else:
        
            contador += 1

            # Calcular el nuevo ID
            IDanterior = listaID[-1]  # Último ID actual
            IDnuevo = str(int(IDanterior) + 1).zfill(2)  # Sumar 1 y mantener formato "01", "02", etc.

            # Pedir el nombre del nuevo cliente
            nombre = input(f"Ingrese el nombre y apellido del nuevo cliente número {contador}: ")

            # Agregar a las listas
            listaID.append(IDnuevo)
            listaNombres.append(nombre)

    # Actualizar el diccionario
    nuevo_diccionario = dict(zip(listaID, listaNombres))
    diccionario.update(nuevo_diccionario)

    return diccionario, listaID, listaNombres

# Llamada a la función
diccionarioClientes, IDs, nombres = agregar_dato(clientes, IDclientes, nombresClientes)

# Mostrar clientes actualizados
print("\nClientes actualizados:")
for id_cliente, nombre_cliente in diccionarioClientes.items():
    print(f"{id_cliente:10} {nombre_cliente}")