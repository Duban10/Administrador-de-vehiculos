import pyodbc

def get_connection(): 
    try:
        # La función pyodbc.connect() se encarga de establecer la conexión con la base de datos.
        # Los parámetros que se le pasan son:
        # - DRIVER: el nombre del driver a utilizar para la conexión. En este caso, el driver de SQL Server.
        # - SERVER: el nombre del servidor en donde se encuentra la base de datos.
        # - DATABASE: el nombre de la base de datos a la que se desea conectar.
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=WIN10-LD9N3EEFB;DATABASE=VentasVehiculos')
        print("Conexión exitosa")
        return connection
    except Exception as e:
        print(f"Error al conectar la base de datos: {str(e)}")