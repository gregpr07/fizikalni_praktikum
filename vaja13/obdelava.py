from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
import numpy as np


data_x = [8.57469E-10, 1.12608E-09, 1.52588E-09, 1.91526E-09, 2.19384E-09,
          2.56369E-09, 2.79947E-09, 3.34124E-09, 3.98054E-09, 4.41496E-09]

data_y = [0.006, 0.01, 0.013, 0.014, 0.017, 0.02, 0.023, 0.025, 0.029, 0.032]


def fit_func(x, a):
    return a*x


params = curve_fit(
    fit_func, data_x, data_y)

a = params[0]

err = params[1][0][0]**0.5

print(a**-1, '$\pm$', err**-1)


x_fit = np.linspace(data_x[0], data_x[-1], 100)

y_fit = fit_func(x_fit, a)

plt.plot(data_x, data_y, 'o', label='Dodajanje uteži')
plt.plot(x_fit, y_fit, label=r'$1/E$')


plt.title(f'Razlike višine manometra v odvisnosti od prostorninskega pretoka')
plt.xlabel(r'$\Phi^2 [m^2/s^2]$')
plt.ylabel(r'$\Delta h$ v manometra $[m]$')

plt.grid(True)

plt.legend()
plt.savefig(f'./graf_manometer_pretok', dpi=300)
print('saved')
plt.show()
