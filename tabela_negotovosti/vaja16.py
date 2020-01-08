from negotovost import Negotovost

popravek = 2*3.14

data = [
    # togo
    [
        ('alpha', 3.293/popravek, 0.001),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.05, 0.001),
        ('g', 9.81066, 0),
    ],
    [
        ('alpha', 10.19/popravek, 0.04),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.15, 0.001),
        ('g', 9.81066, 0),
    ],
    # vpeto
    [
        ('alpha', 2.058/popravek, 0.008),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.05, 0.001),
        ('g', 9.81066, 0),
    ], [
        ('alpha', 6.33/popravek, 0.04),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.15, 0.001),
        ('g', 9.81066, 0),
    ],
    # gibljivo
    [
        ('alpha', 2.066/popravek, 0.007),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.05, 0.001),
        ('g', 9.81066, 0),
    ],  [
        ('alpha', 6.383/popravek, 0.028),
        ('rg', 0.041/2, 0.0001/2),
        ('m', 0.15, 0.001),
        ('g', 9.81066, 0),
    ],
]

function = 'm*(rg*g-rg^2*alpha)/alpha'


res = []
for el in data:
    x = Negotovost(el, function).calculate_error()
    res.append(x[0])
    print(x)


dat1 = [
    ('J', res[0], 0.000066),
    ('R', 0.095/2, 0.0001/2),
    ('d', 0.151/(2)**(1/2), 0.001),
    ('m', 0.514, 0.001),
    ('g', 9.81066, 0),
]

f1 = 'J+2* (1/2*m*R^2+m*d^2)'

Negotovost(dat1, f1).draw_table(variable='J_2')

f2 = 'J+2* (m*d^2)'

Negotovost(dat1, f2).draw_table(variable='J_3')
