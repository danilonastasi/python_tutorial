# for and while in Python

# print the square of number in the list
seq = [1, 2, 3, 4]   # create a list
for n in seq:
     print('quadrato di', n, '=', n**2)

#quadrato di 1 = 1
#quadrato di 2 = 4
#quadrato di 3 = 9
#quadrato di 4 = 16


# check if numbers in the list are even or odd using for cycle and conditions
seq = [1, 2, 3, 4, 5]
for n in seq:
     print('Il numero', n, '=', end=' ')
     if n % 2 == 0:
         print('pari')
     else:
         print('dispari')

#Il numero 1 = dispari
#Il numero 2 = pari
#Il numero 3 = dispari
#Il numero 4 = pari
#Il numero 5 = dispari


# built-in function range
range(5) #range(0, 5)  # return object with start = o and stop = 5, 5 is not included (0,1,2,3,4)
list(range(5)) #[0, 1, 2, 3, 4]
list(range(5, 10)) #[5, 6, 7, 8, 9]    # 10 is not included
list(range(0, 10, 2))  # [0, 2, 4, 6, 8]   # using the third element we decide the step

for n in range(1, 6):
     print('il quadrato di', n, '=', n**2)
#il quadrato di 1 = 1
#il quadrato di 2 = 4
#il quadrato di 3 = 9
#il quadrato di 4 = 16
#il quadrato di 5 = 25


# let's print 'Python' 3 times
for x in range(3):
     print('Python')
#Python
#Python
#Python



# let's use cycle while

#remove and print nubers from seq until they will be 3 in the list
seq = [10, 20, 30, 40, 50, 60]
while len(seq) > 3:
     print(seq.pop())  # remove elements in seq
#60
#50
#40
seq #[10, 20, 30]   # the new list when len(seq) is not > 3

# ask user to insert numbers until he says the right number
n = 8
while True:   # condition is true and never can be false so we have an endless loop
    guess = int(input('Inserisci un numero da 1 a 10: '))
    if guess == n:
        print('Hai indovinato!')
        break   # interruption of cycle while
    else:
        print('Ritenta sarai piu fortunato')  # restart cycle

#Inserisci un numero da 1 a 10: 3
#Ritenta sarai piu fortunato
#Inserisci un numero da 1 a 10: 8
#Hai indovinato!



# break and continue

seq = ['alpha', 'beta', 'gamma', 'delta']
for elem in seq:
    print('Sto controllando', elem)
    if elem == 'gamma':
       print('Elemento trovato!')
       break   # exit cycle, without checking delta
#Sto controllando alpha
#Sto controllando beta
#Sto controllando gamma
#Elemento trovato!


seq = ['alpha', 'beta', 'gamma', 'delta']
for elem in seq:
     if len(elem) == 5:
         continue    # restart from cycle and next index
     print(elem)   # condition if is not true so print element
#beta


#for-else and while-else
n = 8
for x in range(3):  #3 times (0,1,2)
     guess = int(input('Inserisci un numero da 1 a 10: '))
     if guess == n:
         print('Hai indovinato!')
         break   # exit cycle, end cycle
     # if condition is not true repeat cycle from the next index, second time and third time
else:   # at the end of 3 times print something and exit cycle, end cycle.
     print('Tentativi finiti. Non hai indovinato')
#Inserisci un numero da 1 a 10: 3
#Inserisci un numero da 1 a 10: 2
#Inserisci un numero da 1 a 10: 6
#Tentativi finiti. Non hai indovinato


for x in range(3):
     guess = int(input('Inserisci un numero da 1 a 10: '))
     if guess == n:
         print('Hai indovinato!')
         break
else:
     print('Tentativi finiti. Non hai indovinato')

#Inserisci un numero da 1 a 10: 2
#Inserisci un numero da 1 a 10: 8
#Hai indovinato!






