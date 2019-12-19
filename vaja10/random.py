from decimal import Decimal
import math
mz = 10**31
ro = 6.3*10**9
vo = 20000
g = 6.67*10**-11


print('%.6E' % Decimal((((mz*g)-math.sqrt(mz**2*g**2 -
                                          (2*mz*g/ro-vo**2)*(ro*vo*1/2)**2))/((ro*vo*1/2)**2))**-1))
