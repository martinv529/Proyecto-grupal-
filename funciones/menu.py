import ventas 

def mostrar_menu():
    print(" ")
    print("*** MENÚ ***")
    print(" ")
    print("1. Listado de todos los articulos y precios")
    print("2. Listado de todos los clientes")
    print("3. Listado de todas las ventas")
    print("4. Estadísticas de ventas por articulos")
    print("5. Estadísticas de ventas por clientes")
    print("6. Estadísticas de ventas por producto en específico ")
    print("7. Estadísticas de ventas por cliente en específico ")
    print("8. Salir")
        
    

    bandera = True
    while bandera:
        

        try:
            entrada = input("Seleccione su opción (1-8) \n").strip()
            if entrada == "":
                raise ValueError("Vacío")
            eleccion = int(entrada)
        except ValueError:
            print("Opción no válida. Intenta de nuevo.\n")
            continue  # vuelve a mostrar el menú principal

        if eleccion == 1:
            while True:
                print("1. Imprimir listado de articulos")
                print("2. agregar articulo/s")
                print("3. Editar articulo/s")
                print("4. Eliminar articulo/s")
                print("5. Volver al menú principal")

                try:
                    entrada = input("Seleccione su opción (1-5) \n").strip()
                    if entrada == "":
                        raise ValueError("Vacío")
                    opcion = int(entrada)
                except ValueError:
                    print("Opción no válida. Intenta de nuevo.\n")
                    continue  # vuelve a mostrar el submenú
                    
                if opcion == 1:
                    print("Opcion 1")
                elif opcion == 2:
                    print("Opcion 2")
                elif opcion == 3:
                    print("Opcion 3")
                elif opcion == 4:
                    print("Opcion 4")
                elif opcion == 5:
                    break
                else: 
                    print(" ")
                    print("Opción no válida. Intenta de nuevo.")

        elif eleccion == 2:
            while True:
                print("1. Imprimir listado de clientes")
                print("2. agregar cliente/s")
                print("3. Editar cliente/s")
                print("4. Eliminar cliente/s")
                print("5. Volver al menú principal")
                    
                try:
                    entrada = input("Seleccione su opción (1-5) \n").strip()
                    if entrada == "":
                        raise ValueError("Vacío")
                    opcion = int(entrada)
                except ValueError:
                    print("Opción no válida. Intenta de nuevo.\n")
                    continue  # vuelve a mostrar el submenú

                if opcion == 1:
                    print("Opcion 1")
                elif opcion == 2:
                    print("Opcion 2")
                elif opcion == 3:
                    print("Opcion 3")
                elif opcion == 4:
                    print("Opcion 4")
                elif opcion == 5:
                    break 
                else: 
                    print(" ")
                    print("Opción no válida. Intenta de nuevo.")
        elif eleccion == 3:
            while True:
                print("1. Imprimir listado de ventas")
                print("2. agregar venta/s")
                print("3. Editar venta/s")
                print("4. Eliminar venta/s")
                print("5. Volver al menú principal")
                    
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
                    ventas.agregar_venta(ventas.matriz_ventas)
                elif opcion == 3:
                    ventas.editar_venta_venta(ventas.matriz_ventas)
                elif opcion == 4:
                    ventas.eliminar_venta_venta(ventas.matriz_ventas)
                elif opcion == 5:
                    break 
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
        elif eleccion == 8:
            print("Saliste del programa.")
            bandera = False
        else:
            print(" ")
            print("Opción no válida. Intenta de nuevo.")


mostrar_menu()