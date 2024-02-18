# database.py
import psycopg2
from psycopg2 import sql
import bcrypt
from decouple import config
from bypasssafe.account import Account


class Database:
    """
    Classe para interação com o banco de dados.

    Esta classe contém métodos para salvar contas, buscar contas associadas a um mestre,
    autenticar usuários e obter informações de uma conta por nome de usuário.
    """

    DATABASE_URL = config("DATABASE_URL")
    
    @staticmethod
    def save_account(account):
        """
        Salva uma conta no banco de dados.

        Args:
            account (Account): A conta a ser salva no banco de dados.
        """
        try:
            connection = psycopg2.connect(Database.DATABASE_URL)
            cursor = connection.cursor()

            create_account_query = sql.SQL(
                "INSERT INTO accounts (master_id, username, password, email) VALUES ({}, {}, {}, {})"
            ).format(
                sql.Literal(account.master_id),
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
        """
        Autentica um usuário comparando email e senha com o banco de dados.

        Args:
            email (str): O email do usuário.
            password (str): A senha do usuário.

        Returns:
            int or None: O ID do mestre se a autenticação for bem-sucedida, None caso contrário.
        """
        connection = psycopg2.connect(Database.DATABASE_URL)
        cursor = connection.cursor()

        select_master_query = "SELECT * FROM masters WHERE email = %s"
        cursor.execute(select_master_query, (email,))
        master = cursor.fetchone()

        cursor.close()
        connection.close()

        if master is not None and bcrypt.checkpw(
            password.encode("utf-8"), master[2].encode("utf-8")
        ):
            return master[0]
        else:
            return None

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
                account_data[0], account_data[2], account_data[3], account_data[4]
            )
            return account
        else:
            return None
