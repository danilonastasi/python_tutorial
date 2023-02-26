# not just list, tuple, dictionary. We have also set and frozenset
# Set are used to represent the set (insieme) not ordered of unique objects
# This sequence is changeable in set and unchangeable in frozenset

# to determinate a set or frozenset we use {} like in dictionary
# to create an empty set or frozenset we don't use {} but ()

nums = {10, 20, 30, 40}
nums #{40, 10, 20, 30}
type(nums) #<class 'set'>
fnums = frozenset(nums)  # new frozenset starting form set nums
fnums #frozenset({40, 10, 20, 30})
type(fnums) #<class 'frozenset'>
{'Python'} #{'Python'}  # set for 1 element string
empty = set()  # new empty set
empty #set()
type(empty) #<class 'set'>
type({}) #<class 'dict'>  # create a dictionary empty
type(set()) #<class 'set'>  # create a set empty
type(frozenset()) #<class 'frozenset'>  # create a frozenset empty


{1, 2, 3, 2, 1} #{1, 2, 3}  #  in set and frozenset elements have to be unique
set('abracadabra') #{'a', 'b', 'r', 'd', 'c'}   # remove copies
frozenset('abracadabra') #frozenset({'a', 'b', 'r', 'd', 'c'})
{'a', 1, (3, 14)}  #{1, (3, 14), 'a'}  # la tuple e' hashable, unchangeable
{'a', 1, (3, 14), [3, 2, 1]}   # error because list is not hashable, list is changeable
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: unhashable type: 'list'


nums = {10, 20, 30, 40}
len(nums) #4
min(nums) #10
max(nums) #40
10 in nums #True
50 not in nums #True
60 in nums #False


#methods
nums.add(50)   # add 50 to the set
nums #{40, 10, 50, 20, 30}
nums.remove(10)  # remove 1o from the set
nums #{40, 50, 20, 30}
nums.remove(10)  # error because 10 is missing
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 10
nums.discard(20)   # remove 20 frome the set
nums #{40, 50, 30}
nums.discard(20) # 20 is missing but not error
nums.pop() #40   return an element which is removed from the set
nums #{50, 30}
nums.clear()   # remove all elements
nums #set()


# typical set(insiemi) operation
{1, 2, 3}.isdisjoint({4, 5, 6}) #True  #are them disjoint? Not common elements?
{1, 2, 3}.isdisjoint({3, 4, 5}) #False  # 3 is in common
{2, 4} <= {1, 2, 3, 4} #True  # the first set is (sottinsieme) of the second set
{2, 4} < {1, 2, 3, 4} #True   # the first is (sottinsieme proprio)
{1, 2, 3} >= {1, 2, 3} #True #  the second set is (sottinsieme) of first set
{1, 2, 3} > {1, 2, 3} #False  # but it is not (sottinsieme proprio)
{1, 2, 3} | {2, 3, 4} | {3, 4, 5} #{1, 2, 3, 4, 5}   # union of all elements
{1, 2, 3} & {2, 3, 4} & {3, 4, 5} #{3}    # intersection of all elements (common)
{1, 2, 3, 4, 5} - {1, 2} - {2, 3} #{4, 5}    # difference
{1, 2, 3, 4} ^ {3, 4, 5, 6} #{1, 2, 5, 6}    # not common elements
s1 = {1, 2, 3}
s1 |= {2, 3, 4} | {3, 4, 5}   # add on s1 the other elements, rejecting copies because set in unique
s1 #{1, 2, 3, 4, 5}



