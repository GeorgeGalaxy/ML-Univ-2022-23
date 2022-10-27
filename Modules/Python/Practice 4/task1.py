class Soda:
    def __init__(self, additive=''):
        self.additive = additive


    def show_my_drink(self):
        if self.additive == '':
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.additive}')


simple_Soda = Soda()
simple_Soda.show_my_drink()

lemon_Soda = Soda('лимон')
lemon_Soda.show_my_drink()
