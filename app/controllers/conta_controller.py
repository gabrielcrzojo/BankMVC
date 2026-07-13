from bottle import template, request, redirect
from app.models.conta import ContaModel
from app.utils.auth import get_current_user

class ContaController:
    def index(self):
        user = get_current_user()
        if user and user['tipo'] == 'admin':
            contas = ContaModel.get_all()
        else:
            contas = ContaModel.get_by_usuario(user['id']) if user else []
        return template('app/views/html/contas_list', contas=contas, title="Contas", active_page="contas", user=user)

    def create(self):
        user = get_current_user()
        if not user:
            redirect('/login')
            
        if request.method == 'GET':
            return template('app/views/html/contas_form', title="Nova Conta", active_page="contas", erro=None, conta=None, user=user)
        
        # POST
        numero = request.forms.get('numero_conta')
        nome = user['nome']
        sobrenome = ''
        saldo_inicial = request.forms.get('saldo_inicial')
        
        try:
            saldo_inicial = float(saldo_inicial) if saldo_inicial else 0.0
        except ValueError:
            return template('app/views/html/contas_form', title="Nova Conta", active_page="contas", erro="Saldo inválido.", conta=None, user=user)

        sucesso = ContaModel.create(numero, user['id'], nome, sobrenome, saldo_inicial)
        if sucesso:
            redirect('/contas')
        else:
            return template('app/views/html/contas_form', title="Nova Conta", active_page="contas", erro="Número de conta já existe.", conta=None, user=user)

    def edit(self, conta_id):
        user = get_current_user()
        conta = ContaModel.get_by_id(conta_id)
        
        # Se for admin, passa direto. Se não, verifica se é o dono.
        if not conta or (user and user['tipo'] != 'admin' and conta['usuario_id'] != user['id']):
            redirect('/contas')
            
        if request.method == 'GET':
            return template('app/views/html/contas_form', title="Editar Conta", active_page="contas", erro=None, conta=conta, user=user)
            
        # POST
        numero = request.forms.get('numero_conta')
        nome = user['nome']
        sobrenome = ''
        
        sucesso, erro = ContaModel.update_info(conta_id, numero, nome, sobrenome)
        if sucesso:
            redirect('/contas')
        else:
            return template('app/views/html/contas_form', title="Editar Conta", active_page="contas", erro=erro, conta=conta, user=user)

    def delete(self, conta_id):
        user = get_current_user()
        conta = ContaModel.get_by_id(conta_id)
        if conta and user and (user['tipo'] == 'admin' or conta['usuario_id'] == user['id']):
            ContaModel.delete(conta_id)
        redirect('/contas')
