import os
class Config:

    # Configuración de la base de datos
    DATABASE_URL = os.getenv("DATABASE_URL")

    # Configuración de la clave secreta
    SECRET_KEY = os.getenv("SECRET_KEY")