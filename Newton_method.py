
from __future__ import division

def Newton_method(x_0,epi):
    f_1 = 2*x_0 -54/(x_0**2)
    f_2 = 2 + 108/(x_0**3)
    x_1 = x_0 - f_1/f_2
    if (x_1-x_0) < epi:
        return x_1
    else:
        return Newton_method(x_1,epi)


print Newton_method(2,10**-5)        
    
