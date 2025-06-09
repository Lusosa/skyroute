##def verClientes(dni):
#import Config
import Gestion_Clientes
import Gestion_Destinos
import Gestion_Ventas
import mysql.connector
conexion = mysql.connector.connect(user='root', password='Eithan2605',host='localhost',database='skyroute',port='3306')
cursor =conexion.cursor()
respuesta=-1
respuestaDos=-1
condicion= True
respuestaCliente=None
respuestaDestino=None
respuestaVenta=None
while condicion:
    respuesta=0
    
    print("Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes") #ACA MOSTRAMOS EL MENU
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("8. Salir")
    respuestaDos=-1
    respuesta=int(input("ingrese una opcion: "))

    
   
    if respuesta==1:
            while respuestaDos !=5:
                print("GESTIONAR CLIENTES")
                print("1. Ver Clientes")
                print("2. Agregar Cliente")
                print("3. Modificar Cliente")
                print("4. Eliminar Cliente")
                print("5. Volver al Menu Principal")           
                respuestaDos=int(input("ingrese una opcion: "))
                if respuestaDos == 1:
                  Gestion_Clientes.verClientes(cursor) #Aqui se mostraran los clientes
              
                  if respuestaCliente != None:
                     print("El cliente existente es: \n", respuestaCliente)
                  else:
                       print("No ingresaron ningun cliente todavia\n")
                if respuestaDos == 2:
                  nombre = input("Nuevo nombre: ")
                  apellido = input("Nuevo apellido: ")
                  documento = input("Nuevo documento: ")
                  direccion = input("Nueva dirección: ")
                  fecha_nacimiento = input("Nueva fecha de nacimiento (YYYY-MM-DD): ")
                  mail = input("Nuevo mail: ")
                  telefono = input("Nuevo teléfono: ")
                  lista = [nombre, apellido, documento, direccion, fecha_nacimiento, mail, telefono]
                  Gestion_Clientes.agregarCliente(cursor, conexion, lista)
                if respuestaDos == 3:
                  Gestion_Clientes.verClientes(cursor)  # Mostrar clientes disponibles
                  
                  dni = input("Ingrese el DNI del cliente que desea modificar: ")

                  # Pedir nuevos datos
                  nombre = input("Nuevo nombre: ")
                  apellido = input("Nuevo apellido: ")
                  direccion = input("Nueva dirección: ")
                  fecha_nacimiento = input("Nueva fecha de nacimiento (YYYY-MM-DD): ")
                  mail = input("Nuevo mail: ")
                  telefono = input("Nuevo teléfono: ")

                  # Armar la lista en el orden correcto
                  lista = [nombre, apellido, dni, direccion, fecha_nacimiento, mail, telefono]

                  Gestion_Clientes.modificarCliente(cursor, conexion, lista) #Le pasamos cursor y conexion que es parte de la conexion a la base de datos y en lista armamos los datos del cliente que estamos esperado dentro del UPDATE.
                  print("\nCliente modificado correctamente")
                if respuestaDos == 4:  
                  
                  dni = str(input("Ingresa DNI del cliente a eliminar: \n"))
                  print() #Aca solicitamos el DNI para saber que cliente eliminar
                  Gestion_Clientes.eliminarCliente(cursor, conexion, dni)
                  print("Cliente ha sido eliminado ")                               
                if respuestaDos !=5 and respuestaDos>5:
                 print("por favor ingrese una opcion correcta")
                 
    if respuesta==2:
        while respuestaDos !=5:
                 print("GESTIONAR DESTINOS")
                 print("1. Ver Destino")
                 print("2. Agregar Destino")
                 print("3. Modificar Destino")
                 print("4. Eliminar Destino")
                 print("5. Volver al Menu Principal")
                 respuestaDos=int(input("ingrese una opcion: "))
                 if respuestaDos == 1:
                  respuestaDestino = Gestion_Destinos.verDestinos(cursor)
                  if respuestaDestino != None:
                          print("El destino es: \n", respuestaDestino)  #AQUI GESTIONAMOS LOS DESTINOS
                  else:
                          print("No ingresaron ningun destino todavia\n")
                 if respuestaDos == 2:
                                pais = input("Ingrese el pais del destino a agregar: ")
                                ciudad = input("Ingrese la ciudad del destino a agregar: ")
                                CodigoPostal = int(input("Ingrese el codigo postal del destino a agregar: "))
                                lista = [pais , ciudad , CodigoPostal]
                                Gestion_Destinos.agregarDestino(cursor,conexion,lista)
                                print()
                                print("Agregado con exito \n")
                 if respuestaDos == 3:
                                Gestion_Destinos.verDestinos(cursor)  # Mostrar destinos disponibles
                  
                                codigo_destino = int(input("Ingrese el codigo del destino que desea modificar: "))

                                # Pedir nuevos datos
                                pais = input("Ingrese nuevo pais: ")
                                ciudad = input("Ingrese nueva ciudad: ")
                                codigo_postal = int(input("Ingrese el nuevo codigo postal: "))
                                

                                # Armar la lista en el orden correcto
                                lista = [codigo_postal, ciudad, pais , codigo_destino]

                                Gestion_Destinos.modificarDestino(cursor, conexion, lista)
                                print("Ha sido modificado correctamente: \n")
                                print()
                               
                 if respuestaDos == 4:  
                                codigo_destino = int(input("ingresa el codigo destino a eliminar: \n"))
                                Gestion_Destinos.eliminarDestino(cursor , conexion , codigo_destino)
                                print()
                                respuestaDestino=None
                                                             
                 if respuestaDos !=5 and respuestaDos>5:
                                print("por favor ingrese una opcion correcta")
                 

    if respuesta == 3:
      while respuestaDos != 5:
          print("GESTIONAR VENTAS")
          print("1. Agregar venta")
          print("2. Listado de ventas")
          print("3. Boton de arrepentimiento")
          print("5. Volver al Menú Principal")
          respuestaDos = int(input("Ingrese una opción: "))  #AQUI GESTIONAMOS LAS VENTAS

          if respuestaDos == 1:
              print("\n--- Agregar Venta ---")
              codigo_cliente = int(input("Código del cliente: "))
              codigo_destino = int(input("Código del destino: "))
              precio = int(input("Precio: "))
              estado_venta = 0
              lista = [codigo_cliente, codigo_destino, precio, estado_venta]
              Gestion_Ventas.registrarVenta(cursor, conexion, lista)

              print()

          elif respuestaDos == 2:
              print("\n--- Listado de Ventas ---")
              Gestion_Ventas.verVentas(cursor)
              print()
          elif respuestaDos == 3:
            print("\n--- Boton de Arrepentimiento ---")
            codigo_venta = int(input("Ingrese el codigo de la venta que desea anular: "))
            Gestion_Ventas.botonArrepentimiento(cursor, conexion, codigo_venta) #LISTADO DE VENTAS Y AÑADIMOS BOTON DE ARREPENTIMIENTO
            print()


          elif respuestaDos != 5:
              print("Por favor ingrese una opción correcta.")
    if respuesta==8:
          condicion=False  
    if respuesta<1 or respuesta>8:
            print("opcion incorrecta, intente nuevamente ")                 
print("Gracias por comprar con SkyRoute") 
