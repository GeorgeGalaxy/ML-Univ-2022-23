def get_coordinate(t, x0, v=10, a=5):

    x = x0 + v*t + (a * (t ** 2) / 2)

    return x


t = int(input('t = '))
x0 = int(input('x0 = '))

print(f'Ваша координата = {get_coordinate(t, x0)}')
