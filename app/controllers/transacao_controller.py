from bottle import template, request, redirect
from app.models.transacao import TransacaoModel
from app.models.conta import ContaModel
from app.utils.auth import get_current_user

class TransacaoController:
    def index(self):
        user = get_current_user()
        if not user:
            redirect('/login')
            
        if user['tipo'] == 'admin':
            transacoes = TransacaoModel.get_all()
        else:
            transacoes = TransacaoModel.get_by_usuario(user['id'])
            
        # Enriquecer as transações com os números das contas para exibir bonitinho
        contas_cache = {}
        def get_numero_conta(cid):
            if not cid: return "-"
            if cid not in contas_cache:
                c = ContaModel.get_by_id(cid)
                contas_cache[cid] = c['numero_conta'] if c else str(cid)
            return contas_cache[cid]
            
        for t in transacoes:
            t['origem_str'] = get_numero_conta(t['conta_origem'])
            t['destino_str'] = get_numero_conta(t['conta_destino'])

        return template('app/views/html/transacoes_list', transacoes=transacoes, title="Transações", active_page="transacoes", user=user)

    def create(self):
        user = get_current_user()
        if not user:
            redirect('/login')
            
        todas_contas = ContaModel.get_all()
        if user['tipo'] == 'admin':
            contas_usuario = todas_contas
        else:
            contas_usuario = [c for c in todas_contas if c['usuario_id'] == user['id']]
        
        if request.method == 'GET':
            return template('app/views/html/transacoes_form', contas=todas_contas, contas_usuario=contas_usuario, title="Nova Transação", active_page="transacoes", erro=None, sucesso=None, user=user)
        
        # POST
        tipo = request.forms.get('tipo')
        conta_origem_id = request.forms.get('conta_origem')
        conta_destino_id = request.forms.get('conta_destino')
        valor = request.forms.get('valor')
        descricao = request.forms.getunicode('descricao') or ''
        
        try:
            valor = float(valor)
        except (ValueError, TypeError):
            return template('app/views/html/transacoes_form', contas=todas_contas, contas_usuario=contas_usuario, title="Nova Transação", active_page="transacoes", erro="Valor inválido.", sucesso=None, user=user)

        sucesso = False
        mensagem = ""

        # Verificar se conta de origem pertence ao usuário (ou se é admin)
        if conta_origem_id:
            c_origem = ContaModel.get_by_id(int(conta_origem_id))
            if not c_origem or (user['tipo'] != 'admin' and c_origem['usuario_id'] != user['id']):
                return template('app/views/html/transacoes_form', contas=todas_contas, contas_usuario=contas_usuario, title="Nova Transação", active_page="transacoes", erro="Conta de origem não pertence ao usuário logado.", sucesso=None, user=user)

        if tipo == 'deposito':
            if not conta_destino_id:
                mensagem = "Conta de destino é obrigatória para depósito."
            else:
                sucesso, mensagem = TransacaoModel.depositar(int(conta_destino_id), valor, descricao)
                
        elif tipo == 'saque':
            if not conta_origem_id:
                mensagem = "Conta de origem é obrigatória para saque."
            else:
                sucesso, mensagem = TransacaoModel.sacar(int(conta_origem_id), valor, descricao)
                
        elif tipo == 'transferencia':
            if not conta_origem_id or not conta_destino_id:
                mensagem = "Conta de origem e destino são obrigatórias para transferência."
            else:
                sucesso, mensagem = TransacaoModel.transferir(int(conta_origem_id), int(conta_destino_id), valor, descricao)
        else:
            mensagem = "Tipo de transação inválido."

        if sucesso:
            # Retorna pro form com mensagem de sucesso
            return template('app/views/html/transacoes_form', contas=todas_contas, contas_usuario=contas_usuario, title="Nova Transação", active_page="transacoes", erro=None, sucesso=mensagem, user=user)
        else:
            # Retorna pro form com mensagem de erro
            return template('app/views/html/transacoes_form', contas=todas_contas, contas_usuario=contas_usuario, title="Nova Transação", active_page="transacoes", erro=mensagem, sucesso=None, user=user)
