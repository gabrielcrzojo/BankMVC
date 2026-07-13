import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'bmvc.db')

class UsuarioModel:
    @staticmethod
    def get_connection():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def get_by_id(cls, usuario_id):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuario WHERE id = ?", (usuario_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @classmethod
    def get_by_email(cls, email):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Usuario WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @classmethod
    def authenticate(cls, email, senha):
        usuario = cls.get_by_email(email)
        # Comparação em texto puro conforme requisitado
        if usuario and usuario['senha_hash'] == senha:
            return usuario
        return None

    @classmethod
    def create(cls, nome, email, senha, tipo='cliente'):
        conn = cls.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Usuario (nome, email, senha_hash, tipo) VALUES (?, ?, ?, ?)",
                (nome, email, senha, tipo)
            )
            conn.commit()
            return True, None
        except sqlite3.IntegrityError:
            return False, "E-mail já cadastrado."
        finally:
            conn.close()
