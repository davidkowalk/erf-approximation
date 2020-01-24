from math import e
from math import erf as m_erf

# b ~= 2.4095

def erf(x, b):
    return 2/(1+e**(-b*x**2))-1

def erfinv(y, b):
    # this is a rough approximation of erfinv which diverges
    # from erfinv between -0.02 and +0.02
    # For a similar method refer to “An Ad hoc Approximation to the Gauss Error Function and a Correction Method” by Beong In Yun (Applied Mathematical Sciences, Vol. 8, 2014, no. 86)
    # http://www.m-hikari.com/ams/ams-2014/ams-85-88-2014/yunAMS85-88-2014.pdf
    x = -log(2/(1+y)-1)/b
    return x

def error(min, max):
    pass


def sgn(x):
    if x<0:
        return -1
    else:
        return +1
