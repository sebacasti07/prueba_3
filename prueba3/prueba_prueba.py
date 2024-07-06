def registro_de_prestamo(prestamos):
        #creamos una funcion de registro de cada prestamo en parametros de todo los prestamos
        
        nombre = input("Ingrese nombre del cliente: \n")
        while len(nombre) < 4:
         nombre=input("El nombre debe tener al menos 4 caracteres ej castell: \n") 
        #validaciones
        while nombre.isspace():
         nombre=input("El nombre debe tener al menos 4 caracteres sin espacios ej castell:  \n")
            #validaciones
        apellido = input("Ingrese apellido del cliente: ")
        while len(apellido) < 4:
          apellido=input("El nombre debe tener al menos 4 caracteres ej castell:  \n")
             #validacion
        while apellido.isspace():
          apellido=input("El nombre debe tener al menos 4 caracteres sin espacios ej castell: \n")
            #validaciones
        while True: 
            try:
                id_del_libro = int(input("Ingrese ID del libro: \n"))
                break  
            except ValueError:
                print("Debe ingresar un número entero para el ID del libro: \n")
                #validacionnes
        
        fecha_prestamo = input("Ingrese fecha de prestamo ej:07/07/24:  \n")
        #validaciones
        while len(fecha_prestamo) < 8:
          fecha_prestamo=input("la fecha debe tener al menos 8 caracteres ej 07/07/24:  \n")
            #validaciones
        
        while fecha_prestamo.isspace():
          fecha_prestamo=input("la fecha debe tener al menos 8 caracteres sin espacios ej 07/07/24: \n")
            #validaciones
        fecha_devolucion = input("Ingrese fecha de devolucion: \n")
        #validaciones
        while len(fecha_devolucion) < 8:
          fecha_devolucion=input("El nombre debe tener al menos 8 caracteres ej 07/07/24 :  \n")
            #validaciones
        
        while fecha_devolucion.isspace():
         fecha_devolucion=input("la fecha debe tener al menos 4 caracteres sin espacios ej 07/07/24 : \n")
            #validaciones
        
        prestamo = {
            "nombre": nombre,
            "apellido": apellido,
            "id_del_libro": id_del_libro,
            "fecha_prestamo": fecha_prestamo,
            "fecha_devolucion": fecha_devolucion
        }
        #creamos un diccionario para guardar cada pedido
        prestamos.append(prestamo)
        #agregamos cada unidad de prestamo para que se almacene prestamos
        print("Registro ingresado correctamente \n")


def listar_prestamos(prestamos):
  #creamos otra funciones para crear una funcion para detallar los pedidos 
  if not prestamos:
   print("No existen prestamos registrados \n")
   return

  
  for prestamo in prestamos :
   #recorremos los elementos de cada prestamo dentro de toda la lista de prestamos
   print(f"Nombre:  {prestamo['nombre']} Apellido:  {prestamo['apellido']}")
   print(f"ID libro: {prestamo['id_del_libro']}")
   print(f"Fecha de prestamo: {prestamo['fecha_prestamo']}")
   print(f"Fecha de devolucion: {prestamo['fecha_devolucion']} ")
   #se leen los valores de cada diccionario y listas


def imprimir_resibo_prestamo(prestamos):
    if not prestamos:
     print("No hay prestamos registrados \n")
     #si no hay prestamo se imprime..el mensaje
  
    id_=int(input("ingrese ID "))
    buscador_de_prestamos=[prestamo for prestamo in prestamos if prestamo['id_del_libro'] == id_ ]
    #buscador hace que se encuentre y recorra el elemento del diccionario prestamos en el valor id del libro
    #dentro de las listas de prestam
 
    if not buscador_de_prestamos:
     print(f"No existe ese prestamo para {id_}\n")

    with open(f"recibo_de_prestamo_de{id_}.txt","w") as recibo:
     #abrimos un archivo txt para cada recibo dandole el permiso 
     #de escritura y un alias de recibo

     for prestamo in buscador_de_prestamos:
      #recorrimos la lista de todos los prestamos con el buscador y todo sus elementos
      recibo.write(f"Recibo del prestamo \n")
      recibo.write(f" Nombre: {prestamo['nombre']} {prestamo['apellido']} \n")
      recibo.write(f" ID Libro: {prestamo['id_del_libro']} \n ")
      recibo.write(f"Fecha de prestamo {prestamo['fecha_prestamo']} \n ")
      recibo.write(f"Fecha de devolucion {prestamo['fecha_devolucion']} \n")
      recibo.write("\n")
      #al archivo txt escribira todo lo de arriba

def salir():
 print("saliendo del programa\n")
 #funcion para salir del programas ..











 

 

 










def salir():
  print("saliendo del programa")
 
   
 

