# Documentação de Alterações e Instruções de Código - Nível I

Este documento detalha o desenvolvimento do **Nível I (Landing Page Institucional)** para o projeto **BMVC Bank**, explicando a arquitetura implementada, decisões de design, correções técnicas e fornecendo instruções sobre a estrutura de código.

---

## 🛠️ Alterações Realizadas

### 1. Roteamento e Controle (Python)
- **Rotas Mapeadas:** Modificamos o arquivo [route.py](file:///home/gabriel/Python/bmvc/route.py) para expor as seguintes rotas:
  - `/` (Home): Renderiza a página principal do banco.
  - `/sobre` (Sobre Nós): Apresenta o histórico, objetivos e valores do banco.
  - `/servicos` (Serviços): Mostra as funcionalidades e diferenciais da conta digital.
  - `/contato` (Contato): Permite o envio de mensagens com um formulário estilizado.
- **Estruturação do Controlador:** Atualizamos a classe [Application](file:///home/gabriel/Python/bmvc/app/controllers/application.py#L4) em [application.py](file:///home/gabriel/Python/bmvc/app/controllers/application.py) para gerenciar o dicionário de páginas dinamicamente e expor métodos para cada uma das views institucionais.
- **Remoção de Arquivos de Instrução:** Removemos todos os arquivos de exemplo e tutorial originais (`helper.tpl`, `helper.css` e `helper.js`) e as respectivas menções nas rotas para obter um projeto limpo e otimizado.

### 2. Apresentação (Views / TPL)
Criamos um sistema de templates baseado em herança usando o motor *SimpleTemplate* do Bottle:
- **[base.tpl](file:///home/gabriel/Python/bmvc/app/views/html/base.tpl):** Layout base contendo os metadados, links externos (Google Fonts, FontAwesome), cabeçalho com navegação fluida, footer responsivo e carregamento assíncrono de arquivos estáticos.
- **[home.tpl](file:///home/gabriel/Python/bmvc/app/views/html/home.tpl):** Contém a seção de Hero com o slogan, chamada para ação, destaques dinâmicos de recursos e uma representação visual premium de um cartão de crédito (`BMVC Black`).
- **[sobre.tpl](file:///home/gabriel/Python/bmvc/app/views/html/sobre.tpl):** Apresenta indicadores estatísticos do banco e os três valores institucionais pilares.
- **[servicos.tpl](file:///home/gabriel/Python/bmvc/app/views/html/servicos.tpl):** Grid responsivo detalhando os 6 principais serviços digitais.
- **[contato.tpl](file:///home/gabriel/Python/bmvc/app/views/html/contato.tpl):** Layout com informações físicas de contato e um formulário de envio integrado com validações básicas.

### 3. Estilização & Design System (CSS)
Criamos o arquivo [style.css](file:///home/gabriel/Python/bmvc/app/static/css/style.css), contendo:
- **Design System com Variáveis CSS:** Configuração centralizada de fontes (`Outfit`), raios de borda, tempos de transição e sombras.
- **Modos Escuro & Claro nativos:** Suporte total à alteração dinâmica de paleta de cores através da classe `.dark-mode` injetada na tag `body`.
- **Glassmorphism:** Estilos para os cartões e navbar utilizando propriedades modernas como `backdrop-filter` e transparência com canais alfa.
- **Componentes Responsivos:** Media queries implementadas para garantir legibilidade e usabilidade em dispositivos móveis e desktops.

### 4. Interatividade Dinâmica (JavaScript)
Criamos o arquivo [main.js](file:///home/gabriel/Python/bmvc/app/static/js/main.js), responsável por:
- **Alternador de Tema (Dark Mode):** Alterna o ícone de lua/sol, injeta a classe no `body` e persiste a escolha do usuário no `localStorage` do navegador para visitas futuras.
- **Menu Mobile Responsivo:** Efeito de *toggle* do menu hambúrguer com transição suave.
- **Botão Voltar ao Topo:** Exibido de forma flutuante após rolar mais de 300px da página, executando scroll suave ao topo ao ser clicado.
- **Efeitos de Navegação e Scroll:** Controle de transparência na navbar ao rolar a página.

---

## 💻 Instruções de Código e Funcionamento

### Herança de Templates no Bottle
Para evitar código duplicado em cada página, o Bottle permite definir um layout base central e redefinir o conteúdo em sub-templates.

No [base.tpl](file:///home/gabriel/Python/bmvc/app/views/html/base.tpl), declaramos a tag de injeção `{{!base}}`:
```html
<main>
    {{!base}}
</main>
```
E em cada página (como [home.tpl](file:///home/gabriel/Python/bmvc/app/views/html/home.tpl)), fazemos o *rebase* passando variáveis úteis (como o título e a aba ativa da navbar):
```tpl
% rebase('app/views/html/base.tpl', title='Home', active_page='home')
<section class="hero-section">
   <!-- Conteúdo específico da Home -->
</section>
```

### Persistência de Preferência de Tema no Lado do Cliente
O código JavaScript lê a preferência anterior e aplica imediatamente ao carregar o DOM para evitar o efeito "flash" de luz em telas escuras:
```javascript
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
  document.body.classList.add('dark-mode');
}
```

---

## 🐳 Ajustes e Solução de Problemas no Docker (SELinux)

Durante os testes locais sob o Docker na máquina do usuário, identificamos que a montagem de volume `-v $(pwd):/bmeta` causava uma exceção de permissão negada (`[Errno 13] Permission denied`) devido à proteção de segurança do **SELinux** ativada no host Linux.

### Resolução:
Adicionamos o modificador de contexto compartilhado `:z` ao volume no comando de inicialização. Isso instrui o Docker a relotear o contexto de segurança dos arquivos no host automaticamente para que possam ser lidos/gravados pelo container:
```bash
docker run --name bmetaap -d -p 8080:8080 -v $(pwd):/bmeta:z bmetimg
```
Isso sanou completamente o problema de acesso, permitindo a execução do servidor Flask/Bottle com sucesso.
