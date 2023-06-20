from flask import Blueprint, render_template

produto_blueprint = Blueprint('produto', __name__, template_folder='templates')

@produto_blueprint.route('/produto')
def produto_index():
    return render_template('produto/produto_index.html')

@produto_blueprint.route('/produto/criar')
def produto_criar():
    return render_template('produto/produto_criar.html')

@produto_blueprint.route('/produto/editar/<id_produto>')
def produto_editar(id_produto):
    return render_template('produto/produto_editar.html')

@produto_blueprint.route('/produto/excluir/<id_produto>')
def produto_excluir(id_produto):
    return render_template('produto/produto_excluir.html')