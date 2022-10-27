class Nikola:
    __slots__ = ('name', 'age')


    def __init__(self, name=None, age=None):
        if name == None or name == 'Николай':
            self.name = 'Николай'
        else:
            self.name = f'Я не {name}, а Николай'

        self.age = age


Mike = Nikola('Миша', '21')
Nikolay = Nikola('Николай', '18')
empty_name = Nikola()

print(Mike.name, Mike.age)
print(Nikolay.name, Nikolay.age)
print(empty_name.name, empty_name.age)
