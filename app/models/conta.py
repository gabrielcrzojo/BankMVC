import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'bmvc.db')

class ContaModel:
    @staticmethod
    def get_connection():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def get_all(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Conta")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def get_by_id(cls, conta_id):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Conta WHERE id = ?", (conta_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None
    
    @classmethod
    def get_by_numero(cls, numero_conta):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Conta WHERE numero_conta = ?", (numero_conta,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @classmethod
    def get_by_usuario(cls, usuario_id):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Conta WHERE usuario_id = ?", (usuario_id,))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def create(cls, numero_conta, usuario_id, nome='', sobrenome='', saldo_inicial=0.0):
        conn = cls.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Conta (numero_conta, usuario_id, nome, sobrenome, saldo) VALUES (?, ?, ?, ?, ?)",
                (numero_conta, usuario_id, nome, sobrenome, saldo_inicial)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()

    @classmethod
    def update(cls, conta_id, saldo):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Conta SET saldo = ? WHERE id = ?",
            (saldo, conta_id)
        )
        conn.commit()
        conn.close()
        return True

    @classmethod
    def update_info(cls, conta_id, numero_conta, nome, sobrenome):
        conn = cls.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Conta SET numero_conta = ?, nome = ?, sobrenome = ? WHERE id = ?",
                (numero_conta, nome, sobrenome, conta_id)
            )
            conn.commit()
            return True, None
        except sqlite3.IntegrityError:
            return False, "Número de conta já existe."
        finally:
            conn.close()

    @classmethod
    def delete(cls, conta_id):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Conta WHERE id = ?", (conta_id,))
        conn.commit()
        conn.close()
        return True
