% rebase('app/views/html/base.tpl', title='Contato', active_page='contato')

<section class="container">
    <div class="section-header">
        <div class="hero-badge">
            <i class="fa-solid fa-envelope"></i> Central de Contato
        </div>
        <h2>Entre em <span class="gradient-text">contato</span> conosco.</h2>
        <p>Tem alguma dúvida, crítica ou sugestão? Envie uma mensagem. Nosso time responderá em até 24 horas.</p>
    </div>
    
    <div class="contact-wrapper">
        <!-- Contact Info column -->
        <div class="contact-info">
            <div class="contact-info-card glass-card">
                <div class="contact-info-icon">
                    <i class="fa-solid fa-location-dot"></i>
                </div>
                <div>
                    <h4 style="margin-bottom: 6px;">Endereço</h4>
                    <p style="font-size: 0.9rem;">Campus Universitário Darcy Ribeiro, Asa Norte, Brasília - DF, CEP 70910-900</p>
                </div>
            </div>
            
            <div class="contact-info-card glass-card">
                <div class="contact-info-icon">
                    <i class="fa-solid fa-phone"></i>
                </div>
                <div>
                    <h4 style="margin-bottom: 6px;">Telefone</h4>
                    <p style="font-size: 0.9rem;">0800 123 4567 (Ligação Gratuita)</p>
                    <p style="font-size: 0.9rem;">+55 (61) 3107-3300 (Geral)</p>
                </div>
            </div>
            
            <div class="contact-info-card glass-card">
                <div class="contact-info-icon">
                    <i class="fa-solid fa-envelope"></i>
                </div>
                <div>
                    <h4 style="margin-bottom: 6px;">E-mail</h4>
                    <p style="font-size: 0.9rem;">suporte@bmvcbank.com</p>
                    <p style="font-size: 0.9rem;">parcerias@bmvcbank.com</p>
                </div>
            </div>
        </div>
        
        <!-- Contact Form column -->
        <div class="contact-form-container glass-card">
            <form action="#" method="POST" class="contact-form" onsubmit="event.preventDefault(); alert('Mensagem enviada com sucesso! Agradecemos seu contato.'); this.reset();">
                <div class="form-group">
                    <label for="name">Nome Completo</label>
                    <input type="text" id="name" name="name" placeholder="Digite seu nome completo" required>
                </div>
                
                <div class="form-group">
                    <label for="email">E-mail</label>
                    <input type="email" id="email" name="email" placeholder="exemplo@email.com" required>
                </div>
                
                <div class="form-group">
                    <label for="subject">Assunto</label>
                    <input type="text" id="subject" name="subject" placeholder="Qual o motivo do contato?" required>
                </div>
                
                <div class="form-group">
                    <label for="message">Mensagem</label>
                    <textarea id="message" name="message" rows="5" placeholder="Escreva sua mensagem aqui..." required></textarea>
                </div>
                
                <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 10px;">
                    <i class="fa-solid fa-paper-plane"></i> Enviar Mensagem
                </button>
            </form>
        </div>
    </div>
</section>
