# database.py
import psycopg2
from psycopg2 import sql
from decouple import config
from bypasssafe.account import Account
import bcrypt


class Database:
    """
    Classe para interação com o banco de dados.

    Esta classe contém métodos para salvar contas, buscar contas associadas a um mestre,
    autenticar usuários e obter informações de uma conta por nome de usuário.
    """

    DATABASE_URL = config("DATABASE_URL")
    
    @staticmethod
    def save_account(account):
        try:
            connection = psycopg2.connect(Database.DATABASE_URL)
            cursor = connection.cursor()
            
            master_id = int(account.master_id[0])  # Extract the first element from the tuple

            # Usando parâmetros preparados para evitar injeção SQL
            create_account_query = sql.SQL(
                "INSERT INTO accounts (master_id, username, password, email) VALUES ({}, {}, {}, {})"
            ).format(
                sql.Literal(master_id),
                sql.Literal(account.username),
                sql.Literal(account.password),
                sql.Literal(account.email),
            )
            
            cursor.execute(create_account_query)
            connection.commit()

            print("Conta salva com sucesso.")

        except Exception as e:
            print(f"Erro ao salvar conta: {e}")

        finally:
            cursor.close()
            connection.close()
            
    @staticmethod
    def save_master_account(master_account):
        try:
            connection = psycopg2.connect(Database.DATABASE_URL)
            cursor = connection.cursor()

            create_master_account_query = sql.SQL(
                "INSERT INTO masters (username, email, password) VALUES ({}, {}, {})"
            ).format(
                sql.Literal(master_account.username),
                sql.Literal(master_account.email),
                sql.Literal(master_account.password),
            )

            cursor.execute(create_master_account_query)
            connection.commit()

            print("Conta mestre salva com sucesso.")

        except Exception as e:
            print(f"Erro ao salvar conta mestre: {e}")

        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_accounts_by_master_id(master_id):
        """
        Obtém todas as contas associadas a um mestre.

        Args:
            master_id (int): O ID do mestre para o qual as contas estão associadas.

        Returns:
            list: Uma lista de tuples representando as contas associadas ao mestre.
        """
        connection = psycopg2.connect(Database.DATABASE_URL)
        cursor = connection.cursor()

        select_accounts_query = "SELECT * FROM accounts WHERE master_id = %s"
        cursor.execute(select_accounts_query, (master_id,))
        accounts = cursor.fetchall()

        cursor.close()
        connection.close()

        return accounts

    @staticmethod
    def authenticate_user(email, password):
        try:
            connection = psycopg2.connect(Database.DATABASE_URL)
            cursor = connection.cursor()

            # Consulta parametrizada para obter o id do mestre e a senha codificada
            select_master_query = sql.SQL("SELECT id, password FROM masters WHERE email = {}").format(
                sql.Literal(email)
            )

            cursor.execute(select_master_query)
            result = cursor.fetchone()

            if result and bcrypt.checkpw(password.encode(), result[1].encode()):
                # Se a senha estiver correta, retorna o id do mestre
                return result[0]
            else:
                # Senha incorreta ou usuário não encontrado
                return None

        except Exception as e:
            print(f"Um erro ocorreu durante a autenticação do usuário: {e}")
            return None

        finally:
            cursor.close()
            connection.close()
        
    @staticmethod
    def get_account_by_username(master_id, username):
        """
        Obtém informações de uma conta por nome de usuário.

        Args:
            master_id (int): O ID do mestre ao qual a conta está associada.
            username (str): O nome de usuário da conta.

        Returns:
            Account or None: A conta correspondente se encontrada, None caso contrário.
        """
        connection = psycopg2.connect(Database.DATABASE_URL)
        cursor = connection.cursor()

        select_account_query = (
            "SELECT * FROM accounts WHERE master_id = %s AND username = %s"
        )
        cursor.execute(select_account_query, (master_id, username))
        account_data = cursor.fetchone()

        cursor.close()
        connection.close()

        if account_data:
            account = Account(
                account_data[1], account_data[2], account_data[3], account_data[4]
            )
            return account
        else:
            return None
