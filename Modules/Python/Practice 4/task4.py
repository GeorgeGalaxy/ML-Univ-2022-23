class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, new_kg):

        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')


weight = KgToPounds(74)
print(f'Before setting: {weight.kg}')
weight.kg = 72
print(f'After setting: {weight.kg}')
print(f'{weight.kg} kg = {weight.to_pounds()} pounds')
