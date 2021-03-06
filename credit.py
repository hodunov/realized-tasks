"""
Напишите программу (алгоритм), который вычисляет платежи про кредиту в зависимости от процентной ставки,
от размера первоначального взноса и от времени, на которое был взят кредит,
и представляет платежи по кредиту в виде таблицы.

Например:
- кредит был взят на 10 лет на сумму 100.000$
- ставка 5% годовых
- первоначальный взнос 5000$

Необходимо построить таблицу платежей со следующими колонками:

| номер месяца | остаток по кредиту | сумма платежа по кредиту | сумма платежа по процентам |
общая сумма платежа за данный месяц |
"""

from prettytable import PrettyTable  # pip install prettytable


def input_positive_integer(input_message, negative_value_message, value_error_message,
                           max_value=0, max_value_message="Вы ввели слишком большое число"):
    """
    Проверяем пользовательский ввод
    Args:
        input_message (str): приглашение к вводу
        negative_value_message (str): ответ при неверном вводе
        value_error_message (str): ответ при ошибке
        max_value (int):максимальное значение, positive integer. Defaults to 0.
        max_value_message (str, optional): ответ при вводе числа, больше максимального.
                                            Defaults to "Вы ввели слишком большое число".

    Returns:
        int: positive integer
    """
    while True:
        try:
            value = int(input(f"{input_message} - "))
            if value < 0:
                print(negative_value_message)
                continue
            if max_value and value > max_value:
                print(max_value_message)
                continue
            return value
        except ValueError:
            print(value_error_message)
            continue


credit_term = input_positive_integer("Введите срок кредита в годах",
                                     "Срок не может быть отрицательным. Попробуйте ещё раз",
                                     "Введите целое число",
                                     )
credit_amount = input_positive_integer("Введите сумму кредита",
                                       "Сумма не может быть отрицательной. Попробуйте ещё раз",
                                       "Введите число",
                                       )
interest_rate = input_positive_integer("Введите процентную ставку",
                                       "Процент не может быть отрицательным. Попробуйте ещё раз",
                                       "Введите только число"
                                       )
down_payment = input_positive_integer("Введите сумму первоначального взноса",
                                      "Сумма не может быть отрицательной. Попробуйте ещё раз",
                                      "Введите число",
                                      max_value=credit_amount,
                                      max_value_message="Первоначальный взнос не может быть больше суммы кредита"
                                      )


# Вычитаем первоначальный взнос из суммы кредита:
credit_amount -= down_payment


def month_payment(amount, term, rate):
    """
    Аналог функции ПЛТ в Excel
    https://exceltable.com/funkcii-excel/primery-funkcii-plt
    Возвращает размер периодического платежа
    для аннуитета с учетом постоянства сумм платежей и процентной ставки.
    Args:
        amount (int): размер займа
        term (int): срок займа, мес
        rate (int): % годовых

    Returns:
        int: размер ежемесячного платежа
    """

    rate = rate / 100
    month_rate = rate / 12
    term = term * 12
    payment = amount * (month_rate * (1 + month_rate) ** term) / ((1 + month_rate) ** term - 1)
    return payment


def outstanding_balance(balance, month, payment):
    """
    Остаток задолженности по кредиту

    Args:
        balance (int): сумма кредита
        month (list): список месяцев
        payment (int): выплата основного долга

    Returns:
        [type]: [description]
    """
    result = [balance]  # добавляем остаток в первый месяц
    for item in range(len(month) - 1):
        # вычитаем из текущего баланса выплату основного долга
        balance = balance - payment
        result.append(balance)
    return result


# Список месяцев
months = [month for month in range(1, credit_term * 12 + 1)]

# Размер основного долга
principal_payment = credit_amount / (credit_term * 12)

# Остаток задолженности по кредиту
balance_of_debt = outstanding_balance(balance=credit_amount, month=months, payment=principal_payment)

# Выплата процентов
interest_payment = [payment * (interest_rate / 100 / 12) for payment in balance_of_debt]

# Итоговый платёж
result_payment = [payment + principal_payment for payment in interest_payment]

# Формируем итоговую таблицу
credit = PrettyTable()
credit.add_column('Месяц', months)
credit.add_column('Остаток по кредиту', [round(num, 2) for num in balance_of_debt])
credit.add_column("Сумма платежа по кредиту", [round(num, 2) for num in [principal_payment] * len(months)])
credit.add_column('Сумма платежа по процентам', [round(num, 2) for num in interest_payment])
credit.add_column("Общая сумма платежа", [round(num, 2) for num in result_payment])

print("Ежемесячный платеж: ", round(month_payment(amount=credit_amount, term=credit_term, rate=interest_rate), 2))
print(credit)

"""
Result example:

Введите срок кредита в годах - 1
Введите сумму кредита - 10000
Введите процентную ставку - 5
Введите сумму первоначального взноса - 500
Ежемесячный платеж:  813.27
+-------+--------------------+--------------------------+----------------------------+---------------------+
| Месяц | Остаток по кредиту | Сумма платежа по кредиту | Сумма платежа по процентам | Общая сумма платежа |
+-------+--------------------+--------------------------+----------------------------+---------------------+
|   1   |        9500        |          791.67          |           39.58            |        831.25       |
|   2   |      8708.33       |          791.67          |           36.28            |        827.95       |
|   3   |      7916.67       |          791.67          |           32.99            |        824.65       |
|   4   |       7125.0       |          791.67          |           29.69            |        821.35       |
|   5   |      6333.33       |          791.67          |           26.39            |        818.06       |
|   6   |      5541.67       |          791.67          |           23.09            |        814.76       |
|   7   |       4750.0       |          791.67          |           19.79            |        811.46       |
|   8   |      3958.33       |          791.67          |           16.49            |        808.16       |
|   9   |      3166.67       |          791.67          |           13.19            |        804.86       |
|   10  |       2375.0       |          791.67          |            9.9             |        801.56       |
|   11  |      1583.33       |          791.67          |            6.6             |        798.26       |
|   12  |       791.67       |          791.67          |            3.3             |        794.97       |
+-------+--------------------+--------------------------+----------------------------+---------------------+
"""
