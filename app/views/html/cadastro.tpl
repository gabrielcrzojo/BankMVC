% rebase('app/views/html/base.tpl', title='Criar Conta', active_page='cadastro')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-user-plus"></i> Cadastro
        </div>
        <h2>Crie sua <span class="gradient-text">Conta</span></h2>
    </div>

    <div class="contact-form-container glass-card" style="max-width: 500px; margin: 0 auto;">
        % if defined('erro') and erro:
        <div class="alert alert-error" style="background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #ef4444; padding: 10px; border-radius: 8px; margin-bottom: 20px;">
            <i class="fa-solid fa-circle-exclamation"></i> {{erro}}
        </div>
        % end

        <form action="/cadastro" method="POST" class="contact-form">
            <div class="form-group">
                <label for="nome">Nome Completo</label>
                <input type="text" id="nome" name="nome" required placeholder="Seu nome">
            </div>

            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" id="email" name="email" required placeholder="seu@email.com">
            </div>
            
            <div class="form-group">
                <label for="senha">Senha</label>
                <input type="password" id="senha" name="senha" required placeholder="Sua senha">
            </div>
            
            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 10px;">Cadastrar</button>
        </form>
        
        <div style="text-align: center; margin-top: 20px; color: var(--text-secondary);">
            Já tem conta? <a href="/login" style="color: var(--primary-color);">Faça login</a>
        </div>
    </div>
</section>
