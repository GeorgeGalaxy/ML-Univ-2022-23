import os

with open('data/task2_file.txt', 'r') as fr:

    file_data = fr.read()
    with open('data/task2_file_copy.txt', 'w') as fw:
        fw.write(file_data)

os.remove('data/task2_file.txt')
