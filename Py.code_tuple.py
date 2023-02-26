# tuple - rappresenting unchangeable sequence of objects, different eachother

t = 'abc', 123, 45.67 # we have here string, integer, float # comma creates tuple
t # ('abc', 123, 45.67)
type(t) # <class 'tuple'>
tp = ('abc', 123, 45.67) # it is always better to use brackets ()
t == tp #True
len((1, 'a', 2.3)) #3 double brackets

len(1, 'a', 2.3) # one brackets, error
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: len() takes exactly one argument (3 given)

t = 'abc'
t #'abc'
tv = () # empty tuple
tv #()
type(tv) #<class 'tuple'>
len(tv) #0



#indexing, slicing, contenimento, concatenamento, ripetizione

t = ('abc', 123, 45.67)
t[0] #'abc'
t[:2] #('abc', 123)
123 in t #True
t + ('xyz', 890) #('abc', 123, 45.67, 'xyz', 890)
t*2 #('abc', 123, 45.67, 'abc', 123, 45.67)

# tuple are unchangeable, it will be not possible to add or remove or modify objects
t[0] = 'xyz'
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

len(('abc', 123, 45.67, 'xyz', 890)) #5
min((4, 1, 7, 5)) #1
max((4, 1, 7, 5)) #7
t = ('a', 'b', 'c', 'b', 'a')
t.index('c') #2 # index starts from 0
t.count('c') #1
t.count('b') #2 # number of times we have 'b'

