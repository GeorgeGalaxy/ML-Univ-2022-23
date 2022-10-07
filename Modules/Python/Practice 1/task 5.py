import numpy as np

names = ['Dart Vader', 'Yoda', 'Han Solo', 'Luke',
         'Obi-Wan', 'Rex', 'Anakin', 'Count Dooku']
ages = np.arange(10, 100)
classes = np.arange(0, 10)
parameters = ['Empire', 'Republic', 'Rebels', '1st Order']
characteristics = ['Jedi', 'Clone', 'Sith', 'Simple Human']

skills = ['Force', 'Pilot', 'Guns', 'Lightnings']


def generate_character():

    name = np.random.choice(names, 1)
    age = np.random.choice(ages, 1)
    ur_class = np.random.choice(classes, 1)
    parameter_s = np.random.choice(parameters, 1)
    characteristic_s = np.random.choice(characteristics, 1)

    number_of_skills = np.random.randint(1, len(skills))

    skill_s = np.random.choice(skills, number_of_skills, replace=False)

    print(f'Your character:\n')
    print('-'*20)
    print(f'Name           : {name}')
    print(f'Age            : {age}')
    print(f'Class          : {ur_class}')
    print(f'Parameters     : {parameter_s}')
    print(f'Characteristics: {characteristic_s}')
    print(f'Skills         : {skill_s}')


generate_character()
