% rebase('app/views/html/base.tpl', title='Sobre Nós', active_page='sobre')

<section class="container">
    <div class="about-wrapper">
        <div class="about-text">
            <div class="hero-badge">
                <i class="fa-solid fa-users"></i> Quem Somos
            </div>
            <h2>Nascemos para <span class="gradient-text">simplificar</span> sua vida financeira.</h2>
            <p>O BankMVC foi criado como parte de um projeto acadêmico incremental na Universidade de Brasília (UnB), projetado para ilustrar na prática o poder da arquitetura MVC (Model-View-Controller) aplicada a sistemas de missão crítica, como bancos digitais.</p>
            <p>Nossa missão é demonstrar que a complexidade de transações financeiras e dados sensíveis de usuários pode ser gerenciada com elegância, modularidade e clareza de código. Acreditamos que a tecnologia deve ser transparente e acessível.</p>
            
            <div class="stats-container">
                <div class="stat-item">
                    <h3>50k+</h3>
                    <p>Clientes Ativos</p>
                </div>
                <div class="stat-item">
                    <h3>R$ 10M+</h3>
                    <p>Transacionados</p>
                </div>
                <div class="stat-item">
                    <h3>99.9%</h3>
                    <p>Uptime do App</p>
                </div>
            </div>
        </div>
        
        <div class="about-img-container">
            <div class="hero-card-mockup" style="transform: rotate(-5deg); height: 260px; width: 340px; margin-bottom: 20px;">
                <div class="card-top">
                    <span class="card-brand">BankMVC</span>
                    <i class="fa-solid fa-microchip" style="font-size: 1.5rem;"></i>
                </div>
                <p style="color: white; font-size: 0.95rem; line-height: 1.4;">"A simplicidade é o último grau da sofisticação."</p>
                <div style="font-size: 0.8rem; text-align: right; opacity: 0.8;">- Leonardo da Vinci</div>
            </div>
            
            <div class="glass-card about-badge-card">
                <div class="about-badge-num">100%</div>
                <div>
                    <h4 style="margin-bottom: 4px;">Código Seguro</h4>
                    <p style="font-size: 0.8rem;">Lógica limpa e protegida</p>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="container" style="background: rgba(99, 102, 241, 0.02); border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color);">
    <div class="section-header">
        <h2>Nossos Valores Fundamentais</h2>
        <p>Pilares que norteiam nossa engenharia de software e relacionamento com clientes.</p>
    </div>
    
    <div class="features-grid">
        <div class="feature-card glass-card">
            <div class="feature-icon"><i class="fa-solid fa-code"></i></div>
            <h3>Clareza Arquitetural</h3>
            <p>Seguimos rigidamente o padrão MVC para garantir que cada componente faça apenas uma coisa, e faça bem.</p>
        </div>
        <div class="feature-card glass-card">
            <div class="feature-icon"><i class="fa-solid fa-user-shield"></i></div>
            <h3>Privacidade Absoluta</h3>
            <p>Seus dados pertencem a você. Usamos padrões modernos de proteção para salvaguardar suas informações pessoais.</p>
        </div>
        <div class="feature-card glass-card">
            <div class="feature-icon"><i class="fa-solid fa-rotate"></i></div>
            <h3>Inovação Contínua</h3>
            <p>Do Nível I ao Nível IV, implementamos tecnologias inovadoras, como WebSockets para tempo real e SQLite para persistência.</p>
        </div>
    </div>
</section>
