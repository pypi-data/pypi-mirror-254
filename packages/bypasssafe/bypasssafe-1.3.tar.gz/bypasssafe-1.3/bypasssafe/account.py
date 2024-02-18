# account.py

class MasterAccount:
    """
    Representa uma conta mestre no sistema.

    Atributos:
        username (str): O nome de usuário associado à conta mestre.
        password (str): A senha mestra, armazenada como um hash.
        email (str): O endereço de email associado à conta mestre.
    """

    def __init__(self, username, hashed_password, email):
        """
        Inicializa uma nova instância de MasterAccount.

        Args:
            username (str): O nome de usuário associado à conta mestre.
            hashed_password (str): A senha mestra, armazenada como um hash.
            email (str): O endereço de email associado à conta mestre.
        """
        self.username = username
        self.password = hashed_password  
        self.email = email


class Account:
    """
    Representa uma conta associada a uma conta mestre no sistema.

    Atributos:
        master_id (int): O ID da conta mestre à qual esta conta está associada.
        username (str): O nome de usuário associado à conta.
        password (str): A senha associada à conta.
        email (str): O endereço de email associado à conta.
    """

    def __init__(self, master_id, username, password, email):
        """
        Inicializa uma nova instância de Account.

        Args:
            master_id (int): O ID da conta mestre à qual esta conta está associada.
            username (str): O nome de usuário associado à conta.
            password (str): A senha associada à conta.
            email (str): O endereço de email associado à conta.
        """
        self.master_id = master_id
        self.username = username
        self.password = password
        self.email = email
