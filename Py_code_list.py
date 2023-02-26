# List in python. It is a changeable sequence of similar objects

nums = [0, 1, 2, 3] # [] create a list
nums #[0, 1, 2, 3]
type(nums) #<class 'list'>
empty = [] #empty list
empty #[]
one = ['Python']
one #['Python']

# indexing and slicing on list
letters = ['a', 'b', 'c', 'd', 'e']
letters[0] #'a'
letters[-1] #'e'
letters[1:4] #['b', 'c', 'd']
'a' in letters #True
letters + ['f', 'g', 'h'] #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
[1, 2, 3] * 3 #[1, 2, 3, 1, 2, 3, 1, 2, 3]

letters = ['a', 'b', 'c', 'b', 'a']
len(letters) #5
min(letters) #'a'
max(letters) #'c'
letters.index('c') #2
letters.count('c') #1
letters.count('b') #2


# keyword del in list and other methods
letters = ['a', 'b', 'c']
letters.append('d')  # add 'd' at the end
letters #['a', 'b', 'c', 'd']
letters.extend(['e', 'f']) # add 'e'and 'f' athe the end as single objects
letters #['a', 'b', 'c', 'd', 'e', 'f']
letters.append(['e', 'f'])  # add a new list ['e', 'f'] at the end
letters #['a', 'b', 'c', 'd', 'e', 'f', ['e', 'f']]
letters.pop() #['e', 'f'] # remove and return the last elements in the list
letters.pop() #'f' # remove and return the last element in the list
letters.pop(0) #'a' # remove and return the element in the position 0
letters.remove('d') # remove element 'd'
letters #['b', 'c', 'e']
letters.reverse()  # invert the order of the elements in the list
letters #['e', 'c', 'b']
letters[1] #'c'  
letters[1] = 'x'  # replace element in the position 1 with 'x'
letters #['e', 'x', 'b']
del letters[1]   # remove element in the position 1
letters #['e', 'b']
letters.clear()  # remove all elements
letters #[]  # empty list


# let's type a list of tuple:
prova = [('John', 'Smith', 20), ('Jane', 'Johnson', 30), ('Jack', 'Williams', 28)]
prova #[('John', 'Smith', 20), ('Jane', 'Johnson', 30), ('Jack', 'Williams', 28)]
type(prova) #<class 'list'>
prova[1] #('Jane', 'Johnson', 30)


