import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

data = [0.109768, 0.109858, 0.110012, 0.110057, 0.110107, 0.11016, 0.110201, 0.110284, 0.110305, 0.110307, 0.110311, 0.110344, 0.110405, 0.110415, 0.110435, 0.110457, 0.110489, 0.110515, 0.110576, 0.110616, 0.110624, 0.110638, 0.110689, 0.110728, 0.110731, 0.110781, 0.110813, 0.110818,
        0.110824, 0.110867, 0.110871, 0.110881, 0.110897, 0.110979, 0.11098, 0.111004, 0.111016, 0.111022, 0.111063, 0.111079, 0.111102, 0.111123, 0.111124, 0.11118, 0.111206, 0.11124, 0.111259, 0.111292, 0.111456, 0.111592, 0.111695, 0.111728, 0.111844, 0.111956, 0.112509, 0.112739]

s = 0.2226
d = 0.0152
h = 0.0994

r = 0.0151/2

h = h
s = s-r

bins = int((len(data))**0.5)

res = stats.cumfreq(data, numbins=bins)

x = res.lowerlimit + \
    np.linspace(0, res.binsize*res.cumcount.size, res.cumcount.size)

mean, std = stats.norm.fit(data)

fig = plt.figure(figsize=(6, 4))
ax1 = fig.add_subplot(1, 1, 1)

ax1.hist(data, bins=bins, density=True)

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = stats.norm.pdf(x, mean, std)
ax1.plot(x, y)
ax1.set_xlabel('čas [s]')
ax1.set_ylabel(r'gostota verjetnosti [$s^{-1}$]')
ax1.set_title('Histogram')


t = mean


def rac_g(t, h, s):
    print(t, h, s)
    return ((((-(2*h)**0.5) + (2*h+2*s)**0.5) / t)**2)


g = rac_g(t, h, s)

print(g)

plt.show()
