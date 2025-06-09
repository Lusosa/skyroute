def verDestinos (cursor):
    import mysql.connector
    conexion = mysql.connector.connect(user='root', password='Eithan2605',host='localhost',database='skyroute',port='3306')
    cursor =conexion.cursor()
    cursor.execute("SELECT * FROM destinos")
    destinos= cursor.fetchall()
    if destinos:
            print("Destinos:")
            for destino in destinos:
                print(f"codigoDestino: {destino[0]}, Pais: {destino[1]}, Ciudad: {destino[2]}, CP: {destino[3]}")
    else:
            print("No hay Destinos.")


def agregarDestino (cursor, conexion, lista ):
        cursor.execute("""
        INSERT INTO destinos (pais, ciudad, codigo_postal) 
        VALUES (%s, %s, %s)
        """, (lista[0], lista[1], lista[2]))
        conexion.commit()
        print("Destino agregado exitosamente.")

def mostrarDestino (cursor, codDestino):
        cursor.execute("SELECT * FROM destinos WHERE cod_destino = %s", (codDestino,)) #Acá hay código SQL
        destino = cursor.fetchone()
        print(destino)


def modificarDestino(cursor, conexion,lista):
        cursor.execute("""
        UPDATE destinos
        SET ciudad = %s, pais = %s , codigo_postal = %s
        WHERE cod_destino = %s
        """, (lista[1], lista[2],lista[0],lista[3]))
        conexion.commit()
        print("Se modifico correctamente el destino")

def eliminarDestino(cursor, conexion , codDestino):
        cursor.execute("DELETE FROM destinos WHERE cod_destino = %s", (codDestino,)) #Acá hay código SQL
        conexion.commit()
        if cursor.rowcount > 0:
            print("Destino eliminada exitosamente.")
        else:
            print("No se encontró ningun destino con ese codigo.")
