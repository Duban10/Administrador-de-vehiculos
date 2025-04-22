from flask import Blueprint, request, jsonify
from db.connection import get_connection

concesionarios_bp = Blueprint('concesionario', __name__)

# POST - Crear un cliente   
@concesionarios_bp.route('/concesionario', methods=['POST'])
def create_concesionario():
    data = request.json
    print(f"data:::", data)
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.Concesionarios (ConcesionarioID, Nombre, Direccion, Ciudad)
            VALUES (?, ?, ?, ?)
        """, (data['ConcesionarioID'], data['Nombre'], data['Direccion'], data['Ciudad']))
        conn.commit()
        return jsonify({"message": "Concesionario creado con éxito"})
    except Exception as e:
        print(f"Error al crear el concesionario: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()
    
@concesionarios_bp.route('/concesionario', methods=['GET'])
def get_concesionarios():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.Concesionarios")

        columnas = [col[0] for col in cursor.description]
        resultados = [dict(zip(columnas, row)) for row in cursor.fetchall()]
        return jsonify(resultados)
    except Exception as e:
        print(f"Errorrrr: {str(e)}")
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

# PUT - Actualizar concesionario
@concesionarios_bp.route('/concesionario/<int:id>', methods=['PUT'])
def update_concesionario(id):
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE dbo.Concesionarios
            SET Nombre = ?, Direccion = ?, Ciudad = ?
            WHERE ConcesionarioID = ?
        """, (data['Nombre'], data['Direccion'], data['Ciudad'], id))
        conn.commit()
        return jsonify({"message": "Concesionario actualizado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

# DELETE - Eliminar cliente
@concesionarios_bp.route('/concesionario/<int:id>', methods=['DELETE'])
def delete_concesionario(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dbo.Concesionarios WHERE ConcesionarioID = ?", (id,))
        conn.commit()
        return jsonify({"message": "Concesionario eliminado con éxito"})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        conn.close()

