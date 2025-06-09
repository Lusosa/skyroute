def registrarVenta(cursor, conexion, lista):
    cursor.execute("""
    INSERT INTO ventas (codigo_cliente, codigo_destino, precio, estado_venta) 
    VALUES (%s, %s, %s, %s)
    """, (lista[0], lista[1], lista[2], lista[3]))
    conexion.commit()
    print("Venta agregada exitosamente.")


def verVentas(cursor):
    cursor.execute("SELECT * FROM ventas")
    ventas = cursor.fetchall()
    if ventas:
        print("Ventas:")
        for venta in ventas:
            estado = "Activa" if venta[5] == 0 else "Anulada"
            print(f"codigoVenta: {venta[0]}, codigoCliente: {venta[1]}, codigoDestino: {venta[2]}, fechaVenta: {venta[3]}, precio: {venta[4]}, estado: {estado}")
    else:
        print("No hay ventas.")

from datetime import datetime

def botonArrepentimiento(cursor, conexion, codigo_venta):
    cursor.execute("SELECT fecha_venta, estado_venta FROM ventas WHERE codigo_venta = %s", (codigo_venta,))
    venta = cursor.fetchone()

    if not venta:
        print("No se encontró una venta con ese código.")
        return

    fecha_venta, estado_actual = venta
    ahora = datetime.now()
    diferencia = ahora - fecha_venta

    if diferencia.total_seconds() <= 60:
        if estado_actual == 0:
            cursor.execute("UPDATE ventas SET estado_venta = 1 WHERE codigo_venta = %s", (codigo_venta,))
            conexion.commit()
            print("La venta ha sido anulada exitosamente (boton de arrepentimiento).")
        else:
            print("La venta ya estaba anulada.")
    else:
        print("Ya paso el tiempo permitido para arrepentirse de la venta.")
