number = input('Число: ')
sum = 0

for digit in number:
    sum += int(digit)

print(f'Для числа {number} сумма цифр = {sum}')
