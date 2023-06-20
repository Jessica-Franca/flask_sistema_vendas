from flask import render_template, request,  redirect
from flask import session as cache

class UsuarioAuth:
    def usuario_login():            
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            print(email)
            
            #Validação de acesso:
            if email == 'teste@teste.com.br' and senha == '1234':
                cache['control']['email'] = email
                cache['control']['senha'] = senha
                print(cache)
                return redirect('/')
        return render_template('usuario/usuario_login.html')      
