from handlers_clients import (
    handle_create_client,
    handle_list_clients,
    handle_search_clients,
)
from handlers_trips import handle_create_trip, handle_list_trips, handle_update_trip


def mostrar_menu() -> None:
    print("\n=== GERENCIADOR DE CLIENTES ===")
    print("1. Cadastrar cliente")
    print("2. Listar cliente")
    print("3. Buscar cliente")
    print("4. Criar viagem")
    print("5. Listar viagem")
    print("6. Atualizar status da viagem")
    print("0. Sair")


if __name__ == "__main__":

    while True:

        mostrar_menu()
        option = input("Escolha uma opção: ").strip()

        if option == "0":
            print("Saindo...")
            break

        elif option == "1":
            handle_create_client()

        elif option == "2":
            handle_list_clients()

        elif option == "3":
            handle_search_clients()

        elif option == "4":
            handle_create_trip()

        elif option == "5":
            handle_list_trips()

        elif option == "6":
            handle_update_trip()

        else:
            print("Opção inválida. Tente novamente.")
