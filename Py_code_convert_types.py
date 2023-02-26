# in Python the type is connected to the object, it is not possible to change it
# It is not possible to convert a variable or object from a type to an other
# In Python the conversion doesn't modify the original object but create new objects starting from objects 

mylist = [1, 2, 3, 2, 1] # define a list
myset = set(mylist)  # create a set from the list created
myset #{1, 2, 3}  # unique values, no copies
mylist #[1, 2, 3, 2, 1]  # the list is still here

mystr = '3.14'  # create a string
myfloat = float(mystr)  # transform str in float
myfloat #3.14
mystr  #'3.14'   # mystr is still here

mylist = [('a', 1), ('b', 2), ('c', 3)]   # new list
type(mylist) #<class 'list'>
mydict = dict(mylist)    # create a dictionary from a list
mydict #{'a': 1, 'b': 2, 'c': 3}
type(mydict) #<class 'dict'>

int('un milione')   # the string 'un milione' is not convertible   --> error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: invalid literal for int() with base 10: 'un milione'
int([1, 2, 3])    # list is not a valid type
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'

mylist1 = [1, 2, 3]   # create a list
mylist2 = list(mylist1)    # new list which is a copy of the first list
mylist2 #[1, 2, 3]
mylist1.append(4)  # add one element to mylist1
mylist1 #[1, 2, 3, 4]
mylist2 #[1, 2, 3]    # mylist2 is still the same



