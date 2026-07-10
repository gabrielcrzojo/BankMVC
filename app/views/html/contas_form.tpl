% rebase('app/views/html/base.tpl', title=title, active_page='contas')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid {{'fa-pen' if conta else 'fa-plus'}}"></i> {{title}}
        </div>
        <h2>{{'Editar' if conta else 'Criar'}} <span class="gradient-text">Conta Bancária</span></h2>
    </div>

    <div class="contact-form-container glass-card" style="max-width: 600px; margin: 0 auto;">
        % if defined('erro') and erro:
        <div class="alert alert-error" style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #ef4444; padding: 10px; border-radius: 8px; margin-bottom: 20px;">
            <i class="fa-solid fa-circle-exclamation"></i> {{erro}}
        </div>
        % end

        <form action="{{'/contas/editar/' + str(conta['id']) if conta else '/contas/nova'}}" method="POST" class="contact-form">
            <div class="form-group">
                <label for="nome">Nome do Titular</label>
                <input type="text" id="nome" name="nome" placeholder="Ex: João" value="{{conta['nome'] if conta else ''}}" required>
            </div>
            
            <div class="form-group">
                <label for="sobrenome">Sobrenome do Titular</label>
                <input type="text" id="sobrenome" name="sobrenome" placeholder="Ex: Silva" value="{{conta['sobrenome'] if conta else ''}}" required>
            </div>

            <div class="form-group">
                <label for="numero_conta">Número da Conta</label>
                <input type="text" id="numero_conta" name="numero_conta" placeholder="Ex: 12345-6" value="{{conta['numero_conta'] if conta else ''}}" required>
            </div>
            
            % if not conta:
            <div class="form-group">
                <label for="saldo_inicial">Saldo Inicial (R$)</label>
                <input type="number" id="saldo_inicial" name="saldo_inicial" step="0.01" min="0" value="0.00" required>
            </div>
            % end
            
            <div style="display: flex; gap: 10px; margin-top: 20px;">
                <a href="/contas" class="btn btn-secondary" style="flex: 1; text-align: center;">Cancelar</a>
                <button type="submit" class="btn btn-primary" style="flex: 1;">{{'Salvar Alterações' if conta else 'Criar Conta'}}</button>
            </div>
        </form>
    </div>
</section>
