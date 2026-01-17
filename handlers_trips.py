from db import (
    get_client,
    get_trip,
    insert_trip,
    list_trips_by_client,
    update_trip_status,
)
from utils import ask_future_date, ask_int, ask_return_date, ask_yes_no, format_yes_no


def mostrar_menu_status() -> None:
    print("\n=== STATUS DE CLIENTES ===")
    print("1. RASCUNHO")
    print("2. COTACAO")
    print("3. RESERVADO")
    print("4. PAGO")
    print("5. CANCELADO")
    print("0. Sair")


def print_trips(trips):
    if not trips:
        print("Nenhuma viagem encontrada.")
    else:
        print("\n--- Viagens encontradas ---")
        for trip in trips:
            (
                trip_id,
                destination,
                start_date,
                end_date,
                travelers_qty,
                flight,
                hotel,
                car,
                insurance,
                status,
            ) = trip
            end_date_display = end_date if end_date else "Somente ida"
            print("")
            print(
                f"ID: {trip_id} | Destino: {destination} | Data de ida: {start_date} | Data de volta: {end_date_display} | Quantidade de pessoas: {travelers_qty}"
            )
            print(
                f"Passagem: {format_yes_no(flight)} | Hospedagem: {format_yes_no(hotel)} | Carro: {format_yes_no(car)} | Seguro: {format_yes_no(insurance)} | Status: {status}"
            )


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

    start_date = ask_future_date("Digite a data de partida: (YYYY-MM-DD) ")
    start_date_str = start_date.isoformat()
    oneway = ask_yes_no("A viagem é somente ida? (s/n): ")
    end_date_str = None
    if not oneway:
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


def handle_list_trips():
    client_id = ask_int("Digite o id do cliente: ")
    client = get_client(client_id)
    if not client:
        print("Nenhum cliente com o id selecionado.")
        return
    trips = list_trips_by_client(client_id)
    print_trips(trips)


def handle_update_trip():
    trip_id = ask_int("Digite o id da viagem: ")
    trip = get_trip(trip_id)
    if not trip:
        print("Não existe viagem com o id selecionado.")
        return
    trip_id_db, client_id, destination, status = trip
    print(
        f"ID: {trip_id_db} | Cliente: {client_id} | Destino: {destination} | Status: {status}"
    )

    status_option = ["RASCUNHO", "COTACAO", "RESERVADO", "PAGO", "CANCELADO"]

    while True:
        mostrar_menu_status()
        option_status_menu = ask_int("Escolha uma opção: ", min_value=0)

        if option_status_menu == 0:
            print("Cancelando...")
            break
        elif option_status_menu > len(status_option):
            print("Opção inválida. Tente novamente.")
            continue

        choice = option_status_menu - 1
        new_status = status_option[choice]
        if new_status == status:
            print(f"A viagem já está com status {status}")
            continue
        updated_status = update_trip_status(trip_id, new_status)
        if updated_status == 1:
            print("Status atualizado com sucesso.")
            break
        else:
            print("Viagem não encontrada ou status não alterado.")
            break
