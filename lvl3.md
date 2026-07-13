# Documentação de Alterações e Instruções de Código - Nível III

Este documento detalha a evolução do projeto **BankMVC** para o **Nível III (Autenticação e Dashboard)**, introduzindo gestão de sessões, restrição de acesso e painéis personalizados.

---

## 🛠️ Alterações Realizadas

### 1. Sistema de Autenticação (Models, Controllers e Utils)
- **`UsuarioModel` (`app/models/usuario.py`):** Criado para interagir com a tabela `Usuario`, permitindo o cadastro (`create`), busca por e-mail e ID, e a verificação de credenciais (`authenticate`). As senhas estão sendo validadas em texto puro.
- **`AuthController` (`app/controllers/auth_controller.py`):** Lida com as requisições GET e POST das telas de Cadastro e Login. Gerencia a criação e exclusão do cookie de sessão (`session_id`) usando os recursos integrados do Bottle.
- **Middleware/Decorator (`app/utils/auth.py`):** Implementação da função `get_current_user()` e do decorator `@requires_auth`, usado para proteger rotas.

### 2. Dashboard e Restrição de Dados
- **`DashboardController` (`app/controllers/dashboard_controller.py`):** Novo controlador responsável por processar e renderizar a rota `/dashboard`. Ele coleta o saldo total do usuário logado e as últimas transações realizadas.
- **Filtros por Usuário:**
  - `ContaModel.get_by_usuario(usuario_id)`: Busca apenas contas daquele usuário.
  - `TransacaoModel.get_by_usuario(usuario_id)`: Traz apenas o extrato envolvendo contas deste mesmo usuário.
  - O `ContaController` e `TransacaoController` foram refatorados para utilizar esses filtros ao invés de exibir todos os registros do banco indiscriminadamente.

### 3. Rotas Protegidas (`route.py`)
- Foram introduzidas as rotas `/login`, `/cadastro` e `/logout`.
- As rotas `/dashboard`, `/contas`, `/transacoes` e todas as suas variações de CRUD (`/nova`, `/editar`, `/deletar`) receberam o decorator `@requires_auth`. Usuários anônimos são redirecionados automaticamente para o login.

### 4. Apresentação (Views)
- **Novas Views:** Adicionadas `login.tpl`, `cadastro.tpl` e `dashboard.tpl` usando os componentes estéticos já criados (como `glass-card`).
- **Navegação Dinâmica (`base.tpl`):** O botão de "Login" do menu principal agora é inteligente. Se o cookie de autenticação for detectado, ele é substituído pelos botões "Dashboard" e "Sair". O método estático no `Application` foi ajustado para passar os dados do usuário conectado às páginas públicas (`home`, `sobre`, etc.).

---

## 💻 Instruções de Uso

1. **Iniciar o Servidor:**
   ```bash
   python route.py
   ```
   
2. **Fluxo de Navegação (Testando o Nível III):**
   - Acesse **[http://localhost:8080/](http://localhost:8080/)**. Note que o botão "Login" está visível no topo.
   - Tente acessar `/contas` diretamente pela URL. O sistema deverá barrar o acesso e redirecionar para a tela de Login.
   - Clique em **"Crie uma aqui"** (na tela de login) ou no botão "Abra sua Conta Grátis" na Home para criar seu perfil.
   - Após o cadastro, você será levado para o seu novo **Dashboard**.
   - Crie contas e faça transações. Observe que tudo agora está confinado à sua sessão (se você sair e criar uma nova conta de usuário, não verá os mesmos dados bancários).
   - Use o botão **Sair** no menu superior para testar a remoção do cookie de sessão.
