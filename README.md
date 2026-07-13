# BankMVC - Banco Digital

O **BankMVC** é um projeto de simulação de banco digital desenvolvido de forma incremental utilizando a arquitetura **MVC (Model-View-Controller)** com o framework **Bottle** para Python. 

Atualmente, o projeto abrange até o **Nível III (Autenticação e Dashboard)**, suportando páginas estáticas institucionais responsivas, persistência em banco de dados SQLite, operações transacionais seguras e gestão de sessão de usuários (login/logout e áreas restritas).

---

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.12, Bottle Framework, SQLite (Persistência)
- **Frontend**: HTML5 (SimpleTemplate Engine), CSS3 (Custom styling com variáveis CSS), JavaScript moderno (Vanilla ES6)
- **Containerização**: Docker (imagem base `python:3.12-slim`)

---

## 📁 Estrutura do Projeto (Nível III)

```text
bmvc/
├── app/
│   ├── controllers/
│   │   ├── application.py         # Controlador base
│   │   ├── auth_controller.py     # Lógica de Login/Cadastro
│   │   ├── conta_controller.py    # Lógica de Contas
│   │   ├── dashboard_controller.py# Lógica do Painel do Usuário
│   │   └── transacao_controller.py# Lógica de Transações
│   ├── models/
│   │   ├── conta.py               # Persistência e regras de Contas
│   │   ├── transacao.py           # Persistência e regras de Transações
│   │   └── usuario.py             # Persistência e regras de Autenticação
│   ├── utils/
│   │   └── auth.py                # Decorators para proteção de rotas
│   ├── views/
│   │   └── html/
│   │       ├── base.tpl
│   │       ├── home.tpl, sobre.tpl, servicos.tpl, contato.tpl
│   │       ├── login.tpl, cadastro.tpl, dashboard.tpl
│   │       ├── contas_list.tpl, contas_form.tpl
│   │       └── transacoes_list.tpl, transacoes_form.tpl
│   └── static/
│       ├── css/style.css
│       ├── js/main.js, crud.js
│       └── img/BottleLogo.png
├── database/
│   ├── db_init.py           # Script para inicializar DB SQLite
│   └── bmvc.db              # Banco de dados (gerado pós-inicialização)
├── Dockerfile               # Configuração da imagem Docker
├── route.py                 # Ponto de entrada (Router e Configuração de Middlewares)
├── README.md                # Instruções Gerais de Uso
├── lvl1.md                  # Relatório de Alterações do Nível I
├── lvl2.md                  # Relatório de Alterações do Nível II
└── lvl3.md                  # Relatório de Alterações do Nível III
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

2. **Inicializar Banco de Dados (Apenas 1ª Vez):**
   ```bash
   python database/db_init.py
   ```

3. **Iniciar a Aplicação:**
   Execute o roteador na raiz do projeto:
   ```bash
   python route.py
   ```

4. **Acessar a Aplicação:**
   Navegue para [http://localhost:8080](http://localhost:8080) no seu navegador.
