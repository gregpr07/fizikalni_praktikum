# made with heart by Gregor Zunic

from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

'''
izracun nagotovsti v enacbah

treba je installat:

pip install sympy, numpy, matplotlib

kt v Projekt Tomo se spreminja samo stvari k so med ##   ##
'''

####################################################################
####################################################################

# to je samo vizualno da se vid kaj se za rezultat dubi
racunamo = 'g'

# stevilo racunskih mest pri koncnem rezultatu (output)
natancnost_mest = 4

# vazn samo za koncn output, za velikost texta
text_size = 20

# za vsak simbol k se ga uporab v enacbi (function) je treba narest symbol (lahko je z latex formatingom, samo more bit r'')
h, s, t, r = symbols(r'h s t r')

# za vsako neznanko nrdimo tuple, (x, []) prvi el v listu je velikost neznanke, drugi el je napaka
data = [
    (h, [0.0994, 0.00001]),
    (s, [0.215, 0.001]),
    (r, [0, 0.0001]),
]

# tuki se definira funkcijo, lahko se uporabla use funkcije eg. sin(), ln() iz numpy-ja in sympy-ja
function = ((sqrt(2*h) - sqrt(2*h+2*(s-r))) / t)**2

####################################################################
####################################################################

# ne spreminjat, mislm lah ampak se lah kej breaka


def format_text(num):
    return str(f'%.{natancnost_mest}E' % num).replace('+', '')


values = [(x[0], x[1][0]) for x in data]

results = []
formated_results = []

for el in data:
    deriv = Derivative(function, el[0])
    res = deriv.doit()
    deltaa = el[1][1]
    error = (float(deriv.doit().subs(values) * deltaa))
    latfunc = '$'+latex(res)+'$'
    results.append((latfunc, deltaa, error))
    formated_results.append((latfunc, deltaa, format_text(error)))


vrednost_f = float(function.doit().subs(values))

final_error = sqrt(sum([abs(float(x[2])**2) for x in results]))

if not text_size:
    text_size = 15

columns = [r'$\frac{\partial %s}{\partial x_i}$' % racunamo,
           r'$\sigma_i$', r'$\sigma_i \cdot \frac{\partial %s}{\partial x_i}$' % racunamo]
rows = ['$'+str(x[0])+'$' for x in data]

plt.title('Negotovost za funkcijo')

plt.xticks([])
plt.yticks([])

plt.subplots_adjust(left=0.03, bottom=0, right=0.97, top=0.94)

plt.axis('off')

table = plt.table(cellText=formated_results, loc='center left',
                  rowLabels=rows, colLabels=columns)

plt.text(0.35, 0.90, '$'+racunamo+'=' +
         latex(function)+'$', fontsize=text_size+5)
table.set_fontsize(text_size)
table.scale(1, 3)
table.auto_set_font_size(False)


latex_vrednost = format_text(vrednost_f)
latex_error = format_text(final_error)

print(latex_vrednost, '+-', latex_error)

plt.text(0.1, 0.02, r'$'+racunamo+' = ' + latex_vrednost + ' \pm ' +
         latex_error + '$', fontsize=text_size+4)


plt.show()
