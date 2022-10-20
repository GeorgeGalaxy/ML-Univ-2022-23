s = input('Ваша строка: ')

try:
    with open('data/task2_file.txt', 'r') as f:
        pass

    with open('data/task2_file.txt', 'a') as fw:
        fw.write(f'\n{s}')

except FileNotFoundError:

    with open('data/task2_file.txt', 'a') as fw:
        fw.write(f'\n{s}')