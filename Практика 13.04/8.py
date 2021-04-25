def fstepen(year):
    if year >= 1 and year <= 4:
        print("Первая степнь среднего образования")
    elif year >= 5 and year <= 9:
        print("Вторая степнь среднего образования")
    elif year >= 10 and year <= 11:
        print("Третья степнь среднего образования")
    else:
        print("Ошибка ввода")
fstepen(int(input()))