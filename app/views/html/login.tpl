% rebase('app/views/html/base.tpl', title='Acessar Conta', active_page='login')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-lock"></i> Autenticação
        </div>
        <h2>Acesse sua <span class="gradient-text">Conta</span></h2>
    </div>

    <div class="contact-form-container glass-card" style="max-width: 400px; margin: 0 auto;">
        % if defined('erro') and erro:
        <div class="alert alert-error" style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #ef4444; padding: 10px; border-radius: 8px; margin-bottom: 20px;">
            <i class="fa-solid fa-circle-exclamation"></i> {{erro}}
        </div>
        % end

        <form action="/login" method="POST" class="contact-form">
            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" required placeholder="seu@email.com">
            </div>
            
            <div class="form-group">
                <label for="senha">Senha</label>
                <input type="password" id="senha" name="senha" required placeholder="Sua senha">
            </div>
            
            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 10px;">Entrar</button>
        </form>
        
        <div style="text-align: center; margin-top: 20px; color: var(--text-secondary);">
            Ainda não tem conta? <a href="/cadastro" style="color: var(--primary-color);">Crie uma aqui</a>
        </div>
    </div>
</section>
