<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} | BMVC Bank</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Main Style -->
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar">
        <a href="/" class="nav-logo">
            <i class="fa-solid fa-building-columns"></i>
            <span>BMVC <span style="font-weight: 300;">Bank</span></span>
        </a>

        <ul class="nav-links" id="nav-links">
            <li><a href="/" class="{{'active' if active_page == 'home' else ''}}">Home</a></li>
            <li><a href="/sobre" class="{{'active' if active_page == 'sobre' else ''}}">Sobre Nós</a></li>
            <li><a href="/servicos" class="{{'active' if active_page == 'servicos' else ''}}">Serviços</a></li>
            <li><a href="/contato" class="{{'active' if active_page == 'contato' else ''}}">Contato</a></li>
        </ul>

        <div class="nav-actions">
            <button class="btn-icon" id="theme-toggle" aria-label="Toggle Theme">
                <i class="fa-solid fa-moon"></i>
            </button>
            <button class="btn btn-primary">
                Abra sua Conta <i class="fa-solid fa-arrow-right"></i>
            </button>
        </div>

        <div class="hamburger" id="hamburger">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        {{!base}}
    </main>

    <!-- Floating Back to Top Button -->
    <button class="back-to-top" id="back-to-top" aria-label="Back to Top">
        <i class="fa-solid fa-arrow-up"></i>
    </button>

    <!-- Footer -->
    <footer>
        <div class="footer-top">
            <div class="footer-brand">
                <a href="/" class="nav-logo">
                    <i class="fa-solid fa-building-columns"></i>
                    <span>BMVC <span style="font-weight: 300;">Bank</span></span>
                </a>
                <p>O BMVC Bank é um banco digital inovador construído sob a arquitetura BMVC (Bottle MVC). Simplicidade, segurança e performance para gerenciar seu dinheiro.</p>
                <div class="footer-socials">
                    <a href="#" class="btn-icon"><i class="fa-brands fa-facebook"></i></a>
                    <a href="#" class="btn-icon"><i class="fa-brands fa-instagram"></i></a>
                    <a href="#" class="btn-icon"><i class="fa-brands fa-twitter"></i></a>
                    <a href="#" class="btn-icon"><i class="fa-brands fa-linkedin"></i></a>
                </div>
            </div>
            
            <div class="footer-links-col">
                <h4>Serviços</h4>
                <ul>
                    <li><a href="/servicos">Conta Corrente</a></li>
                    <li><a href="/servicos">Pix & Transferências</a></li>
                    <li><a href="/servicos">Cartão Black</a></li>
                    <li><a href="/servicos">Investimentos</a></li>
                </ul>
            </div>
            
            <div class="footer-links-col">
                <h4>Empresa</h4>
                <ul>
                    <li><a href="/sobre">Sobre Nós</a></li>
                    <li><a href="#">Carreiras</a></li>
                    <li><a href="#">Imprensa</a></li>
                    <li><a href="#">Segurança</a></li>
                </ul>
            </div>
            
            <div class="footer-links-col">
                <h4>Suporte</h4>
                <ul>
                    <li><a href="/contato">Fale Conosco</a></li>
                    <li><a href="#">FAQ</a></li>
                    <li><a href="#">Ouvidoria</a></li>
                </ul>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p>&copy; 2026 BMVC Bank. Desenvolvido para a disciplina de Orientação a Objetos (UnB).</p>
        </div>
    </footer>

    <!-- Scripts -->
    <script src="/static/js/main.js"></script>
</body>
</html>
