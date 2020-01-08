from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
import numpy as np


g = 9.8106
# g

# m
y = [0, 3, 6, 9, 12, 15.5, 19, 22.5, 25.75, 29, 32.25]

x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


# find best fit

def fit_func(x, a, b):
    return x*a+b


params = curve_fit(
    fit_func, x, y)
a = params[0][0]
b = params[0][1]


print(params)
err = params[1][0][0]**(1/2)/a
print('naklon grafa: a =', a, ', b =', b, 'err=', err)
print('hitrost je', a**-1 * 10**3, '+-', err*a * 10**3)

x_fit = np.linspace(x[0], x[-1], 100)

y_fit = fit_func(x_fit, a, b)

# /fit


plt.plot(x, y, 'o')
plt.plot(x_fit, y_fit, label=r'$k$')


plt.title(f'Časovna razlika s povečevanjem razdalje med spremenikom in oddajnikom')
plt.ylabel(r'$\Delta t [\mu s]$')
plt.xlabel(r'$\Delta x [mm]$')

plt.grid(True)

plt.legend()
# plt.savefig(f'./raztezek_{}_zice', dpi=300)
# print('saved')
plt.show()
