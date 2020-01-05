from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
import numpy as np


g = 9.8106
# g
mase = [0, 10, 50, 100, 150, 200]

# m
y = [0.781, 0.784, 0.801, 0.820, 0.841, 0.860]

x = [l*g/1000 for l in mase]


# find best fit

def fit_func(x, a, b):
    return x*a+b


params = curve_fit(
    fit_func, x, y)
a = params[0][0]
b = params[0][1]


print(params)
err = params[1][0][0]**(1/2)/a
print('k je', a**-1, '+-', err**(-1/2))

x_fit = np.linspace(x[0], x[-1], 100)

y_fit = fit_func(x_fit, a, b)

# /fit


plt.plot(x, y, 'o', label='Dodajanje uteži')
plt.plot(x_fit, y_fit, label=r'$k$')


plt.title(f'Raztezek zvmeti v odvisnosti od sile na vzmet')
plt.ylabel(r'$x$')
plt.xlabel(r'$mg$')

plt.grid(True)

plt.legend()
# plt.savefig(f'./raztezek_{}_zice', dpi=300)
print('saved')
plt.show()
