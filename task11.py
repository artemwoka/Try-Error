"""
Помилки (номери рядків через пробіл): !!!
"""


class NoMoneyToWithdrawError(Exception):
    pass


class PaymentError(Exception):
    pass


def print_accounts(accounts):
    """Друк акаунтів."""
    print(f"Список клієнтів ({len(accounts)}): ")
    for i, (name, value) in enumerate(accounts.items(), start=1):
        print(f"{i}. {name} {value}")


def transfer_money(accounts, account_from, account_to, value):
    """Виконати переказ 'value' грошей з рахунку 'account_from' на 'account_to'.

    При переказі коштів необхідно враховувати:
        - чи вистачає грошей на рахунку, з якого здійснюється переказ;
        - переказ складається зі зменшення балансу першого рахунку та збільшення
          балансу другого; якщо хоча б на одному етапі відбувається помилка,
          облікові записи повинні бути приведені в початковий стан
          (механізм транзакції)
          см. https://uk.wikipedia.org/wiki/Транзакція_(бази_даних)

    Винятки (raise):
        - NoMoneyToWithdrawError: на рахунку 'account_from'
                                  не вистачає грошей для переказу;
        - PaymentError: помилка під час переказу.
    """
    if accounts[account_from] < value:
        raise NoMoneyToWithdrawError(
            f"На рахунку '{account_from}' не вистачає грошей для переказу."
        )
    original_from_balance = accounts[account_from]
    original_to_balance = accounts[account_to]
    try:
        accounts[account_from] -= value
        accounts[account_to] += value
    except Exception as e:
        # Відновлення початкових балансів у разі помилки
        accounts[account_from] = original_from_balance
        accounts[account_to] = original_to_balance
        raise PaymentError(f"Помилка під час переказу: {e}")

    # Видаліть коментар та допишіть код


if __name__ == "__main__":
    accounts = {
        "Василь Іванов": 100,
        "Іван Васильєв": 1500,
        "Петро Бондаренко": 400
    }
    print_accounts(accounts)

    payment_info = {
        "account_from": "Василь Іванов",
        "account_to": "Іван Васильєв"
    }

    print("Переказ від {account_from} для {account_to}...".
          format(**payment_info))
    try:
        payment_info["value"] = int(input("Сума = "))

        transfer_money(accounts, **payment_info)

        print("OK!")

        print_accounts(accounts)
    except ValueError:
        print("Помилка: введено некоректне значення. Будь ласка, введіть число.")
    except NoMoneyToWithdrawError as nmwe:
        print(f"Помилка: {nmwe}")
    except PaymentError as pe:
        print(f"Помилка: {pe}")
    except KeyError as ke:
        print(f"Помилка: невідомий рахунок: {ke}")
    except Exception as e:
        print(f"Сталася помилка: {e}")