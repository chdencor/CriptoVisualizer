from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models.dbBorker import Usuario
from app import db

login_bp = Blueprint('login', __name__, template_folder='../views/templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Si el usuario ya está logueado, redirigir al home
    if 'user_id' in session:
        return redirect(url_for('home.index'))

    if request.method == 'POST':
        nombre_usuario = request.form.get('nombre_usuario')
        contraseña = request.form.get('contraseña')

        # Buscar al usuario en la base de datos utilizando db.session
        usuario = db.session.query(Usuario).filter_by(nombre_usuario=nombre_usuario).first()

        if usuario and check_password_hash(usuario.contraseña, contraseña):
            # Iniciar sesión
            session['user_id'] = usuario.id
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('home.index'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.', 'danger')

    return render_template('login.html')
