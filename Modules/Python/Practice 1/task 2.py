import numpy as np

def word_generator():

    nouns = []
    verbs = []

    nouns.append(input('Noun: '))
    while nouns[-1] != 'стоп слово':
        nouns.append(input('Noun: '))

    nouns.pop(-1)

    verbs.append(input('Verb: '))
    while verbs[-1] != 'стоп слово':
        verbs.append(input('Verb: '))

    verbs.pop(-1)

    amount = int(input('Amount of phrases: '))
    phrase_type = input('Phrase type (сгс,гсс,ссг): ')

    for i in range(amount):
        for phrase in phrase_type:
            if phrase == 'г':
                print(np.random.choice(verbs, 1)[0], end=' ')
            elif phrase == 'с':
                print(np.random.choice(nouns, 1)[0], end=' ')

        print()


word_generator()
