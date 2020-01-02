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
enote = r'\frac{m}{s^2}'

# stevilo racunskih mest pri koncnem rezultatu (output)
natancnost_mest = 5

# vazn samo za koncn output, za velikost texta
text_size = 20

# za vsak simbol k se ga uporab v enacbi (function) je treba narest symbol (lahko je z latex formatingom, samo more bit r'')
r, l, T, x, lambdaa = symbols(r'r l t_0 x \Lambda')

# za vsako neznanko nrdimo tuple, (x, []) prvi el v listu je velikost neznanke, drugi el je napaka
data = [
    (l, [2.140, 0.005]),
    (T, [(2*60+25+(0.5+0.67+0.74+0.78)/4)/49, 0.0011]),
    (r, [0.0554, 0.0066]),
    (x, [0.0892, 0.0002]),
    (lambdaa, [9.6*10**-5, 2.7*10**-5]),
]

hide = []

print((2*60+25+(0.5+0.67+0.74+0.78)/4)/49)

alfa = atan(x/(l+r))

mz = l*0.0002**2*math.pi*7850
mk = 3*r**3*math.pi/4*7870


popravki = 1 + 1/2*(sin(alfa/2))**2 + (0.4 * (r/(l+r))**2) - 1/6*mz/mk + \
    1.6*1.3/7870 + (lambdaa/2/pi)**2

# drugi razvoj sinusa ne vpliva vec - mansa razlika od napake
function = ((l+r) * 4 * pi**2)/T**2 * popravki


####################################################################
####################################################################

# ne spreminjat, mislm lah ampak se lah kej breaka


def format_text(num):
    return str(f'%.{natancnost_mest}E' % num).replace('+', '')


values = [(x[0], x[1][0]) for x in data]

results = []
formated_results = []

for el in data:
    if el[0] in hide:
        continue
    deriv = Derivative(function, el[0])
    res = deriv.doit()
    deltaa = el[1][1]
    error = (float(deriv.doit().subs(values) * deltaa))
    latfunc = (float(res.subs(values)))
    results.append((latfunc, deltaa, error))
    formated_results.append(
        (format_text(latfunc), format_text(deltaa), format_text(error)))


vrednost_f = float(function.doit().subs(values))

final_error = sqrt(sum([abs(float(x[2])**2) for x in results]))

if not text_size:
    text_size = 15

columns = [r'$\frac{\partial %s}{\partial x_i}$' % racunamo,
           r'$\sigma_i$', r'$\sigma_i \cdot \frac{\partial %s}{\partial x_i}$' % racunamo]
rows = ['$'+str(x[0])+'$' for x in data if x[0] not in hide]

# plt.title('Negotovost za funkcijo')

plt.xticks([])
plt.yticks([])

plt.subplots_adjust(left=0.03, bottom=0, right=0.97, top=0.94)

plt.axis('off')

table = plt.table(cellText=formated_results, loc='center left',
                  rowLabels=rows, colLabels=columns)

plt.text(0.1, 0.9, '$'+racunamo+'=' +
         latex(function)+'$', fontsize=text_size+5)
table.set_fontsize(text_size)
table.scale(1, 3)
table.auto_set_font_size(False)


latex_vrednost = format_text(vrednost_f)
latex_error = format_text(final_error)

print(latex_vrednost, '+-', latex_error)

plt.text(0.02, 0.1, r'$'+racunamo+' = (' + latex_vrednost + ' \pm ' +
         latex_error + ')' + enote + '$', fontsize=text_size+4)


plt.show()
