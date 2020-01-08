from .tabela_negotovosti.negotovost import Negotovost

data = [
    ('rho', 13000, 0.1),
    ('d1', 0.006, 0.00001),
    ('d2', 0.0128, 0.1*10**-6)
]

function = 'rho*(1/(pi*d2^(2))**2-1/(pi*d1**2)**2)/2*(cos(rho))'


tabl = Negotovost(data, function)

tabl.draw_table()
