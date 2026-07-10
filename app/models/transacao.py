import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'bmvc.db')

class TransacaoModel:
    @staticmethod
    def get_connection():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def get_all(cls):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Transacao ORDER BY data_hora DESC")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    
    @classmethod
    def get_by_conta(cls, conta_id):
        conn = cls.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Transacao WHERE conta_origem = ? OR conta_destino = ? ORDER BY data_hora DESC", (conta_id, conta_id))
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @classmethod
    def depositar(cls, conta_destino_id, valor, descricao="Depósito"):
        if valor <= 0:
            return False, "Valor inválido"
            
        conn = cls.get_connection()
        try:
            cursor = conn.cursor()
            # Inicia transação
            cursor.execute("BEGIN")
            
            # Atualiza saldo
            cursor.execute("UPDATE Conta SET saldo = saldo + ? WHERE id = ?", (valor, conta_destino_id))
            if cursor.rowcount == 0:
                conn.rollback()
                return False, "Conta não encontrada"
                
            # Registra transação
            cursor.execute(
                "INSERT INTO Transacao (conta_destino, tipo, valor, descricao) VALUES (?, 'deposito', ?, ?)",
                (conta_destino_id, valor, descricao)
            )
            
            conn.commit()
            return True, "Depósito realizado com sucesso"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            conn.close()

    @classmethod
    def sacar(cls, conta_origem_id, valor, descricao="Saque"):
        if valor <= 0:
            return False, "Valor inválido"
            
        conn = cls.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("BEGIN")
            
            # Checar saldo
            cursor.execute("SELECT saldo FROM Conta WHERE id = ?", (conta_origem_id,))
            row = cursor.fetchone()
            if not row:
                conn.rollback()
                return False, "Conta não encontrada"
                
            saldo_atual = row['saldo']
            if saldo_atual < valor:
                conn.rollback()
                return False, "Saldo insuficiente"
            
            # Atualiza saldo
            cursor.execute("UPDATE Conta SET saldo = saldo - ? WHERE id = ?", (valor, conta_origem_id))
                
            # Registra transação
            cursor.execute(
                "INSERT INTO Transacao (conta_origem, tipo, valor, descricao) VALUES (?, 'saque', ?, ?)",
                (conta_origem_id, valor, descricao)
            )
            
            conn.commit()
            return True, "Saque realizado com sucesso"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            conn.close()
            
    @classmethod
    def transferir(cls, conta_origem_id, conta_destino_id, valor, descricao="Transferência"):
        if valor <= 0:
            return False, "Valor inválido"
        if conta_origem_id == conta_destino_id:
            return False, "Conta de destino igual à conta de origem"
            
        conn = cls.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("BEGIN")
            
            # Checar saldo origem
            cursor.execute("SELECT saldo FROM Conta WHERE id = ?", (conta_origem_id,))
            row = cursor.fetchone()
            if not row:
                conn.rollback()
                return False, "Conta de origem não encontrada"
                
            saldo_atual = row['saldo']
            if saldo_atual < valor:
                conn.rollback()
                return False, "Saldo insuficiente"
                
            # Checar conta destino
            cursor.execute("SELECT id FROM Conta WHERE id = ?", (conta_destino_id,))
            if not cursor.fetchone():
                conn.rollback()
                return False, "Conta de destino não encontrada"
            
            # Atualiza saldos
            cursor.execute("UPDATE Conta SET saldo = saldo - ? WHERE id = ?", (valor, conta_origem_id))
            cursor.execute("UPDATE Conta SET saldo = saldo + ? WHERE id = ?", (valor, conta_destino_id))
                
            # Registra transação
            cursor.execute(
                "INSERT INTO Transacao (conta_origem, conta_destino, tipo, valor, descricao) VALUES (?, ?, 'transferencia', ?, ?)",
                (conta_origem_id, conta_destino_id, valor, descricao)
            )
            
            conn.commit()
            return True, "Transferência realizada com sucesso"
        except Exception as e:
            conn.rollback()
            return False, str(e)
        finally:
            conn.close()
