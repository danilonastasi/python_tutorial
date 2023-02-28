# how to manage exception

#error examples
print 'Hello World!'
#  File "<stdin>", line 1
#    print 'Hello World!'
#    ^^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?   # SyntaxError comes when the code is not valid

test
#Traceback (most recent call last):   Traceback tells informations about the sequence of operations
#  File "<stdin>", line 1, in <module>
#NameError: name 'test' is not defined  # NameError describes error

int('five')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: invalid literal for int() with base 10: 'five'

list(5)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'int' object is not iterable

8 / 0
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ZeroDivisionError: division by zero  # gerarchy is ArithmeticError



# example of Traceback with sequence:
def a(x, y):
    return x / y

def b(x, y):
    return a(x, y)

def c(x, y):
    return b(x, y)

c(8, 2) #4.0
c(8, 0)
#Traceback (most recent call last):    # sequence, the most recent call is at the end
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 2, in c
#  File "<stdin>", line 2, in b
#  File "<stdin>", line 2, in a
#ZeroDivisionError: division by zero


# let's manage errors:
try:   # keyword try followed by :
    n = int('five')
except ValueError:  #name of the exception we want to manage
    print('Invalid number!')  # code we want to manage error

#Invalid number!

try:
    n = 5 / 0
except ArithmeticError:
    print('Invalid operation!')

#Invalid operation!


try:
    n = 5 / 0
except ZeroDivisionError as err:   # keyword as followed by variable, in this case err
    print('Invalid operation ({})!'.format(err))  # we print the type of error err (as err)

#Invalid operation (division by zero)!



def try_except_else_test(x):
    try:
       n = int(x) # try to convert x in int
    except ValueError:
       # run in case of ValueError
       print('Invalid number!')
    else:
       # run in case there are no errors
       print('Valid number!')
      
try_except_else_test('five') #Invalid number!
try_except_else_test('5') #Valid number!


# let's try using duble except managing different errors
def try_except_except_test(x):
    try:
       n = int(x) # try to convert x in int
    except ValueError:
       # run in case of ValueError
       print('Invalid number!')
    except TypeError:
       # run in case of TypeError
       print('Invalid type!')
    else:
       # run in case there are no errors
       print('Valid number!')

try_except_except_test('five') #Invalid number!
try_except_except_test([1, 2, 3]) #Invalid type!
try_except_except_test('5') #Valid number!


# using finally
f = open('test.txt', 'w') # open file in writing
try:
    f.read() # try to read but it's failure
finally:
    f.close() # close file despite error

#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#io.UnsupportedOperation: not readable
f.closed  # let's verify that file is closed 
#True

f = open('test.txt')  # re-open the same file in reading (default)
try:
    f.read() # let's try to read the file, now it works
finally:
    f.close()  # file is closed

''
f.closed  # verify if file is closed
#True


#reporting exception   --> raise
try:
    5 / 0
except ZeroDivisionError as err:
    # print information about error
    print('*Logged exception:', err)
    print('*Re-rasing exception.')
    raise  # permits that the original exception can be visible

#*Logged exception: division by zero
#*Re-rasing exception.
#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#ZeroDivisionError: division by zero


try:
    5 / 0
except ZeroDivisionError:
    # capture original error and print a new one
    raise ValueError('Invalid denominator valure!')

#Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#ZeroDivisionError: division by zero

#During handling of the above exception, another exception occurred:

#Traceback (most recent call last):
#  File "<stdin>", line 5, in <module>
#ValueError: Invalid denominator valure!


