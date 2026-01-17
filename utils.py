from datetime import datetime


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
            start_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
            return start_date
        except ValueError:
            print("Digite uma data válida no formato YYYY-MM-DD")
            continue


def ask_future_date(prompt):
    while True:
        prompt_date = ask_date(prompt)
        if prompt_date < datetime.now().date():
            print("A data não pode ser anterior à data de hoje.")
            continue
        return prompt_date


def ask_return_date(start_date):
    while True:
        end_date = ask_future_date("Digite a data de retorno (YYYY-MM-DD): ")
        if end_date < start_date:
            print("A data de retorno não pode ser anterior à data de partida.")
            continue
        else:
            return end_date


def format_yes_no(value):
    sim = "Sim"
    nao = "Não"
    if value == 1 or value == True:
        return sim
    else:
        return nao
