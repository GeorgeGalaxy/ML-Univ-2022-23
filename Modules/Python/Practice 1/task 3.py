import difflib

def check_sentences():

    count = int(input('Число правильных слов: '))
    checkers = [input() for _ in range(count)]

    sentence = input('Предложение:\n').split()

    for word in sentence:
        for checker in checkers:
            if len(checker) == len(word):

                diff = 0

                for i in range(len(word)):
                    if checker[i] != word[i]:
                        diff += 1
                        diff_idx = i
                        diff_char = word[i]

                if diff == 1:
                    print(f'{word[:diff_idx]} {diff_char} {word[diff_idx+1:]}')


check_sentences()
