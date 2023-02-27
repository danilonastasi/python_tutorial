# if-elif-else  -- switch-case

#calcolo il valore assoluto di un numero
n = int(input('Inserisci un numero: ')) #Inserisci un numero: -9
if n < 0:  # condition is true
    n = -n
print('valore assoluto =', n) #valore assoluto = 9

n = int(input('Inserisci un numero: ')) #Inserisci un numero: 3
if n < 0:   # condition is false
    n = -n
print('valore assoluto =', n) #valore assoluto = 3


#let's try using else
n = int(input('Inserisci un numero: ')) #Inserisci un numero: -9
if n < 0:
    print(n, 'negativo')
else:
    print(n, 'positivo')
#-9 negativo

n = int(input('Inserisci un numero: ')) #Inserisci un numero: 6
if n < 0:
    print(n, 'negativo')
else:
    print(n, 'positivo')
#6 positivo


#let's try with elif
n = int(input('Inserisci un numero: ')) #Inserisci un numero: -9
if n < 0:
    print(n, 'negativo')
elif n > 0:
    print(n, 'positivo')
else:
    print(n, 'zero')
#-9 negativo

n = int(input('Inserisci un numero: ')) #Inserisci un numero: 5
if n < 0:
    print(n, 'negativo')
elif n > 0:
    print(n, 'positivo')
else:
    print(n, 'zero')
#5 positivo

n = int(input('Inserisci un numero: ')) #Inserisci un numero: 0
if n < 0:
    print(n, 'negativo')
elif n > 0:
    print(n, 'positivo')
else:
    print(n, 'zero')
#0 zero


# let's try mixing if and else different times
n = int(input('Inserisci un numero: ')) #Inserisci un numero: -9
if n == 0:
    print(n, 'zero')
else:
    if n > 0:
        print(n, 'positivo')
    else:
        print(n, 'negativo')
#-9 negativo

n = int(input('Inserisci un numero: ')) #Inserisci un numero: 5
if n == 0:
    print(n, 'zero')
else:
    if n > 0:
        print(n, 'positivo')
    else:
        print(n, 'negativo')
#5 positivo

n = int(input('Inserisci un numero: ')) #Inserisci un numero: 0
if n == 0:
    print(n, 'zero')
else:
    if n > 0:
        print(n, 'positivo')
    else:
        print(n, 'negativo')
#0 zero


# in Python there is no switch-case condition which is in C:
# let's try switch-case in Python using if, elif, else
n = int(input('Inserisci un numero: ')) #Inserisci un numero: 2
if n == 0:
    print('zero')
elif n == 1 or n == 2:
    print('uno o due')
elif n == 3:
    print('tre')
else:
    print('numero diverso da 0, 1, 2, 3')
#uno o due


#let's try something else using dictionary:
num = int(input('Inserisci un numero: ')) #Inserisci un numero: 8
conv = input('Inserisci tipo di conversione [b/o/x]: ') #Inserisci tipo di conversione [b/o/x]: b
funcs = dict(b=bin, o=oct, x=hex)  # create a dictionary with letter associated to functions
funcs #{'b': <built-in function bin>, 'o': <built-in function oct>, 'x': <built-in function hex>}  # this is the dictionary
if conv in {'b', 'o', 'x'}:   # check if letter is correct for converting
    func = funcs[conv]   # return the value of the dictionary with key conv  #  funcs[conv] will be in this case bin function, we assign it to func
    res = func(num)   # calculate the binary of num
    print('Risultato della conversione =:', res)
else:
    print('Conversione non valida')
#Risultato della conversione =: 0b1000   # number 8 is 1000 in binary sistem, 0b is the prefix
