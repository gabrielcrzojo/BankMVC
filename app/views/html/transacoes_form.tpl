% rebase('app/views/html/base.tpl', title='Nova Transação', active_page='transacoes')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-money-bill-transfer"></i> Movimentar
        </div>
        <h2>Nova <span class="gradient-text">Transação</span></h2>
    </div>

    <div class="contact-form-container glass-card" style="max-width: 600px; margin: 0 auto;">
        % if defined('erro') and erro:
        <div class="alert alert-error" style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #ef4444; padding: 10px; border-radius: 8px; margin-bottom: 20px;">
            <i class="fa-solid fa-circle-exclamation"></i> {{erro}}
        </div>
        % end
        
        % if defined('sucesso') and sucesso:
        <div class="alert alert-success" style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; color: #10b981; padding: 10px; border-radius: 8px; margin-bottom: 20px;">
            <i class="fa-solid fa-circle-check"></i> {{sucesso}}
        </div>
        % end

        <form action="/transacoes/nova" method="POST" class="contact-form" id="transacao-form">
            <div class="form-group">
                <label for="tipo">Tipo de Transação</label>
                <select id="tipo" name="tipo" required onchange="toggleCamposTransacao()">
                    <option value="deposito">Depósito</option>
                    <option value="saque">Saque</option>
                    <option value="transferencia">Transferência</option>
                </select>
            </div>

            <div class="form-group" id="grp-origem" style="display: none;">
                <label for="conta_origem">Conta de Origem</label>
                <select id="conta_origem" name="conta_origem">
                    <option value="">Selecione uma conta...</option>
                    % for c in contas:
                    <option value="{{c['id']}}">{{c['numero_conta']}} (Saldo: R$ {{"%.2f" % c['saldo']}})</option>
                    % end
                </select>
            </div>

            <div class="form-group" id="grp-destino">
                <label for="conta_destino">Conta de Destino</label>
                <select id="conta_destino" name="conta_destino">
                    <option value="">Selecione uma conta...</option>
                    % for c in contas:
                    <option value="{{c['id']}}">{{c['numero_conta']}}</option>
                    % end
                </select>
            </div>
            
            <div class="form-group">
                <label for="valor">Valor (R$)</label>
                <input type="number" id="valor" name="valor" step="0.01" min="0.01" required>
            </div>
            
            <div class="form-group">
                <label for="descricao">Descrição (Opcional)</label>
                <input type="text" id="descricao" name="descricao" placeholder="Ex: Pagamento de aluguel">
            </div>
            
            <div style="display: flex; gap: 10px; margin-top: 20px;">
                <a href="/transacoes" class="btn btn-secondary" style="flex: 1; text-align: center;">Voltar</a>
                <button type="submit" class="btn btn-primary" style="flex: 1;">Confirmar Transação</button>
            </div>
        </form>
    </div>
</section>

<script>
function toggleCamposTransacao() {
    const tipo = document.getElementById('tipo').value;
    const grpOrigem = document.getElementById('grp-origem');
    const grpDestino = document.getElementById('grp-destino');
    const selOrigem = document.getElementById('conta_origem');
    const selDestino = document.getElementById('conta_destino');

    if (tipo === 'deposito') {
        grpOrigem.style.display = 'none';
        grpDestino.style.display = 'block';
        selOrigem.required = false;
        selDestino.required = true;
    } else if (tipo === 'saque') {
        grpOrigem.style.display = 'block';
        grpDestino.style.display = 'none';
        selOrigem.required = true;
        selDestino.required = false;
    } else if (tipo === 'transferencia') {
        grpOrigem.style.display = 'block';
        grpDestino.style.display = 'block';
        selOrigem.required = true;
        selDestino.required = true;
    }
}

// Call on load to set initial state
document.addEventListener('DOMContentLoaded', toggleCamposTransacao);
</script>
