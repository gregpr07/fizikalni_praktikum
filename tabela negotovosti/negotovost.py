from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

####################################################################
####################################################################

racunamo = 'g'

text_size = 15

h, s, t = symbols('h s t')


data = [
    (h, [0.0994, 0.00001]),
    (s, [0.215, 0.001]),
    (t, [0.110856, 0.00005])
]

function = ((sqrt(2 * h) +
             sqrt(2 * (h + s))) / t)**2


####################################################################
####################################################################

values = [(x[0], x[1][0]) for x in data]

results = []

for el in data:
    deriv = Derivative(function, el[0])
    res = deriv.doit()
    deltaa = el[1][1]
    error = float(deriv.doit().subs(values) * deltaa)
    latfunc = '$'+latex(res)+'$'
    results.append((latfunc, deltaa, '%.4E' % Decimal(error)))

final_error = sqrt(sum([abs(float(x[2])) for x in results]))
print(final_error)

if not text_size:
    text_size = 15

columns = [r'$\frac{da}{dx}$',
           r'$\Delta a$', r'$(\Delta a \frac{da}{dx})^2$']
rows = [x[0] for x in data]

plt.title('Negotovost za funkcijo')

plt.xticks([])
plt.yticks([])

plt.subplots_adjust(left=0.03, bottom=0, right=0.96, top=0.94)

plt.axis('off')

table = plt.table(cellText=results, loc='center left',
                  rowLabels=rows, colLabels=columns)

plt.text(0.35, 0.85, '$'+latex(function)+'$', fontsize=text_size+5)
table.set_fontsize(text_size)
table.scale(1, 4)
table.auto_set_font_size(False)

plt.text(0.35, 0.1, r'$\Delta '+racunamo+' = ' +
         str(final_error)+'$', fontsize=text_size+4)


plt.show()
