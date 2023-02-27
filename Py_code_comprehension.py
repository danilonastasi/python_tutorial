# list, set, dict comprehension

# list comprehension:
[x**2 for x in range(10)] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# set comprehension:
{x**3 for x in range(10)} #{0, 1, 64, 512, 8, 343, 216, 729, 27, 125}

# dict comprehension
{c: c.upper() for c in 'abcde'} #{'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'}

squares = [x**2 for x in range(10)]
squares #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# the same here:
squares = []  # empty list
for x in range(10):
    squares.append(x**2)   # add calculating square for 10 times
squares #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# listcomp that filter numbers gettin only even
[x for x in range(10) if x%2 == 0] #[0, 2, 4, 6, 8]

# setcomp that filter letters getting only uppercase
{c for c in 'aAbBcCdDeE' if c.isupper()} #{'B', 'C', 'E', 'A', 'D'}

# listcomp that create all combinations between ABC and 123
[c+n for c in 'ABC' for n in '123'] #['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']


# the list comprehension:
even = [x for x in range(10) if x%2 == 0]
even #[0, 2, 4, 6, 8]

#is equal to:
even = []
for x in range(10):
    if x%2 == 0:
        even.append(x)
even #[0, 2, 4, 6, 8]


# The list comprehension:
combs = [c+n for c in 'ABC' for n in '123']
combs # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

# is equal to:
combs = []
for c in 'ABC':
    for n in '123':
        combs.append(c+n)
combs # ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']



# map and filter, built-in functions

# definition of a function which return square of a number
def square(n):
    return n**2   # return square of n
squares = map(square, range(10))  # map applies the function square to all values in range
squares #<map object at 0x0000020E48A3B9A0>  # return a iterabile object
type(squares) #<class 'map'>
list(squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  # converting in list we get values

[square(x) for x in range(10)] #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  # same result with listcomp

# definition of a function that return True if number is even
def is_even(n):
    if n%2 == 0:
       return True
    else:
       return False
even = filter(is_even, range(10))   # filter returns an iterabile that include all elements of range where is_even(element) is true.
even #<filter object at 0x0000020E48A396F0>  # return an iterabile object
list(even) #[0, 2, 4, 6, 8]  # converting in list we get values

[x for x in range(10) if is_even(x)] #[0, 2, 4, 6, 8]  # same result with listcomp

