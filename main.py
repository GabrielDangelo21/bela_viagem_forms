from datetime import datetime

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
                f"ID: {client_id} | Nome: {name} | Email: {email} | Telefone: {phone} | Documento: {document}"
            )


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("s", "sim", "y", "yes"):
            return True
        elif answer in ("n", "nao", "não", "no"):
            return False
        else:
            print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def ask_int(prompt, min_value=1):
    while True:
        try:
            answer = int(input(prompt).strip())
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue
        if answer < min_value:
            print(f"Digite um número maior ou igual a {min_value}.")
            continue
        else:
            return answer


def ask_date(prompt):
    while True:
        raw_date = input(prompt).strip()
        try:
            start_date = datetime.strptime(raw_date, "%Y-%m-%d")
            return start_date.date()
        except ValueError:
            print("Digite uma data válida no formato YYYY-MM-DD")
            continue


def ask_return_date(start_date):
    while True:
        end_date = ask_date("Digite a data de retorno (YYYY-MM-DD): ")
        if end_date < start_date:
            print("A data de retorno não pode ser anterior à data de partida.")
            continue
        else:
            return end_date


def handle_create_trip():
    client_id = ask_int("Digite o id do cliente: ")

    client = get_client(client_id)
    if not client:
        print("Nenhum cliente com o id selecionado.")
        return

    destination = input("Digite o destino: ").strip()
    if not destination:
        print("Digite um destino.")
        return

    start_date = ask_date("Digite a data de partida: (YYYY-MM-DD) ")
    start_date_str = start_date.isoformat()
    oneway = ask_yes_no("A viagem é somente ida? (s/n): ")
    end_date_str = None
    if oneway:
        end_date_str = None
    else:
        end_date = ask_return_date(start_date)
        end_date_str = end_date.isoformat() if end_date else None

    travelers_qty = ask_int("Digite a quantidade de pessoas: ", min_value=1)

    flight = ask_yes_no("Deseja passagem? (s/n): ")
    hotel = ask_yes_no("Deseja hospedagem? (s/n): ")
    car = ask_yes_no("Deseja alugar um carro? (s/n): ")
    insurance = ask_yes_no("Deseja contratar um seguro? (s/n): ")

    flight_int = 1 if flight else 0
    hotel_int = 1 if hotel else 0
    car_int = 1 if car else 0
    insurance_int = 1 if insurance else 0

    try:
        trip_id = insert_trip(
            client_id,
            destination,
            start_date_str,
            end_date_str,
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
            handle_create_trip()

        else:
            print("Opção inválida. Tente novamente.")
