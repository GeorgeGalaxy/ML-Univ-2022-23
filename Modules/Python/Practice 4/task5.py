class RealString:
    def __init__(self, str1='some 1', str2='some 2'):
        self.str1 = str1
        self.str2 = str2


    def __eq__(self, other):

        if len(self.str1) > len(other.str1):
            return f'{self.str1} > {other.str1}'

        elif len(self.str1) < len(other.str1):
            return f'{self.str1} < {other.str1}'

        else:
            return f'{self.str1} = {other.str1}'


s2 = RealString('Su')
s4 = RealString('Alex')
s6 = RealString('George')

print(s4 == s6)
print(s4 == s2)
print(s2 == s6)

print(s2.str1 < s2.str2) # True: 2 < 4
