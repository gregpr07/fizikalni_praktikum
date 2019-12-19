from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt
import numpy as np


g = 9.81

# m
r1 = 5.97/2/100
r2 = 6.75/2/100
h = 2.6/100

# v g
mase = [10, 20, 30, 40, 50]

# m
radijg = 5.33/2/100

# rad/s^2
kotni_pospesek = [8.935, 17.51, 27.32, 34.83, 44.520]

# navor
y = [y/1000*g*radijg for y in mase]

# alfa
x = kotni_pospesek


def fit_func(x, a, b):
    return a*x+b


params = curve_fit(fit_func, x, y)

err = (-params[1][1][0])**(1/2)

print(params)

print("J (Vztrajnostni moment) je:", '%.3g' %
      params[0][0], 'kgm^2', '+/-', '%.3g' % err, 'kgm^2')

x_fit = np.linspace(0, x[-1]+10, 100)

y_fit = fit_func(x_fit, params[0][0], params[0][1])

# equations

omege = [3.26, 6.48, 7.587, 11.78, 13.65]

mtr = params[0][1]


def ni(mtr, mg, r1, r2, omega, h):
    return ((mtr-mg)*(r1**2-r2**2), (4*math.pi*omega*h*r1**2*r2**2))


def ni1(mtr, mg, r1, r2, omega, h):
    return (mg/omega/(4*math.pi*h*r1**2*r2**2/(r2**2-r1**2)))


#####
plt.plot(x, y, 'o', label='Padanje uteži')
plt.xlim([0, x[-1]+x[-1]*0.1])
plt.ylim([0, y[-1]+y[-1]*0.1])

plt.plot(x_fit, y_fit, label=r'J')
#plt.errorbar(x, y, xerr=napake_x, yerr=napake_y, fmt='none')

plt.title(f'Inverz kotnega pospeška v odvisnosti od mase padajoče uteži')
plt.xlabel(r'$\alpha$ [$rad/s^2$]')
plt.ylabel(r'$M_g$ [$Nm$]')

plt.grid(True)


plt.legend()
plt.savefig(f'./J', dpi=300)
# print('saved')

plt.show()

# nigraf
nix = []
niy = []

for (om, mg) in zip(omege, y):
    x, y = ni(mtr, mg, r1, r2, om, h)
    nix.append(y)
    niy.append(x)
    print(x, y)


params = curve_fit(fit_func, nix, niy)

print(params[1][0][0])

err = (params[1][0][0])**(1/2)

print(params)


print("Ni je:", '%.3g' %
      params[0][0], 'enota', '+/-', '%.3g' % err, 'enota')

plt.plot(nix, niy, 'o', label='Točke')


x_fit = np.linspace(0, nix[-1]+nix[-1]*0.1, 100)

y_fit = fit_func(x_fit, params[0][0], params[0][1])

plt.plot(x_fit, y_fit, label=r'Fit')

plt.title(r'Graf končnega $\eta$')
plt.xlabel(r'$4 \pi \omega h r_1^2 r_2^2$')
plt.ylabel(r'$(M_{tr} - M_g)(r_1^2-r_2^2)$')

plt.grid(True)


plt.legend()
# print('saved')


plt.show()
