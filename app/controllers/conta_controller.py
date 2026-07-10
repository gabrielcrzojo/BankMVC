from bottle import template, request, redirect
from app.models.conta import ContaModel
import sqlite3

# Função utilitária para pegar o id do usuário mock do DB para o nível II
def get_mock_user_id():
    conn = sqlite3.connect('database/bmvc.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM Usuario WHERE email = ?', ('gabriel@bankmvc.com',))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else 1

class ContaController:
    def index(self):
        contas = ContaModel.get_all()
        return template('app/views/html/contas_list', contas=contas, title="Contas", active_page="contas")

    def create(self):
        if request.method == 'GET':
            return template('app/views/html/contas_form', title="Nova Conta", active_page="contas", erro=None, conta=None)
        
        # POST
        numero = request.forms.get('numero_conta')
        nome = request.forms.getunicode('nome') or ''
        sobrenome = request.forms.getunicode('sobrenome') or ''
        saldo_inicial = request.forms.get('saldo_inicial')
        
        try:
            saldo_inicial = float(saldo_inicial) if saldo_inicial else 0.0
        except ValueError:
            return template('app/views/html/contas_form', title="Nova Conta", active_page="contas", erro="Saldo inválido.", conta=None)

        usuario_id = get_mock_user_id()
        
        sucesso = ContaModel.create(numero, usuario_id, nome, sobrenome, saldo_inicial)
        if sucesso:
            redirect('/contas')
        else:
            return template('app/views/html/contas_form', title="Nova Conta", active_page="contas", erro="Número de conta já existe.", conta=None)

    def edit(self, conta_id):
        conta = ContaModel.get_by_id(conta_id)
        if not conta:
            redirect('/contas')
            
        if request.method == 'GET':
            return template('app/views/html/contas_form', title="Editar Conta", active_page="contas", erro=None, conta=conta)
            
        # POST
        numero = request.forms.get('numero_conta')
        nome = request.forms.getunicode('nome') or ''
        sobrenome = request.forms.getunicode('sobrenome') or ''
        
        sucesso, erro = ContaModel.update_info(conta_id, numero, nome, sobrenome)
        if sucesso:
            redirect('/contas')
        else:
            return template('app/views/html/contas_form', title="Editar Conta", active_page="contas", erro=erro, conta=conta)

    def delete(self, conta_id):
        ContaModel.delete(conta_id)
        redirect('/contas')
