from opcion3 import opcion_3
from opcion4 import opcion_4
from opcion5 import opcion_5
from opcion6 import opcion_6
from sub_opcion1_1 import sub_opcion1_1
from sub_opcion1_2 import sub_opcion1_2
from sub_opcion1_3 import sub_opcion1_3
from sub_opcion1_4 import sub_opcion1_4
from sub_opcion2_1 import sub_opcion2_1
from sub_opcion2_2 import sub_opcion2_2
from sub_opcion2_3 import sub_opcion2_3
from sub_opcion2_4 import sub_opcion2_4

def mostrar_menu():
    print(" ")
    print("*** MENÚ ***")
    print(" ")
    print("1. Listado de todos los articulos y precio")
    print("2. Listado de todos los clientes")
    print("3. Listado de todas las ventas")
    print("4. Estadísticas de ventas por articulos")
    print("5. Estadísticas de ventas por clientes")
    print("6. Estadísticas de ventas por producto en específico ")
    print("7. Estadísticas de ventas por cliente en específico ")
    print("8. Salir")

bandera = True
while bandera:
    mostrar_menu()
    
    try:
        entrada = input("Seleccione su opción (1-7) \n").strip()
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
                sub_opcion1_1()
            elif opcion == 2:
                sub_opcion1_2()
            elif opcion == 3:
                sub_opcion1_3()
            elif opcion == 4:
                sub_opcion1_4()
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
                sub_opcion2_1()
            elif opcion == 2:
                sub_opcion2_2()
            elif opcion == 3:
                sub_opcion2_3()
            elif opcion == 4:
                sub_opcion2_4()
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
                sub_opcion2_1()
            elif opcion == 2:
                sub_opcion2_2()
            elif opcion == 3:
                sub_opcion2_3()
            elif opcion == 4:
                sub_opcion2_4()
            elif opcion == 5:
                break 
            else: 
                    print(" ")
                    print("Opción no válida. Intenta de nuevo.")
    elif eleccion == 4:
        opcion_4()
    elif eleccion == 5:
        opcion_5()
    elif eleccion == 6:
        opcion_6()
    elif eleccion == 7:
        opcion_6()
    elif eleccion == 8:
        print("Saliste del programa.")
        bandera = False
    else:
        print(" ")
        print("Opción no válida. Intenta de nuevo.")