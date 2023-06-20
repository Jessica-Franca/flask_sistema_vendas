from flask import Blueprint, render_template

vendas_blueprint = Blueprint('vendas', __name__, template_folder='/vendas') 

@vendas_blueprint.route('/vendas')
def vendas_index():
    return render_template('vendas/vendas_index.html')

@vendas_blueprint.route('/vendas/criar')
def vendas_criar():
    return render_template('vendas/vendas_criar.html')

@vendas_blueprint.route('/vendas/editar/<id_venda>')
def vendas_editar(id_venda):
    return render_template('vendas/vendas_editar.html')

@vendas_blueprint.route('/vendas/excluir/<id_venda>')
def vendas_excluir(id_venda):
    return render_template('vendas/vendas_excluir.html')