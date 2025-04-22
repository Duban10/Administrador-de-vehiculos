from flask import Blueprint, request, jsonify
from db.connection import get_connection

clientes_bp = Blueprint('clientes', __name__)

# POST - Crear un cliente   
@clientes_bp.route('/clientes', methods=['POST'])
def create_cliente():
    data = request.json
    print(f"data:::", data)
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.Clientes (ClienteID, Nombre, Email, Telefono)
            VALUES (?, ?, ?, ?)
        """, (data['ClienteID'], data['Nombre'], data['Email'], data['Telefono']))
        conn.commit()
        return jsonify({"message": "Cliente creado con éxito"})
    except Exception as e:
        print(f"Error al crear el cliente: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.Clientes")

        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]

        return jsonify(resultados)
    except Exception as e:
        print(f"Errorrrr: {str(e)}")
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

# PUT - Actualizar cliente
@clientes_bp.route('/clientes/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE dbo.Clientes
            SET Nombre = ?, Email = ?, Telefono = ?
            WHERE ClienteID = ?
        """, (data['Nombre'], data['Email'], data['Telefono'], id))
        conn.commit()
        return jsonify({"message": "Cliente actualizado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# DELETE - Eliminar cliente
@clientes_bp.route('/clientes/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dbo.Clientes WHERE ClienteID = ?", (id,))
        conn.commit()
        return jsonify({"message": "Cliente eliminado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

