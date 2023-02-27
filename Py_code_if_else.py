# if-elif-else

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


