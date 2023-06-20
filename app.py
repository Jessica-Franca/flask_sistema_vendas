from flask import Flask, Blueprint, render_template, request, url_for, session
from routes.usuario import usuario_blueprint

class UI:
    def __init__(self):
        #configuração padrão
        self.app = Flask(__name__)
        self.app.secret_key = 'salt'
        
        #Ablitando rotas
        self.app.register_blueprint(usuario_blueprint)

    def run(self):
        self.app.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    ui = UI()
    ui.run()