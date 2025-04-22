from flask import Blueprint, request, jsonify
from db.connection import get_connection

transacciones_bp = Blueprint('transacciones', __name__)

# POST - Crear un cliente   
@transacciones_bp.route('/transacciones', methods=['POST'])
def create_transaccion():
    data = request.json
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dbo.Transacciones (TransaccionID, VehiculoID, ClienteID, ConcesionarioID, FechaVenta, PrecioVenta)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (data['TransaccionID'], data['VehiculoID'], data['ClienteID'], data['ConcesionarioID'], data['FechaVenta'], data['PrecioVenta']))
        conn.commit()
        return jsonify({"message": "Transacción creada con éxito"})
    except Exception as e:
        print(f"Error al crear la transacción: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()