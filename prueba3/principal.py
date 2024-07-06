from prueba_prueba import registro_de_prestamo, listar_prestamos,imprimir_resibo_prestamo,salir
#llamamos al modulo y importamos todas las funciones
prestamos = []
#creamos una lista para almacenar todos los prestamos

while True :
    #creamos un menu de inicio 
    print("menu\n")
    print("1- registro de pedido\n")
    print("2- listas de pedidos\n")
    print("3- imprimir recibo de prestamo\n")
    print("4-salir de programa\n")

    opcion=int(input("ingrese una de las cuatro opciones\n"))
#una variable para ingresar a la opncion indicada
    if opcion == 1 :
        registro_de_prestamo(prestamos)
    
    elif opcion == 2 :
        listar_prestamos(prestamos)

    elif opcion == 3 :
        imprimir_resibo_prestamo(prestamos)
        
    elif opcion == 4 :
        salir()
        break

    else :
        print(" opcion ingresada no es valida\n")
#le damos direccion a la opcion escogida con las condiciones




