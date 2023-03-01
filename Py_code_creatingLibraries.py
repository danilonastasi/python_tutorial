# ho w to create new libraries

#let's create a text file like this and then rename it aritmetica.py saving it in the directory lib of Python

# aritmetica.py
def add(a, b):
   return a + b
def sub(a, b):
   return a - b
def mul(a, b):
   return a * b
def div(a, b):
   return a / b
  
import #aritmetica
aritmetica
#<module 'aritmetica' from 'C:\\Users\\danil\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\aritmetica.py'>
aritmetica.add
#<function add at 0x000002DCB32B8720>
aritmetica.add(3, 5)
#8
aritmetica.mul
#<function mul at 0x000002DCB32B8860>
aritmetica.mul(3, 5)
#15
#  running aritmetica.py as exe we have nothing

#let's extent the code in the library with:
if __name__ == '__main__':
   import sys # import library sys from standard library
   ops = dict(add=add, sub=sub, mul=mul, div=div) # create a dictionary
   choice = input("Seleziona un'operazione [add/sub/mul/div]: ")
   if choice not in ops:
      sys.exit('Operazione non valida!') # stop programm with a error message
   op = ops[choice]  # assign op the function chosen by user
   try:
      a = float(input('Inserisci il primo valore: ')) convert value in float
      b = float(input('Inserisci il secondo valore '))
   except ValueError as err:  # if convert doesn't work stop programm with error
      sys.exit('Valore non valido: {}'.format(err))
   print('Il risultato è:', op(a, b))
  
  # with the row if __name__ == '__main__': it is possible to run this programm (aritmetica.py) directly as exe
  
  # if we import the module, __name__ valure will be not '_main__', will be 'aritmetica', programm will not work as exe
  # it is possible to have file that work if exe or import as library
  
  
  
  
  
  
