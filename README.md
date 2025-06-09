Este módulo se encarga de mostrar los menús principales y submenús, manejar la interacción con el usuario y orquestar las llamadas a funciones de gestión de clientes, destinos y ventas que interactúan con la base de datos MySQL.
El sistema SkyRoute permite la gestión básica de clientes, destinos y ventas de pasajes aéreos. Se conecta a una base de datos MySQL para persistir la información. La lógica de negocio para las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) se encuentra modularizada en los módulos Gestion_Clientes, Gestion_Destinos y Gestion_Ventas.
Dependencias
mysql.connector: Módulo de Python para conectarse a bases de datos MySQL.
Gestion_Clientes: Módulo que contiene funciones para la gestión de clientes (ver, agregar, modificar, eliminar).
Gestion_Destinos: Módulo que contiene funciones para la gestión de destinos (ver, agregar, modificar, eliminar).
Gestion_Ventas: Módulo que contiene funciones para la gestión de ventas (registrar, ver, anular/botón de arrepentimiento).
El programa opera en un bucle principal (while condicion:) que muestra el menú principal de opciones:

Gestionar Clientes: Accede al submenú para operaciones con clientes.
Gestionar Destinos: Accede al submenú para operaciones con destinos.
Gestionar Ventas: Accede al submenú para operaciones con ventas.
Salir: Finaliza la ejecución del programa.
Al seleccionar la opción 1 del menú principal, se entra en un submenú para la gestión de clientes, que permite las siguientes acciones:

1. Ver Clientes: Llama a Gestion_Clientes.verClientes(cursor) para mostrar la lista de clientes registrados en la base de datos.

Nota: Las variables respuestaCliente, respuestaDestino, respuestaVenta y las impresiones asociadas ("El cliente existente es: \n") parecen ser remanentes de una versión anterior del código que no usaba la base de datos de forma persistente y podrían ser eliminadas si no se utilizan para otros fines. La información real de los clientes se obtiene de la base de datos a través de Gestion_Clientes.verClientes(cursor).
2. Agregar Cliente: Solicita al usuario los datos del nuevo cliente (nombre, apellido, documento, dirección, fecha de nacimiento, mail, teléfono) y los pasa a Gestion_Clientes.agregarCliente(cursor, conexion, lista).

3. Modificar Cliente:

Primero, muestra la lista de clientes existentes (Gestion_Clientes.verClientes(cursor)) para que el usuario pueda identificar el cliente a modificar.
Solicita el DNI del cliente a modificar.
Solicita los nuevos datos para nombre, apellido, dirección, fecha de nacimiento, mail y teléfono.
Llama a Gestion_Clientes.modificarCliente(cursor, conexion, lista) con los datos actualizados y el DNI para realizar la modificación en la base de datos.
4. Eliminar Cliente:

Solicita el DNI del cliente a eliminar.
Llama a Gestion_Clientes.eliminarCliente(cursor, conexion, dni) para borrar el cliente de la base de datos.
Nota: Similar al punto de "Ver Clientes", la línea respuestaCliente=None parece ser un remanente y no afecta la eliminación de la base de datos.
5. Volver al Menú Principal: Sale del submenú de gestión de clientes.

Python

# Lógica para la opción 1 (Gestionar Clientes)
if respuesta == 1:
    while respuestaDos != 5:
        # ... (código para mostrar el submenú de clientes) ...
        if respuestaDos == 1:
            Gestion_Clientes.verClientes(cursor)
        elif respuestaDos == 2:
            # ... (código para solicitar datos y llamar a agregarCliente) ...
        elif respuestaDos == 3:
            # ... (código para solicitar datos y llamar a modificarCliente) ...
        elif respuestaDos == 4:
            # ... (código para solicitar DNI y llamar a eliminarCliente) ...
        # ... (manejo de opciones incorrectas)
        Al seleccionar la opción 2 del menú principal, se entra en un submenú para la gestión de destinos, que permite las siguientes acciones:

1. Ver Destino: Llama a Gestion_Destinos.verDestinos(cursor) para mostrar la lista de destinos registrados en la base de datos.

Nota: La variable respuestaDestino y las impresiones asociadas ("El destino es: \n") son remanentes, la información actual se obtiene de la base de datos.
2. Agregar Destino: Solicita al usuario el país, ciudad y código postal del nuevo destino, y los pasa a Gestion_Destinos.agregarDestino(cursor, conexion, lista).

3. Modificar Destino:

Muestra los destinos existentes (Gestion_Destinos.verDestinos(cursor)).
Solicita el código del destino a modificar.
Solicita los nuevos datos para país, ciudad y código postal.
Llama a Gestion_Destinos.modificarDestino(cursor, conexion, lista) con los datos actualizados y el código del destino.
4. Eliminar Destino:

Solicita el código del destino a eliminar.
Llama a Gestion_Destinos.eliminarDestino(cursor, conexion, codigo_destino) para borrar el destino de la base de datos.
Nota: La línea respuestaDestino=None es un remanente.
5. Volver al Menú Principal: Sale del submenú de gestión de destinos.

Python

# Lógica para la opción 2 (Gestionar Destinos)
if respuesta == 2:
    while respuestaDos != 5:
        # ... (código para mostrar el submenú de destinos) ...
        if respuestaDos == 1:
            Gestion_Destinos.verDestinos(cursor)
        elif respuestaDos == 2:
            # ... (código para solicitar datos y llamar a agregarDestino) ...
        elif respuestaDos == 3:
            # ... (código para solicitar datos y llamar a modificarDestino) ...
        elif respuestaDos == 4:
            # ... (código para solicitar código y llamar a eliminarDestino) ...
        # ... (manejo de opciones incorrectas) ...
Submenú de Gestión de Ventas (Opción 3)
Al seleccionar la opción 3 del menú principal, se entra en un submenú para la gestión de ventas, que permite las siguientes acciones:

1. Agregar Venta: Solicita al usuario el código del cliente, código del destino y el precio de la venta. El estado_venta se inicializa a 0 (presumiblemente para "activa" o "pendiente"). Estos datos se pasan a Gestion_Ventas.registrarVenta(cursor, conexion, lista).

2. Listado de Ventas: Llama a Gestion_Ventas.verVentas(cursor) para mostrar todas las ventas registradas.

3. Botón de Arrepentimiento:

Solicita el código de la venta que se desea anular.
Llama a Gestion_Ventas.botonArrepentimiento(cursor, conexion, codigo_venta) para cambiar el estado de la venta en la base de datos (presumiblemente a "anulada").
5. Volver al Menú Principal: Sale del submenú de gestión de ventas.
Salida del Programa (Opción 8)
Si el usuario selecciona la opción 8 en el menú principal, la variable condicion se establece en False, terminando el bucle principal. Se imprime un mensaje de despedida.
Manejo de Entradas Inválidas
Si el usuario ingresa una opción fuera del rango permitido en el menú principal (respuesta < 1 or respuesta > 8) o en los submenús (respuestaDos !=5 and respuestaDos>5), se muestra un mensaje de "opción incorrecta".

