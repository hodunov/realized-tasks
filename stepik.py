"""
Всем известно, что ведьмак способен одолеть любых чудовищ, 
однако его услуги обойдутся недешево, к тому же ведьмак не принимает купюры, 
он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1,5,10,25.

Напишите программу, которая определяет какое минимальное количество чеканных монет нужно заплатить ведьмаку.
Формат входных данных 
На вход программе подается одно натуральное число, цена за услугу ведьмака.
Формат выходных данных
Программа должна вывести минимально возможное количество чеканных монет для оплаты.
"""

def min_minted_coin(coin):
    count = 0
    wallet = (25,10,5,1)
    for value in wallet:
        ceil = int(coin/value)
        coin = coin % value
        count += ceil
    return count

print(min_minted_coin(49)) # 7
print(min_minted_coin(74)) # 8
print(min_minted_coin(5)) # 1