# from routes.vehiculos import vehiculos_bp
from flask import Flask
from flask_cors import CORS
from routes.clientes import clientes_bp
from routes.vehiculos import vehiculos_bp
from routes.concesionarios import concesionarios_bp
from routes.transacciones import transacciones_bp

# se registra cada una de las rutas en la app principal

app = Flask(__name__)  # Nos permitira registrar las rutas para que sean consumidas desde nuestra aplicacion cliente.

CORS(app)  # habilita el soporte para peticiones Cross-Origin Resource Sharing (CORS) en la aplicacion. Esto permite que una pagina web realice peticiones HTTP a un servidor que no sea el que la sirvio, lo que es necesario cuando se consume una API desde una aplicacion cliente.

# Registrar rutas
app.register_blueprint(clientes_bp)
app.register_blueprint(vehiculos_bp)
app.register_blueprint(concesionarios_bp)
app.register_blueprint(transacciones_bp)

# Iniciar el servidor
if __name__ == '__main__':  # esto es una variable que se utiliza para indicar el punto de entrada principal de un script de Python. Si el script se esta ejecutando directamente (no se esta importando como modulo en otro script), entonces __name__ es igual a '__main__'. De otra manera, __name__ es el nombre del modulo.
    app.run(debug=True, port=5000)