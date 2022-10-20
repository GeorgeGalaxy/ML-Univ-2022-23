import random


def find_specialties():

    N = random.randint(15, 30)
    data = [random.randint(0, 1) for _ in range(N)]

    for el in data:

        try:
            i_try = 10 / el

        except ZeroDivisionError:
            print('деление на 0')


find_specialties()
