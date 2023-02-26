# Dictionary

# changeable and not ordered eith elements (items) consisting in a key and value. 
# Couples (key and value). Using the key we have the value

# it is possible to define a dictionary using {}

d = {'a': 1, 'b': 2, 'c': 3}  # new dictionary with 3 elements
d #{'a': 1, 'b': 2, 'c': 3}
len(d) #3
d = {'a': 1}
d #{'a': 1}
type(d) #<class 'dict'>
d = {}
d #{}

# most of the times keys are string but

d = {20: ['Jack', 'Jane',], 28: ['John', 'Mary']} # int as keys, list as values
d # {20: ['Jack', 'Jane'], 28: ['John', 'Mary']}
d[20] #['Jack', 'Jane']  #  with this sintax we call the key 20

d = {[0, 10]: 'primo intervallo'}  # return error because list are not hashable. Unchangeable object are normally hashable, list is changeable.
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list'
d = {(0, 10): 'primo intervallo'}  #  tuple are hashable
d #{(0, 10): 'primo intervallo'}


d = {'a': 1, 'b': 2, 'c': 3}
d['a'] #1
d['c'] #3
d['f']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'f'
'f' in d #False
'f' not in d #True
'b' in d #True
d['b'] #2


# methods in dictionary:
d = {'a': 1, 'b': 2, 'c': 3}
len(d) #3
d.items() #dict_items([('a', 1), ('b', 2), ('c', 3)]) # showing elements (keys and values)
d.keys() #dict_keys(['a', 'b', 'c'])  # showing keys
d.values() #dict_values([1, 2, 3])  # showing values
d.get('c', 0) #3  # return values in c
d.get('x', 0) #0  # return default 0 because the key x is not in d
d #{'a': 1, 'b': 2, 'c': 3}
d.pop('a', 0) #1   # return values in a but remove it form the dictionary
d #{'b': 2, 'c': 3}
d.pop('x', 0) #0  # return default 0 because x is not in d
d.pop('x')  # return error because we don't have x and tehre is no default value
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'x'
d.popitem() #('c', 3)  # return a value and remove the element, casually
d #{'b': 2}
d.update({'a': 1, 'c': 3}) # add new elements
d #{'b': 2, 'a': 1, 'c': 3}
d.clear()  # remove all elements
d #{}






