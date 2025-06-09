def verClientes (cursor):
    cursor.execute("SELECT * FROM CLIENTES")
    personas= cursor.fetchall()
    if personas:
         print("Clientes:")
         for persona in personas:
            print(f"codigo: {persona[0]}, Nombre: {persona[1]}, Apellido: {persona[2]}, DNI: {persona[3]}, Direccion: {persona[4]}, Fecha nacimiento: {persona[5]}, Mail: {persona[6]}, Telefono: {persona[7]}")
    else:
         print("No hay clientes.")


def agregarCliente(cursor, conexion, lista):
    cursor.execute("""
        INSERT INTO clientes (nombre_cliente, apellido_cliente, dni_cliente, direccion_cliente, fecha_nacimiento_cliente, mail_cliente, telefono_cliente)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6]))
    conexion.commit()
    print("Se agregó correctamente el cliente.")

def mostrarCliente (cursor, dni):
    cursor.execute("SELECT * FROM clientes WHERE dni_cliente = %s", (dni,)) #Acá hay código SQL
    persona = cursor.fetchone()
    print(persona)


def modificarCliente(cursor, conexion,lista): #UPDATE es la actualizacion de el cliente, el formato en el que lo pasamos es una lista donde le pasamos los datos que queremos modificar.
    cursor.execute("""
    UPDATE clientes  
    SET nombre_cliente = %s, apellido_cliente = %s, direccion_cliente = %s, fecha_nacimiento_cliente = %s, mail_cliente = %s, telefono_cliente = %s
    WHERE dni_cliente = %s
    """, (lista[0], lista[1], lista[3], lista[4], lista[5], lista[6], lista[2]))
    conexion.commit()
    print("Se modifico correctamente el cliente")

def eliminarCliente(cursor, conexion , dni):
    cursor.execute("DELETE FROM clientes WHERE dni_cliente = %s", (dni,)) #Acá hay código SQL
    conexion.commit()
    if cursor.rowcount > 0:
        print("Persona eliminada exitosamente.")
    else:
        print("No se encontró ninguna persona con ese DNI.")