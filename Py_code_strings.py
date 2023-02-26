# strings in Python

# string is a sequence

# indexing and slicing
s = 'Python'
s # 'Python'
s[0] # 'P'
s[5] # 'n'
s[-1] # 'n'
s[-4] # 't'

s[0:2] # 'Py'
s[:2] # 'Py'
s[3:5] # 'ho'
s[4:] # 'on'
s[-2] # 'o'
s[-2:] # 'on'

# contenimento
'P' in s # True
'x' in s # False
'x' not in s # True
'Py' in s # True
'py' in s # False # because Pythons is a case-sensitive language

# concatenamento, ripetizione e lunghezza
'Py' + 'thon' #'Python'
'Py'*2 #'PyPy'
'Ba' + 'na'*2 #'Banana'

len('Python') # 6
s = 'Precipitevolissimevolmente'
len(s) # 26

#functions and methods
