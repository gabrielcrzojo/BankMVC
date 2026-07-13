from bottle import template
from app.models.conta import ContaModel
from app.models.transacao import TransacaoModel
from app.utils.auth import get_current_user

class DashboardController:
    def index(self):
        user = get_current_user()
        
        if user['tipo'] == 'admin':
            contas = ContaModel.get_all()
            transacoes = TransacaoModel.get_all()
        else:
            contas = ContaModel.get_by_usuario(user['id'])
            transacoes = TransacaoModel.get_by_usuario(user['id'])
        
        # Limitar a 5 últimas transações para o dashboard
        ultimas_transacoes = transacoes[:5]
        
        # Enriquecer transacoes
        contas_cache = {}
        def get_numero_conta(cid):
            if not cid: return "-"
            if cid not in contas_cache:
                c = ContaModel.get_by_id(cid)
                contas_cache[cid] = c['numero_conta'] if c else str(cid)
            return contas_cache[cid]
            
        for t in ultimas_transacoes:
            t['origem_str'] = get_numero_conta(t['conta_origem'])
            t['destino_str'] = get_numero_conta(t['conta_destino'])

        saldo_total = sum(c['saldo'] for c in contas)

        return template('app/views/html/dashboard', title="Dashboard", active_page="dashboard", user=user, contas=contas, saldo_total=saldo_total, ultimas_transacoes=ultimas_transacoes)
