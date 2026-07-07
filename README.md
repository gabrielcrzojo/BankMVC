# BankMVC - Nível I: Landing Page Institucional

O **BankMVC** é um projeto de simulação de banco digital desenvolvido de forma incremental utilizando a arquitetura **MVC (Model-View-Controller)** com o framework **Bottle** para Python. 

Este repositório contém a implementação do **Nível I (Landing Page Institucional)**, que consiste em servir páginas estáticas institucionais responsivas e dinâmicas a partir de um servidor Bottle, com foco em uma experiência do usuário premium, com animações e suporte a modo escuro persistente.

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.12, Bottle Framework
- **Frontend**: HTML5 (SimpleTemplate Engine), CSS3 (Custom styling com variáveis CSS), JavaScript moderno (Vanilla ES6)
- **Containerização**: Docker (imagem base `python:3.12-slim`)

---

## 📁 Estrutura do Projeto (Nível I)

```text
bmvc/
├── app/
│   ├── controllers/
│   │   ├── application.py   # Controlador principal (repassa renderizações)
│   ├── views/
│   │   └── html/
│   │       ├── base.tpl     # Layout base comum (navbar, footer, css/js links)
│   │       ├── home.tpl     # Página inicial (Hero, Destaques, Card Mockup)
│   │       ├── sobre.tpl    # Página "Sobre Nós" (Valores, Estatísticas)
│   │       ├── servicos.tpl # Página de Serviços (Lista de recursos da conta)
│   │       └── contato.tpl  # Página de Contato (Informações e Formulário)
│   └── static/
│       ├── css/
│       │   └── style.css    # Design System centralizado (Variáveis, Dark Mode, Responsividade)
│       ├── js/
│       │   └── main.js      # Scripts de interatividade (Tema escuro, Hamburguer, Scroll)
│       └── img/
│           └── BottleLogo.png
├── Dockerfile               # Configuração da imagem Docker
├── route.py                 # Ponto de entrada (Router)
├── README.md                # Instruções Gerais de Uso
└── lvl1.md                  # Relatório de Alterações do Nível I
```

---

## 🚀 Como Executar o Projeto

Você pode executar a aplicação localmente utilizando o terminal (BASH) ou rodá-la isoladamente através do Docker.

### Opção 1: Executando com Docker (Recomendado)

O projeto está totalmente configurado para rodar sob Docker, mapeando o volume do host para permitir alterações de design em tempo real.

1. **Construir a Imagem Docker:**
   ```bash
   docker build -t bmetimg .
   ```

2. **Iniciar o Container:**
   - **Linux (SELinux ativo - ex: Fedora/RedHat):**
     *Mapeia o diretório e aplica a tag `:z` de contexto SELinux para evitar erros de permissão:*
     ```bash
     docker run --name bmetaap -d -p 8080:8080 -v $(pwd):/bmeta:z bmetimg
     ```
   - **Linux padrão / macOS / Windows:**
     ```bash
     docker run --name bmetaap -d -p 8080:8080 -v $(pwd):/bmeta bmetimg
     ```

3. **Acessar a Aplicação:**
   Abra seu navegador e acesse: [http://localhost:8080](http://localhost:8080)

4. **Gerenciar o Container:**
   - **Ver logs de inicialização:** `docker logs bmetaap`
   - **Parar o container:** `docker stop bmetaap`
   - **Iniciar novamente:** `docker start bmetaap`
   - **Remover o container:** `docker rm bmetaap`

---

### Opção 2: Executando Localmente no Terminal (BASH)

Caso prefira rodar diretamente na máquina sem Docker, certifique-se de ter o Python 3 instalado.

1. **Instalar Dependências:**
   Instale o Bottle e demais pacotes necessários:
   ```bash
   pip install bottle eventlet python-socketio reportlab jinja2 pytz filelock
   ```

2. **Iniciar a Aplicação:**
   Execute o roteador na raiz do projeto:
   ```bash
   python route.py
   ```

3. **Acessar a Aplicação:**
   Navegue para [http://localhost:8080](http://localhost:8080) no seu navegador.
