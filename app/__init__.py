from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Inicializar la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    load_dotenv('db_url.env')

    # Obtener la URL de la base de datos desde las variables de entorno    
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("DATABASE_URL no está definida en db_url.env. Asegúrate de configurarla correctamente.")
    print("DATABASE_URL:", database_url)

    # Crear la aplicación Flask
    app = Flask(__name__)

    # Configuraciones de la aplicación
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configurar la clave secreta desde el .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Inicializar la base de datos
    db.init_app(app)

    # Registrar los blueprints (controladores)
    with app.app_context():
        from app.controllers.home_controller import home_bp
        from app.controllers.cripto_controller import crypto_bp
        from app.controllers.logIn_controller import login_bp
        from app.controllers.signIn_controller import signin_bp

        app.register_blueprint(home_bp)
        app.register_blueprint(crypto_bp)
        app.register_blueprint(login_bp)
        app.register_blueprint(signin_bp)

    # Punto de retorno de la aplicación
    return app
