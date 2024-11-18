from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from app.models.dbBorker import Usuario
from app import db

signin_bp = Blueprint('signin', __name__, template_folder='../views/templates')

@signin_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    # Si el usuario ya está logueado, redirigir al home
    if 'user_id' in session:
        return redirect(url_for('home.index'))

    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        contraseña = request.form.get('contraseña')

        # Verificar que no exista un usuario con el mismo nombre
        usuario_existente = db.session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()

        if usuario_existente:
            flash('El nombre de usuario ya está en uso.', 'danger')
        else:
            # Crear un nuevo usuario
            nuevo_usuario = Usuario(
                nombre_usuario=nombre_usuario,
                contraseña=generate_password_hash(contraseña)
            )
            db.session.add(nuevo_usuario)  # Agregar el usuario a la sesión
            db.session.commit()  # Confirmar los cambios en la base de datos
            flash('Cuenta creada con éxito. Inicia sesión.', 'success')
            return redirect(url_for('login.login'))

    return render_template('signin.html')
