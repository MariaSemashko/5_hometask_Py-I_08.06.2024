'''Создайте функцию генератор чисел Фибоначчи'''

def fibonacchi_generator(count):
    number_1 = 1
    number_2 = 1

    if count == 1:
        yield number_1
    else:
        count -= 2
        yield number_1
        yield number_2
        while count:
            number_1, number_2 = number_2, number_1 + number_2
            yield number_2
            count -= 1

for item in fibonacchi_generator(4):
    print(item)
