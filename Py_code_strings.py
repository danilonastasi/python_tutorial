# strings in Python

# string is a sequence

# indexing and slicing
s = 'Python'
s # 'Python'
s[0] # 'P'
s[5] # 'n'
s[-1] # 'n'
s[-4] # 't'

s[0:2] # 'Py'
s[:2] # 'Py'
s[3:5] # 'ho'
s[4:] # 'on'
s[-2] # 'o'
s[-2:] # 'on'

# contenimento
'P' in s # True
'x' in s # False
'x' not in s # True
'Py' in s # True
'py' in s # False # because Pythons is a case-sensitive language

# concatenamento, ripetizione e lunghezza
'Py' + 'thon' #'Python'
'Py'*2 #'PyPy'
'Ba' + 'na'*2 #'Banana'

len('Python') # 6
s = 'Precipitevolissimevolmente'
len(s) # 26



#functions
len('Python') # 6 # 'Python' is the argument
len(['PyPy', 'Jython', 'IronPython']) # 3 # list
len({'a':3, 'b':5}) # 2 # dictionary



# methods
# similar to functions but connected with the type of object
s='Python' # assignment
s.upper() # 'PYTHON' # uppercase
s.lower() #'python' # lowercase

len # <built-in function len>
help(len) # description len
# Help on built-in function len in module builtins:
# len(obj, /)
#    Return the number of items in a container.

dir(str) # list methods and attributes of str:
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
# 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
# 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

str.upper # <method 'upper' of 'str' objects>
help(str.upper) # description of this method
# Help on method_descriptor:

# upper(self, /)
#    Return a copy of the string converted to uppercase.

help(str.replace) # description of this method
# Help on method_descriptor:

# replace(self, old, new, count=-1, /)
#    Return a copy with all occurrences of substring old replaced by new.

#      count
#        Maximum number of occurrences to replace.
#        -1 (the default value) means replace all occurrences.

#    If the optional argument count is given, only the first count occurrences are
#    replaced.

'Python'.replace('thon','Py') #'PyPy' # replace 'thon' with 'Py' #'PyPy'
s='Python, Python, Python!'
s.replace('thon', 'Py', 2)

type(s) # <class 'str'>
s.replace('thon', 'Py', 2) # 'PyPy, PyPy, Python!' # 2 replacement



#formatting strings
str.format # <method 'format' of 'str' objects>

raggio =8.4
area = 3.14*raggio**2
circ = 2*3.14*raggio
s = "L'area e' {}, la circonferenza e' {}." # two placeholder {} {}
s.format(area,circ) # "L'area e' 221.5584, la circonferenza e' 52.752." # arguments are area and circ

help(str.format)
#Help on method_descriptor:

#format(...)
#    S.format(*args, **kwargs) -> str

#    Return a formatted version of S, using substitutions from args and kwargs.
#    The substitutions are identified by braces ('{' and '}').




