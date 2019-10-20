from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
import numpy as np

mase = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1000]  # g

lege_dodajanje = [12.17, 12.22, 12.26, 12.30,
                  12.34, 12.38, 12.42, 12.48, 12.65, 12.74]  # cm

lege_odstranjanje = [12.45, 12.50, 12.535, 12.57,
                     12.60, 12.64, 12.67, 12.70, 12.73, 12.74]  # cm

# pi*(2r/2)^2
# 2r podan v mikrom
presek = ((54/2/(10**6))**2)*math.pi  # m

dolzina = 1.995  # m


def calc_delta(lege):
    new_list = []
    for i in range(len(lege)):
        if i == 0:
            new_list.append(0)
        else:
            new_list.append(lege[i]-lege[0])
    print(new_list)
    return(new_list)  # cm


# N / cm^2 --> /100 je za g v N, /10000 je za m^2 v cm^2
x = [(x-mase[0])/100/presek/10000 for x in mase]

delte_y = calc_delta(lege_dodajanje)

y = [(y/100/dolzina) for y in delte_y]  # brez enote

# error


# find best fit


def fit_func(x, a):
    return a*x


params = curve_fit(fit_func, x[:(len(x)-2)], y[:(len(y)-2)])
[a] = params[0]

x_fit = np.linspace(x[0], x[len(x)-1], 100)

y_fit = fit_func(x_fit, a)


# /fit

print("Calculated E is:", '%.3g' % int(a**-1), 'N/cm^2')


plt.plot(x, y, 'o', label='Meritve')
plt.plot(x_fit, y_fit, label=r'$1/E$')
plt.errorbar(x, y)

plt.title('Raztezek bakrene zice v odvisnosti od sile')
plt.xlabel(r'$(F −F_o)/S$ $[N/cm^2]$')
plt.ylabel(r'$\Delta l \: / \: l$')

plt.grid(True)

plt.legend()
plt.savefig('raztezek_baker', dpi=300)
plt.show()
