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


# using * in argument:
def greet(greeting, *,name):  # all arguments appear after * have to be passed by name
    print('{} {}!'.format(greeting, name))

greet('Hello', 'Python')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: greet() takes 1 positional argument but 2 were given

greet('Hello', name='Python') #Hello Python!
greet(greeting='Hello', name='Python') # Hello Python!

def say_hello(*names):   # * before argument permits funciotn to accept different numbers of arguments.
                         # After call the variable names will be like a tuple with all arguments.
    print('Hello {}!'.format(' '.join(names)))

say_hello('Python') #Hello Python!
say_hello('Python', 'PyPy', 'Jython', 'IronPython') 
#Hello Python PyPy Jython IronPython!



def make_tag(element, **attrs):  #  adding **before the variable it accepts different number of variables passed by name (keyword argument)
                                 #  Function accept an argument element and different arguments in attrs saved as a dictionary.
    attrs = ' '.join(['{}"{}"'.format(k, v) for k, v in attrs.items()])  # create a string combining names of attributes and values in combination with element.
    return '<{} {}>'.format(element, attrs)

make_tag('div', id='header') 
#'<div id"header">'
make_tag('a', href='https://www.python.org/', title='Visit {Python.org')
#'<a href"https://www.python.org/" title"Visit {Python.org">'
make_tag('img', src='logo.png', alt='Python logo')
# '<img src"logo.png" alt"Python logo">'


# reteurn of values
# return is used to give back a value. It is possible to assign to an other variable or use it.
def square(n):
    return n**2
x = square(5)   # assignment
x #25
square(square(5)) #625  # operation in the same function
square(3) + square(4) == square(5) #True

def abs(n):
    if n < 0:
       return -n   # first return, after return function stops
       return n
abs(-5) #5  # first return
abs(5)  # no result, condition is not true 5 is not < 0



def print_twice(text):
    if not text:
       return
    print(text)
    print(text)
res = print_twice('Python')   # text is text so the result is print print
#Python
#Python
type(res) #<class 'NoneType'>
print(res) #None  # return none automatically at the end of the print print , at the end of function
res = print_twice('')  #argument is empty, not text --> return none and exit from function
print(res) #None



# if we want more values as return
def midpoint(x1, y1, x2, y2):
    """Return the midpoint between (x1; y1) and (x2; yw)."""
    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2
    return xm, ym   # return more values
x, y = midpoint(2, 4, 8, 12)
x #5.0
y #8.0



# scope of variable
# we can't use variables of the function but function can use variable outside function
def calc_circle_area(r):
   pi = 3.14
   return pi * r**2
calc_circle_area(5) # 78.5
r # return error because r is in function
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'r' is not defined
pi # the same error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'pi' is not defined

pi = 3.14   # assignment aoutside function
def calc_circle_area(r):
    return pi * r**2
calc_circle_area(5) #78.5


lista = [1, 2, 3, 4, 5]   # create a list outside function
def add_elem(seq, elem):
    seq.append(elem)
lista #[1, 2, 3, 4, 5]  
add_elem(lista, 6)  # add the number 6 to the list
lista #[1, 2, 3, 4, 5, 6]









