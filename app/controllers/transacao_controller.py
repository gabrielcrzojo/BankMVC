from bottle import template, request, redirect
from app.models.transacao import TransacaoModel
from app.models.conta import ContaModel

class TransacaoController:
    def index(self):
        transacoes = TransacaoModel.get_all()
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

        return template('app/views/html/transacoes_list', transacoes=transacoes, title="Transações", active_page="transacoes")

    def create(self):
        contas = ContaModel.get_all()
        
        if request.method == 'GET':
            return template('app/views/html/transacoes_form', contas=contas, title="Nova Transação", active_page="transacoes", erro=None, sucesso=None)
        
        # POST
        tipo = request.forms.get('tipo')
        conta_origem_id = request.forms.get('conta_origem')
        conta_destino_id = request.forms.get('conta_destino')
        valor = request.forms.get('valor')
        descricao = request.forms.getunicode('descricao') or ''
        
        try:
            valor = float(valor)
        except (ValueError, TypeError):
            return template('app/views/html/transacoes_form', contas=contas, title="Nova Transação", active_page="transacoes", erro="Valor inválido.", sucesso=None)

        sucesso = False
        mensagem = ""

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
            return template('app/views/html/transacoes_form', contas=contas, title="Nova Transação", active_page="transacoes", erro=None, sucesso=mensagem)
        else:
            # Retorna pro form com mensagem de erro
            return template('app/views/html/transacoes_form', contas=contas, title="Nova Transação", active_page="transacoes", erro=mensagem, sucesso=None)
