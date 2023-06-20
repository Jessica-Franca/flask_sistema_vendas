from flask import Blueprint, render_template, session
from models.page_model.usuario.usuario import UsuarioAuth

usuario_blueprint = Blueprint('usuario', __name__, template_folder='templates')

@usuario_blueprint.route('/usuario_login' , methods = ['GET','POST'])
def usuario_login():
    return UsuarioAuth.usuario_login()


@usuario_blueprint.route('/')
def usuario_index():
    #session.pop limpa a session
    session.pop('email',None)
    session.pop('senha',None)
    session.pop('control',None)
    return render_template('usuario/usuario_index.html')


@usuario_blueprint.route('/usuario/criar')
def usuario_criar():
    return render_template('usuario/usuario_criar.html')

@usuario_blueprint.route('/usuario/editar/<id_usuario>')
def usuario_editar(id_usuario):
    return render_template('usuario/usuario_editar.html')

@usuario_blueprint.route('/usuario/excluir/<id_usuario>')
def usuario_excluir(id_usuario):
    return render_template('usuario/usuario_excluir.html')
