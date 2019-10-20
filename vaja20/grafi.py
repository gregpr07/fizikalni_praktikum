from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
import numpy as np

mase = [150, 250, 350, 450, 550, 650, 750, 850, 950, 1000]  # g

lege_dodajanje = [12.17, 12.22, 12.26, 12.30,
                  12.34, 12.38, 12.42, 12.48, 12.65, 12.74]  # cm

lege_odstranjanje = [12.45, 12.50, 12.535, 12.57,
                     12.60, 12.64, 12.67, 12.70, 12.73, 12.74]  # cm

# 2r podan v mikrom
radij = 54

dolzina = 1.995  # m


def draw_graph(mase, lege_dodajanje, radij, dolzina, lege_odstranjanje=[]):

    # pi*(2r/2)^2
    presek = ((radij/2/(10**6))**2)*math.pi  # m

    def calc_delta(lege, reverse=False):
        new_list = []
        for i in range(len(lege)):
            if reverse:
                new_list.append(lege[i]-lege[-1])
            else:
                new_list.append(lege[i]-lege[0])
        return(new_list)  # cm

    # N / cm^2 --> /100 je za g v N, /10000 je za m^2 v cm^2
    x = [(x-mase[0])/100/presek/10000 for x in mase]

    # v cm
    delte_y = calc_delta(lege_dodajanje)

    # /100 cm -> m
    y = [(y/100/dolzina) for y in delte_y]  # brez enote

    y_reverse = [y[-1]+(rev/100/dolzina)
                 for rev in calc_delta(lege_odstranjanje, reverse=True)]

    print(y_reverse)
    # error

    def calc_error_y(delte, lege_y):
        abs_y = []
        for i, lega in zip(delte, lege_y):
            if i == 0:
                abs_y.append(0)
            else:
                print(0.005/i)
                abs_y.append((0.01/i)*lega)
        return abs_y

    def calc_error_x(mass, radius, x_axis):
        return [(20/x+2*1/radius)*abscisa for x, abscisa in zip(mass, x_axis)]

    napake_y = calc_error_y(delte_y, y)
    napake_x = calc_error_x(mase, radij, x)

    # find best fit

    def fit_func(x, a):
        return a*x

    params = curve_fit(fit_func, x[:(len(x)-2)], y[:(len(y)-2)])
    a = params[0]

    x_fit = np.linspace(x[0], x[-1], 100)

    y_fit = fit_func(x_fit, a)

    # /fit

    print("Calculated E is:", '%.3g' % int(a**-1), 'N/cm^2')

    plt.plot(x, y, 'o', label='Dodajanje uteži')
    plt.plot(x_fit, y_fit, label=r'$1/E$')
    plt.errorbar(x, y, xerr=napake_x, yerr=napake_y, fmt='none')

    if lege_odstranjanje:
        plt.plot(x, y_reverse, '.', label='Odstranjanje uteži')
        plt.errorbar(x, y_reverse, xerr=napake_x, yerr=napake_y, fmt='none')

        def fit_reverse(x, a, b):
            return a*x+b

        naklon_reverse = curve_fit(fit_reverse, x, y_reverse)[0][0]
        print(naklon_reverse)
        print("Calculated E for reverse is:", '%.3g' %
              int(naklon_reverse**-1), 'N/cm^2')

    plt.title('Raztezek bakrene zice v odvisnosti od sile')
    plt.xlabel(r'$(F −F_o)/S$ $[N/cm^2]$')
    plt.ylabel(r'$\Delta l \: / \: l$')

    plt.grid(True)

    plt.legend()
    plt.savefig('vaja20/raztezek_baker', dpi=300)
    print('saved')
    plt.show()


draw_graph(mase, lege_dodajanje, radij, dolzina,
           lege_odstranjanje=lege_odstranjanje)
