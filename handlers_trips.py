from datetime import datetime

from db import (
    get_client,
    get_trip,
    get_trip_full,
    insert_trip,
    list_trips_by_client,
    update_trip_status,
    update_trip,
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


def handle_edit_trip():
    trip_id = ask_int("Digite o id da viagem: ")
    trip = get_trip_full(trip_id)
    if not trip:
        print("Não existe viagem com o id selecionado.")
        return
    (
        trip_id_db,
        client_id,
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
        f"ID Viagem: {trip_id_db} | ID Cliente: {client_id} | Destino: {destination} | Data de ida: {start_date} | Data de volta: {end_date_display} | Quantidade de pessoas: {travelers_qty}"
    )
    print(
        f"Passagem: {format_yes_no(flight)} | Hospedagem: {format_yes_no(hotel)} | Carro: {format_yes_no(car)} | Seguro: {format_yes_no(insurance)} | Status: {status}"
    )

    flight = bool(flight)
    hotel = bool(hotel)
    car = bool(car)
    insurance = bool(insurance)

    final_destination = destination
    change_destination = ask_yes_no("Deseja alterar o destino? (s/n): ")
    if change_destination:
        new_destination = input("Digite o novo destino: ").strip()
        if not new_destination:
            print("Entrada inválida. Destino não alterado.")
            final_destination = destination
        else:
            final_destination = new_destination

    start_date_date = (
        datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None
    )

    if start_date_date is None:
        print("Esta viagem não possui data de ida cadastrada.")
        final_start_date = ask_future_date("Informe a data de ida (YYYY-MM-DD): ")
    else:
        final_start_date = start_date_date

    end_date_date = datetime.strptime(end_date, "%Y-%m-%d").date() if end_date else None

    final_end_date = end_date_date

    change_start_date = ask_yes_no("Deseja alterar a data de ida? (s/n): ")
    if change_start_date:
        final_start_date = ask_future_date("Digite a nova data de ida (YYYY-MM-DD): ")

    oneway = ask_yes_no("A viagem é somente ida? (s/n): ")

    if oneway:
        final_end_date = None
    else:
        if (
            final_end_date is None
            or final_end_date < final_start_date
            or ask_yes_no("Deseja alterar a data de volta? (s/n): ")
        ):
            final_end_date = ask_return_date(final_start_date)

    final_start_date_str = final_start_date.isoformat()
    final_end_date_str = final_end_date.isoformat() if final_end_date else None
    final_travelers_qty = travelers_qty
    change_travelers_qty = ask_yes_no("Deseja alterar a quantidade de pessoas? (s/n): ")
    if change_travelers_qty:
        new_travelers_qty = ask_int("Digite a quantidade de pessoas: ", min_value=1)
        final_travelers_qty = new_travelers_qty
    final_flight = flight
    change_flight = ask_yes_no("Deseja alterar passagem? (s/n): ")
    if change_flight:
        new_flight = ask_yes_no("Deseja passagem? (s/n): ")
        final_flight = new_flight
    final_hotel = hotel
    change_hotel = ask_yes_no("Deseja alterar hotel? (s/n): ")
    if change_hotel:
        new_hotel = ask_yes_no("Deseja hotel? (s/n): ")
        final_hotel = new_hotel
    final_car = car
    change_car = ask_yes_no("Deseja alterar carro? (s/n): ")
    if change_car:
        new_car = ask_yes_no("Deseja carro? (s/n): ")
        final_car = new_car
    final_insurance = insurance
    change_insurance = ask_yes_no("Deseja alterar seguro? (s/n): ")
    if change_insurance:
        new_insurance = ask_yes_no("Deseja seguro? (s/n): ")
        final_insurance = new_insurance

    flight_int = 1 if final_flight else 0
    hotel_int = 1 if final_hotel else 0
    car_int = 1 if final_car else 0
    insurance_int = 1 if final_insurance else 0

    updated_trip = update_trip(
        trip_id_db,
        final_destination,
        final_start_date_str,
        final_end_date_str,
        final_travelers_qty,
        flight_int,
        hotel_int,
        car_int,
        insurance_int,
    )
    if updated_trip == 1:
        print("Viagem atualizada com sucesso.")
        return
    else:
        print("Nenhuma alteração realizada ou viagem não encontrada.")


def handle_list_trips():
    client_id = ask_int("Digite o id do cliente: ")
    client = get_client(client_id)
    if not client:
        print("Nenhum cliente com o id selecionado.")
        return
    trips = list_trips_by_client(client_id)
    print_trips(trips)


def handle_update_trip_status():
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
