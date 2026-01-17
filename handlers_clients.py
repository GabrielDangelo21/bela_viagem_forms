from db import (
    insert_client,
    list_clients,
    search_clients_document,
    search_clients_email,
    search_clients_name,
)


def mostrar_menu_busca() -> None:
    print("\n=== BUSCADOR DE CLIENTES ===")
    print("1. Buscar por nome")
    print("2. Buscar por email")
    print("3. Buscar por documento")
    print("0. Sair")


def print_clients(results):
    if not results:
        print("Nenhum cliente encontrado.")
    else:
        print("\n--- Clientes encontrados ---")
        for client in results:
            client_id, name, email, phone, document = client
            print(
                f"ID: {client_id} | Nome: {name} | Email: {email} | Telefone: {phone} | Documento: {document}"
            )


def handle_create_client():
    nome = input("Nome: ").strip()

    if not nome:
        print("Nome é obrigatório.")
        return

    email = input("Email: ").strip() or None
    telefone = input("Telefone: ").strip() or None
    documento = input("Documento: ").strip() or None

    try:
        new_id = insert_client(nome, email, telefone, documento)
        print("Cliente cadastrado com ID: ", new_id)
    except ValueError as e:
        print(e)


def handle_list_clients():
    results = list_clients()

    if not results:
        print("Nenhum cliente cadastrado.")
    else:
        print("\n--- Clientes cadastrados ---")
        for client in results:
            client_id, name, email, phone, document = client
            print(
                f"ID: {client_id} | Nome: {name} | Email: {email} | Telefone: {phone} | Documento: {document}"
            )


def handle_search_clients():
    while True:
        mostrar_menu_busca()
        option_find = input("Escolha uma opção: ")

        if option_find == "0":
            print("Voltando ao menu principal.")
            break

        elif option_find == "1":
            data = input("Digite o nome: ").strip()
            results = search_clients_name(data)
            print_clients(results)

        elif option_find == "2":
            data = input("Digite o email: ")
            results = search_clients_email(data)
            print_clients(results)

        elif option_find == "3":
            data = input("Digite o documento: ")
            results = search_clients_document(data)
            print_clients(results)

        else:
            print("Opção inválida. Tente novamente.")
