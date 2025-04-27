import ventas
import articulos
import clientes

def mostrar_menu():
    print(" ")
    print("*** MENÚ PRINCIPAL***")
    print(" ")
    print("1. Listado de todos los articulos y precios")
    print("2. Listado de todos los clientes")
    print("3. Listado de todas las ventas")
    print("4. Estadísticas de ventas por articulos")
    print("5. Estadísticas de ventas por clientes")
    print("6. Estadísticas de ventas por producto en específico ")
    print("7. Estadísticas de ventas por cliente en específico ")
    print("0. Salir")
        
    

bandera = True
while bandera:
    mostrar_menu()
    

    try:
        entrada = input("Seleccione su opción (1-8) \n").strip()
        if entrada == "":
            raise ValueError("Vacío")
        eleccion = int(entrada)
    except ValueError:
        print("Opción no válida. Intenta de nuevo.\n")
        continue  # vuelve a mostrar el menú principal

    if eleccion == 1:
        opcion1=True
        while opcion1:
            print("OPCIÓN 1")
            print("1. Imprimir listado de articulos")
            print("2. agregar articulo/s")
            print("3. Editar articulo/s")
            print("4. Eliminar articulo/s")
            print("0. Volver al menú principal")

            try:
                entrada = input("Seleccione su opción (1-5) \n").strip()
                if entrada == "":
                    raise ValueError("Vacío")
                opcion = int(entrada)
            except ValueError:
                print("Opción no válida. Intenta de nuevo.\n")
                continue  # vuelve a mostrar el submenú
                
            if opcion == 1:
                articulos.productos = [dict(zip(articulos.encabezado,fila))for fila in articulos.matriz_productos]
                for producto in articulos.productos:
                    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")

            elif opcion == 2:
                articulos.matriz_productos=articulos.agregar_producto(articulos.matriz_productos)
                articulos.productos = [dict(zip(articulos.encabezado,fila))for fila in articulos.matriz_productos]
                for producto in articulos.productos:
                    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")
            elif opcion == 3:
                articulos.matriz_productos=articulos.editar_producto(articulos.matriz_productos)
                articulos.productos = [dict(zip(articulos.encabezado,fila))for fila in articulos.matriz_productos]
                for producto in articulos.productos:
                    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")
            elif opcion == 4:
                articulos.matriz_productos=articulos.eliminar_producto(articulos.matriz_productos)
                articulos.productos = [dict(zip(articulos.encabezado,fila))for fila in articulos.matriz_productos]
                for producto in articulos.productos:
                    print(f"{producto['IDarticulo']:<5} | {producto['articulo']:<15} | ${producto['precio']:>10}")
            elif opcion == 0:
                opcion1 = False
            else: 
                print(" ")
                print("Opción no válida. Intenta de nuevo.")

    elif eleccion == 2:
        opcion2 = True
        while opcion2:
            print("OPCIÓN 2")
            print("1. Imprimir listado de clientes")
            print("2. agregar cliente/s")
            print("3. Editar cliente/s")
            print("4. Eliminar cliente/s")
            print("0. Volver al menú principal")
                
            try:
                entrada = input("Seleccione su opción (1-5) \n").strip()
                if entrada == "":
                    raise ValueError("Vacío")
                opcion = int(entrada)
            except ValueError:
                print("Opción no válida. Intenta de nuevo.\n")
                continue  # vuelve a mostrar el submenú

            if opcion == 1:
                for id_cliente, nombre_cliente in clientes.clientes.items():
                    print(f"{id_cliente:10} {nombre_cliente:4}")

            elif opcion == 2:
                clientes.clientes= clientes.agregar_cliente(clientes.clientes, clientes.idClientes)
                for id_cliente, nombre_cliente in clientes.clientes.items():
                    print(f"{id_cliente:10} {nombre_cliente:4}")

            elif opcion == 3:
                clientes.clientes = clientes.modificar_cliente(clientes.clientes)
                for id_cliente, nombre_cliente in clientes.clientes.items():
                    print(f"{id_cliente:10} {nombre_cliente:4}")

            elif opcion == 4:
                clientes.clientes= clientes.eliminar_cliente(clientes.clientes)
                for id_cliente, nombre_cliente in clientes.clientes.items():
                    print(f"{id_cliente:10} {nombre_cliente:4}")
            
            elif opcion == 0:
                opcion2 = False
            else: 
                print(" ")
                print("Opción no válida. Intenta de nuevo.")
    elif eleccion == 3:
        opcion3 = True
        while opcion3:
            print("OPCIÓN 3")
            print("1. Imprimir listado de ventas")
            print("2. agregar venta/s")
            print("3. Editar venta/s")
            print("4. Eliminar venta/s")
            print("0. Volver al menú principal")
                
            try:
                entrada = input("Seleccione su opción (1-5) \n").strip()
                if entrada == "":
                    raise ValueError("Vacío")
                opcion = int(entrada)
            except ValueError:
                print("Opción no válida. Intenta de nuevo.\n")
                continue  # vuelve a mostrar el submenú

            if opcion == 1:
                    for fila in ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, producto, importe, IDcliente = fila
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {producto:<15} | ${importe:<15} | {IDcliente:>10}")

            elif opcion == 2:
                ventas.matriz_ventas=ventas.agregar_venta(ventas.matriz_ventas)
                for fila in ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, producto, importe, IDcliente = fila
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {producto:<15} | ${importe:<15} | {IDcliente:>10}")

            elif opcion == 3:
                ventas.matriz_ventas=ventas.editar_venta(ventas.matriz_ventas)
                for fila in ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, producto, importe, IDcliente = fila
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {producto:<15} | ${importe:<15} | {IDcliente:>10}")

            elif opcion == 4:
                ventas.matriz_ventas=ventas.eliminar_venta(ventas.matriz_ventas)
                for fila in ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, producto, importe, IDcliente = fila
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {producto:<15} | ${importe:<15} | {IDcliente:>10}")
                        
            elif opcion == 0:
                opcion3 = False
            else: 
                print(" ")
                print("Opción no válida. Intenta de nuevo.")
    elif eleccion == 4:
        print("Hola opcion 4")
    elif eleccion == 5:
        print("Hola opcion 5")
    elif eleccion == 6:
        print("Hola opcion 6")
    elif eleccion == 7:
        print("Hola opcion 7")
    elif eleccion == 0:
        print("Saliste del programa.")
        bandera = False
    else:
        print(" ")
        print("Opción no válida. Intenta de nuevo.")


