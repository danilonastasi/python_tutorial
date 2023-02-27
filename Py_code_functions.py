# functions in Python

def is_even(n):
    if n%2 == 0:
        return True
        else:
        return False
is_even(4) #True   # call the function passing 4
is_even(5) #False


#docstring """..."""
def is_even(n):
    """Return True if n is even, False otherwise. """ #first row inside a function, description
    if n%2 == 0:
         return True
    else:
         return False

is_even(3) #False

help(is_even)   # we can see the first instruction as a docstring
#Help on function is_even in module __main__:

#is_even(n)
#    Return True if n is even, False otherwise.


# arguments we can pass to the function can be 0 or more
# we can pass them for position or name

def calc_rect_area(width, height):
     """Return the area of the rectangle."""
     return width * height

calc_rect_area(3, 5) #15   # position call
calc_rect_area(width=3, height=5) #15  # name call
calc_rect_area(height=5, width=3) #15
calc_rect_area(3, height=5) #15


#let's see more
size = (3, 5)  # tuple
calc_rect_area(*size) #15

size = {'width': 3, 'height': 5}  # dictionary
calc_rect_area(**size) #15



# definition of parameters in the functions:
def say_hello():
     print('Hello World!')
say_hello() #Hello World!

def say_hello(name):
     print('Hello {}!'.format(name))
say_hello()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: say_hello() missing 1 required positional argument: 'name'
say_hello('Python') #Hello Python!
say_hello(name='Python') #Hello Python!

def say_hello(name='World'):
     print('Hello {}!'.format(name))
say_hello() #Hello World!
say_hello('Python') #Hello Python!
say_hello(name='Python') #Hello Python!





