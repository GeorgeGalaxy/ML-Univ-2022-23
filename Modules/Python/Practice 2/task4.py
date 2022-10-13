import numpy as np

products = 'мясо; рыба; яйца; молоко; хлеб; ' \
           'крупы; макароны; бобовые; овощи; фрукты; ' \
           'ягоды; орехи; грибы; веганские; протеин'
products = products.split('; ')
print(f'Всего продуктов: {len(products)}')

amount = np.random.randint(1, len(products))

sample_1 = np.random.choice(products, amount, replace=False)
sample_2 = np.random.choice(products, amount, replace=False)

result = np.setxor1d(sample_1, sample_2)
print(f'Продукты, которые не повторяются: {result}')
