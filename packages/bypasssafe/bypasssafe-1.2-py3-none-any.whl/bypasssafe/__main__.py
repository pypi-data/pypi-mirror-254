from bypasssafe.main import create_master_account, login, create_account, generate_password, search_account, clear_console
import time

def main():
    """
    Função principal do programa.

    Controla o fluxo principal do programa, incluindo a exibição de menus, chamadas de funções e interações com o usuário.
    """

    master_id = None

    while master_id is None:
        clear_console()
        print("1 - Fazer Login")
        print("2 - Criar Conta Master")
        ja = int(input("Escolha uma opção: "))
        if ja == 1:
            master_id = login()
        elif ja == 2:
            create_master_account()
        else:
            print("Opção inválida. Por favor, digite um número entre 1 e 2.")

    while True:
        clear_console()
        print("Welcome!")
        print("\nMenu:")
        print("1. Cadastrar Conta")
        print("2. Gerar Senha")
        print("3. Procurar Conta")
        print("4. Sair")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            create_account(master_id)
            time.sleep(2)  # Aguarda 2 segundos antes de limpar o console e mostrar o próximo menu
        elif choice == "2":
            generate_password()
            time.sleep(2)
        elif choice == "3":
            username_to_search = input("Digite o nome da conta que deseja buscar: ")
            search_account(master_id, username_to_search)
            time.sleep(2)
        elif choice == "4":
            print("Fechando. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, digite um número entre 1 e 4.")
            time.sleep(2)


if __name__ == "__main__":
    main()