# routes/vehiculos.py
from flask import Blueprint, request, jsonify
from db.connection import get_connection

vehiculos_bp = Blueprint('vehiculos', __name__) # Nos permite registrar las rutas para que sean consumidas desde nuestra aplicacion cliente.

# POST - Crear un vehículo
@vehiculos_bp.route('/vehiculos', methods=['POST'])
def create_vehiculo():
    data = request.json
    print(f"data:::", data)
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.Vehiculos (VehiculoID, Marca, Modelo, Anio, Precio)
            VALUES (?, ?, ?, ?, ?)
        """, (data['VehiculoID'], data['Marca'], data['Modelo'], data['Anio'], data['Precio']))
        conn.commit() # Nos permite guardar los cambios en la base de datos.
        return jsonify({"message": "Vehículo creado con éxito"})
    except Exception as e:
        print(f"Error al crear el vehículo: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

# GET - Obtener todos los vehículos
@vehiculos_bp.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.Vehiculos")
        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description] # Nos permite obtener los nombres de las columnas de la tabla.
        vehiculos = [dict(zip(columns, row)) for row in rows] # Nos permite convertir los resultados de la consulta en un formato JSON.

        return jsonify(vehiculos)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# GET - Obtener vehiculo por id
@vehiculos_bp.route('/vehiculos/<int:id>', methods=['GET'])
def get_vehiculos_by_id(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.Vehiculos WHERE VehiculoID = ?", (id,))
        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        vehiculos = [dict(zip(columns, row)) for row in rows]

        return jsonify(vehiculos)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()


# PUT - Actualizar vehículo
@vehiculos_bp.route('/vehiculos/<int:id>', methods=['PUT'])
def update_vehiculo(id):
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE dbo.Vehiculos
            SET Marca = ?, Modelo = ?, Anio = ?, Precio = ?
            WHERE VehiculoID = ?
        """, (data['Marca'], data['Modelo'], data['Anio'], data['Precio'], id))
        conn.commit()
        return jsonify({"message": "Vehículo actualizado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# DELETE - Eliminar vehículo
@vehiculos_bp.route('/vehiculos/<int:id>', methods=['DELETE'])
def delete_vehiculo(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dbo.Vehiculos WHERE VehiculoID = ?", (id,))
        conn.commit()
        return jsonify({"message": "Vehículo eliminado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()
