try:

    with open('data/task3_file.txt', 'r') as f:
        pass

    with open('data/task3_file.txt', 'r') as f:
        print(f.read())

except:
    print('Файла нет')