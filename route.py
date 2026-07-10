from app.controllers.application import Application
from app.controllers.conta_controller import ContaController
from app.controllers.transacao_controller import TransacaoController
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template, response


app = Bottle()
ctl = Application()
conta_ctl = ContaController()
transacao_ctl = TransacaoController()


#-----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


#-----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/')
def home():
    return ctl.render('home')

@app.route('/sobre')
def sobre():
    return ctl.render('sobre')

@app.route('/servicos')
def servicos():
    return ctl.render('servicos')

@app.route('/contato')
def contato():
    return ctl.render('contato')

@app.route('/contas')
def contas():
    return conta_ctl.index()

@app.route('/contas/nova', method=['GET', 'POST'])
def contas_nova():
    return conta_ctl.create()

@app.route('/contas/deletar/<conta_id:int>', method=['POST', 'GET'])
def contas_deletar(conta_id):
    return conta_ctl.delete(conta_id)

@app.route('/contas/editar/<conta_id:int>', method=['GET', 'POST'])
def contas_editar(conta_id):
    return conta_ctl.edit(conta_id)

@app.route('/transacoes')
def transacoes():
    return transacao_ctl.index()

@app.route('/transacoes/nova', method=['GET', 'POST'])
def transacoes_nova():
    return transacao_ctl.create()

#-----------------------------------------------------------------------------


if __name__ == '__main__':

    run(app, host='0.0.0.0', port=8080, debug=True)
