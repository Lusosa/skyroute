def conexion1 ():
    import mysql.connector

    conexion = mysql.connector.connect(user='root', password='Eithan2605',host='localhost',database='sky_route',port='3306')
    print(conexion)
    return conexion.cursor()


