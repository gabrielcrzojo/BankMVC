from bottle import template, request, redirect, response
from app.models.usuario import UsuarioModel
from app.utils.auth import get_current_user

class AuthController:
    def login(self):
        user = get_current_user()
        if user:
            redirect('/dashboard')
            
        if request.method == 'GET':
            return template('app/views/html/login', title="Login", erro=None)
            
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        
        user = UsuarioModel.authenticate(email, senha)
        if user:
            response.set_cookie('session_id', str(user['id']), secret='bmvc-secret', path='/')
            redirect('/dashboard')
        else:
            return template('app/views/html/login', title="Login", erro="E-mail ou senha inválidos.")

    def cadastro(self):
        user = get_current_user()
        if user:
            redirect('/dashboard')
            
        if request.method == 'GET':
            return template('app/views/html/cadastro', title="Cadastro", erro=None)
            
        nome = request.forms.get('nome')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        
        sucesso, erro = UsuarioModel.create(nome, email, senha)
        if sucesso:
            # Login automático
            user = UsuarioModel.authenticate(email, senha)
            response.set_cookie('session_id', str(user['id']), secret='bmvc-secret', path='/')
            redirect('/dashboard')
        else:
            return template('app/views/html/cadastro', title="Cadastro", erro=erro)

    def logout(self):
        response.delete_cookie('session_id', path='/')
        redirect('/')
