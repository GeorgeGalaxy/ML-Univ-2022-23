class TriangleChecker:
    def __init__(self, a=0, b=0, c=0):
        if a < 0:
            self.a = 0
        else:
            self.a = a
        if b < 0:
            self.b = 0
        else:
            self.b = b
        if c < 0:
            self.c = 0
        else:
            self.c = c




    def is_triangle(self):
        if self.a + self.b >= self.c and \
           self.a + self.c >= self.b and \
           self.c + self.b >= self.a:
            return 'Ура, можно построить треугольник!'
        else:
            return 'Жаль, но из этого треугольник не сделать'


t1 = TriangleChecker(1, 2, 3)
t2 = TriangleChecker(3, 4, 5)
t3 = TriangleChecker(-1, 0, 1)

print(t1.is_triangle())
print(t2.is_triangle())
print(t3.is_triangle())
