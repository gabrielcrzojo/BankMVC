# Documentação de Alterações e Instruções de Código - Nível II

Este documento detalha a evolução do projeto **BankMVC** para o **Nível II (CRUD de Contas e Transações)**, introduzindo persistência em banco de dados e regras de negócio essenciais de um sistema financeiro.

---

## 🛠️ Alterações Realizadas

### 1. Persistência e Banco de Dados (SQLite)
- **Criação do Banco:** O arquivo `database/bmvc.db` foi gerado via script Python.
- **Tabelas Criadas:** 
  - `Usuario`: Tabela mock para simular o cliente (FK exigida por `Conta`).
  - `Conta`: Armazena número da conta, saldo e o id do usuário proprietário.
  - `Transacao`: Registra depósitos, saques e transferências, vinculando as contas envolvidas (origem e destino).

### 2. Acesso a Dados (Models)
Os modelos foram criados para interagir diretamente com o banco de dados utilizando Queries Parametrizadas (para evitar SQL Injection):
- **`ContaModel` (`app/models/conta.py`):** Suporta criação de conta, listagem de todas as contas cadastradas, leitura por ID/número e exclusão.
- **`TransacaoModel` (`app/models/transacao.py`):** Engloba lógicas transacionais (`BEGIN ... COMMIT`). Caso o saldo seja insuficiente ou a conta seja inválida, é realizado o `ROLLBACK`. Contempla métodos `depositar`, `sacar` e `transferir`.

### 3. Lógica de Controle (Controllers)
- **`ContaController`:** Processa o envio de formulários para abrir uma nova conta e renderiza a lista completa de contas ativas.
- **`TransacaoController`:** Responsável por exibir o histórico completo (com nomes resolvidos de contas a partir dos IDs) e processar as diferentes naturezas de movimentação. Verifica os erros emitidos pelo Model e os devolve para a tela do usuário.

### 4. Apresentação (Views)
Foram adicionadas novas páginas à plataforma:
- **`contas_list.tpl` e `contas_form.tpl`:** Interface para gestão de contas (visualização, criação, exclusão).
- **`transacoes_list.tpl` e `transacoes_form.tpl`:** Tela para listar o extrato e formulário inteligente que oculta campos dependendo do tipo de transação (ex: depósito não exibe a "conta origem").
- As views utilizam componentes estéticos criados no Nível I, expandidos agora com o `.crud-table` e alertas (`.badge` e `.alert`) definidos no `style.css`.

---

## 💻 Instruções de Uso

1. **Inicialização do Banco (Apenas Primeira Vez):**
   Execute o script inicializador para garantir que o banco de dados e as tabelas estejam criados:
   ```bash
   python database/db_init.py
   ```
   *(Isso criará o arquivo `bmvc.db` e um usuário mock para associação das contas).*

2. **Iniciar o Servidor:**
   ```bash
   python route.py
   ```
   
3. **Fluxo de Navegação:**
   - Acesse **[http://localhost:8080/](http://localhost:8080/)**.
   - Na barra de navegação superior, vá até **Contas** e crie uma ou duas contas (ex: "Corrente", "Poupança").
   - Acesse **Transações** > **Nova Transação**.
   - Escolha o tipo "Depósito" para inserir um saldo inicial na conta.
   - Faça uma "Transferência" entre as duas contas criadas.
   - Verifique que saques superiores ao saldo na conta não são permitidos pelo sistema.

A arquitetura atual prova o isolamento das camadas: as validações severas de valor monetário e saldo ocorrem restritamente no `TransacaoModel`, o `TransacaoController` faz a ponte sem misturar SQL, e a `View` se encarrega exclusivamente da disposição visual dos alertas.
