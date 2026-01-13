from db import (
    insert_client,
    list_clients,
    search_clients_name,
    search_clients_email,
    search_clients_document,
    get_client,
    insert_trip,
)


def mostrar_menu() -> None:
    print("\n=== GERENCIADOR DE CLIENTES ===")
    print("1. Cadastrar cliente")
    print("2. Listar cliente")
    print("3. Buscar cliente")
    print("4. Criar viagem")
    print("5. Listar viagem")
    print("6. Atualizar status da viagem")
    print("0. Sair")


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
                f"ID: {client_id} | Nome: {name} | Email: {email} | Documento: {document}"
            )


if __name__ == "__main__":

    while True:

        mostrar_menu()
        option = input("Escolha uma opção: ")

        if option == "0":
            print("Saindo...")
            break

        elif option == "1":
            nome = input("Nome: ").strip()

            if not nome:
                print("Nome é obrigatório.")
                continue

            email = input("Email: ").strip() or None
            telefone = input("Telefone: ").strip() or None
            documento = input("Documento: ").strip() or None

            try:
                new_id = insert_client(nome, email, telefone, documento)
                print("Cliente cadastrado com ID: ", new_id)
            except ValueError as e:
                print(e)

        elif option == "2":
            results = list_clients()

            if not results:
                print("Nenhum cliente cadastrado.")
            else:
                print("\n--- Clientes cadastrados ---")
                for client in results:
                    client_id, name, email, phone, document = client
                    print(
                        f"ID: {client_id} | Nome: {name} | Email: {email} | Documento: {document}"
                    )

        elif option == "3":
            while True:
                mostrar_menu_busca()
                option_find = input("Escolha uma opção: ")

                if option_find == "0":
                    print("Saindo...")
                    break

                elif option_find == "1":
                    data = input("Digite o nome: ")
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

        elif option == "4":
            client_id_raw = input("Digite o id do cliente: ").strip()
            try:
                client_id = int(client_id_raw)
            except ValueError:
                print("ID inválido. Digite um número.")
                continue

            client = get_client(client_id)
            if not client:
                print("Nenhum cliente com o id selecionado.")
                continue

            destination = input("Digite o destino: ").strip()
            start_date = input("Digite a data de ida (YYYY-MM-DD): ").strip()

            oneway = input("A viagem é somente ida? (s/n): ").strip().lower()
            if oneway == "n":
                end_date = input("Digite a data de volta (YYYY-MM-DD): ").strip()
            else:
                end_date = None

            travelers_qty_raw = input("Digite a quantidade de pessoas: ").strip()
            try:
                travelers_qty = int(travelers_qty_raw)
            except ValueError:
                print("Quantidade inválida. Digite um número.")
                continue

            flight = input("Deseja passagem? (s/n): ").strip().lower()
            hotel = input("Deseja hospedagem? (s/n): ").strip().lower()
            car = input("Deseja alugar um carro? (s/n): ").strip().lower()
            insurance = input("Deseja contratar um seguro? (s/n): ").strip().lower()

            flight_int = 1 if flight == "s" else 0
            hotel_int = 1 if hotel == "s" else 0
            car_int = 1 if car == "s" else 0
            insurance_int = 1 if insurance == "s" else 0

            try:
                trip_id = insert_trip(
                    client_id,
                    destination,
                    start_date,
                    end_date,
                    travelers_qty,
                    flight_int,
                    hotel_int,
                    car_int,
                    insurance_int,
                )
                print(
                    f"Viagem cadastrada para o cliente ID {client_id}. ID da viagem: {trip_id}"
                )
            except ValueError as e:
                print("Erro:", e)

        else:
            print("Opção inválida. Tente novamente.")
