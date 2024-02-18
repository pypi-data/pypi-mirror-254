# pass_gen.py
import random
import string

class PasswordGenerator:
    """
    Classe para gerar senhas aleatórias com base em requisitos específicos.

    A classe fornece um método estático para gerar senhas que podem incluir letras,
    números e símbolos, com a opção de incluir ou não letras maiúsculas.
    """

    @staticmethod
    def generate_password(length, num_digits, num_symbols, uppercase):
        """
        Gera uma senha aleatória com base nos parâmetros fornecidos.

        Args:
            length (int): O comprimento total da senha.
            num_digits (int): O número de dígitos na senha.
            num_symbols (int): O número de símbolos na senha.
            uppercase (bool): Indica se a senha deve incluir letras maiúsculas.

        Returns:
            str: A senha gerada.
        """
        all_chars = string.ascii_letters + string.digits + string.punctuation
        if not uppercase:
            all_chars = string.ascii_lowercase + string.digits + string.punctuation

        digits = "".join(random.choice(string.digits) for _ in range(num_digits))
        symbols = "".join(random.choice(string.punctuation) for _ in range(num_symbols))
        letters = "".join(
            random.choice(all_chars) for _ in range(length - num_digits - num_symbols)
        )

        password = "".join(random.sample(digits + symbols + letters, length))
        return password
