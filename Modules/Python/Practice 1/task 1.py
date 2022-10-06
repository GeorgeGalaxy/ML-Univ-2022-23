import math

def calculator():

    symbol = input('Введите операцию (+, -, *, /, ^, %, sqrt):')

    if symbol not in ('+, -, *, /, ^, %, sqrt'.split(', ')):
        return 'Error'

    first = int(input())
    if symbol != 'sqrt':
        second = int(input())

    if symbol == "+":
        return (f'{first} + {second} = {first + second}')
    elif symbol == "-":
        return (f'{first} - {second} = {first - second}')
    elif symbol == "*":
        return (f'{first} * {second} = {first * second}')
    elif symbol == "^":
        return (f'{first} ^ {second} = {first ** second}')
    elif symbol == "%":
        return (f'{first} % {second} = {first % second}')
    elif symbol == "sqrt":
        return (f'sqrt of {first}  = {math.sqrt(first)}')
    elif symbol == "/" or symbol == "del":
        if second != 0:
            return (f'{first} / {second} = {first / second:.4f}')
        else:
            return 'Error'

print(calculator())