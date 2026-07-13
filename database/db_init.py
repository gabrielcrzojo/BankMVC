import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'bmvc.db')

def init_db():
    print(f"Inicializando banco de dados em {DB_PATH}...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabela Usuario
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha_hash TEXT NOT NULL,
        tipo TEXT NOT NULL
    )
    ''')

    # Tabela Conta
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Conta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_conta TEXT UNIQUE NOT NULL,
        usuario_id INTEGER NOT NULL,
        nome TEXT NOT NULL DEFAULT '',
        sobrenome TEXT NOT NULL DEFAULT '',
        saldo REAL NOT NULL DEFAULT 0.0,
        FOREIGN KEY (usuario_id) REFERENCES Usuario (id)
    )
    ''')

    # Tabela Transacao
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transacao (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conta_origem INTEGER,
        conta_destino INTEGER,
        tipo TEXT NOT NULL,
        valor REAL NOT NULL,
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        descricao TEXT,
        FOREIGN KEY (conta_origem) REFERENCES Conta (id),
        FOREIGN KEY (conta_destino) REFERENCES Conta (id)
    )
    ''')

    # Criar usuários iniciais
    cursor.execute('SELECT id FROM Usuario WHERE email = ?', ('admin@bankmvc.com',))
    if not cursor.fetchone():
        cursor.execute('''
        INSERT INTO Usuario (nome, email, senha_hash, tipo)
        VALUES (?, ?, ?, ?)
        ''', ('Administrador', 'admin@bankmvc.com', 'admin', 'admin'))
        print("Usuário administrador criado com sucesso!")

    cursor.execute('SELECT id FROM Usuario WHERE email = ?', ('gabriel@bankmvc.com',))
    if not cursor.fetchone():
        cursor.execute('''
        INSERT INTO Usuario (nome, email, senha_hash, tipo)
        VALUES (?, ?, ?, ?)
        ''', ('Gabriel Padrão', 'gabriel@bankmvc.com', '123456', 'cliente'))
        print("Usuário padrão criado com sucesso!")

    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")

if __name__ == '__main__':
    init_db()
