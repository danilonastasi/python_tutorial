# how to import libraries

import math
math
<module 'math' (built-in)>
help(math)
#Help on built-in module math:

#NAME
#    math

#DESCRIPTION
#    This module provides access to the mathematical functions
#    defined by the C standard.

#FUNCTIONS
#    acos(x, /)
#        Return the arc cosine (measured in radians) of x.

#        The result is between 0 and pi.

#    acosh(x, /)
#        Return the inverse hyperbolic cosine of x.

#    asin(x, /)
#        Return the arc sine (measured in radians) of x.

#        The result is between -pi/2 and pi/2.
# etc..

dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 
 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 
 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 
 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 
 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 
 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 
 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

math.pi
#3.141592653589793
math.sqrt
#<built-in function sqrt>
help(math.sqrt)
#Help on built-in function sqrt in module math:

#sqrt(x, /)
#    Return the square root of x.

math.sqrt(64)
#8.0


#it is possible to import the function from math and not to use math.
from math import pi, sqrt
pi
#3.141592653589793
sqrt(64)
#8.0


#it is also possible to change the name math or the name of functions
import math as matematica
matematica.pi
#3.141592653589793

from math import sqrt as radice_quadrata
radice_quadrata(64)
#8.0


#let's import all names from the library
from math import *
pi
#3.141592653589793
e
#2.718281828459045
sqrt
#<built-in function sqrt>
sin
#<built-in function sin>
cos
#<built-in function cos>
tan
#<built-in function tan>









