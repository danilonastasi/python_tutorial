# function built-in open()
# open file returning a file object. The file object permits to run different operation in the file, resading, writing

# the function opend() accepts different arguments, the most important are name of the file to open and how to open it

open('test02.txt')   # file doesn't exist so we have error, default is reading
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#FileNotFoundError: [Errno 2] No such file or directory: 'test02.txt'

open('test02.txt', 'w')  # opening in writing the file is created
#<_io.TextIOWrapper name='test02.txt' mode='w' encoding='cp1252'>

open('test02.txt', 'r')  # opening in reading the file is read now
#<_io.TextIOWrapper name='test02.txt' mode='r' encoding='cp1252'>

open('test02.txt')  # default is reading, now it works because the file was created
#<_io.TextIOWrapper name='test02.txt' mode='r' encoding='cp1252'>


# file object
f = open('test.txt', 'w') # open the file in writing
f
#<_io.TextIOWrapper name='test.txt' mode='w' encoding='cp1252'>
dir(f)
#['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', 
#'__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', 
#'__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
#'__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 
#'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 
#'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 
#'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
f.name  # attribute .name correspond to name of file
#'test.txt'
f.mode # attribute .mode correspond to modality open
#'w'
f.closed # attribute .closed is True if the file is closed otherwise false
#False
f.read # read is a method that if called read and return the contents
#<built-in method read of _io.TextIOWrapper object at 0x0000023BC8F14A00>
f.write  # write is a method that if called consent to write in the file
#<built-in method write of _io.TextIOWrapper object at 0x0000023BC8F14A00>
f.close # close is a method that if called close the file
#<built-in method close of _io.TextIOWrapper object at 0x0000023BC8F14A00>


# some examples
f = open('test.txt', 'w')  # opening in writing
f.write('prima riga del file\n')  # let's write a row in the file
#20
f.write('seconda riga del file\n')  # let's write an other row in the file
#22
f.close() # let's close the file

f = open('test.txt')  # re-open in reading
content = f.read()  # reading all content in the file
print(content)
#prima riga del file
#seconda riga del file

f.close()  # closing file



# creating a list of rows
lines = [
    'prima riga del file\n',
    'seconda riga del file\n',
    'terza riga del file\n'
    ]
lines
#['prima riga del file\n', 'seconda riga del file\n', 'terza riga del file\n']
type(lines)
#<class 'list'>
f = open('test.txt', 'w')
f.writelines(lines) # we use method writelines to write rows in the file
f.close()

f = open('test.txt') # open in reading
f.readlines()  # method readlines to get the list
#['prima riga del file\n', 'seconda riga del file\n', 'terza riga del file\n']
f.close()

f = open('test.txt') # re-open in reading
f.readline() # we use the method readline to get a single row
#'prima riga del file\n'
f.readline() # we use the method readline to get an other single row
#'seconda riga del file\n'
f.readline() # we use the method readline to get an other single row
#'terza riga del file\n'
f.close()

# it is possible to use for:
f = open('test.txt')
for line in f:  #iteriamo on rows of the file
    line
#'prima riga del file\n'
#'seconda riga del file\n'
#'terza riga del file\n'
f.close()


# it is possible to use metodifile.tell() and file.seek() to verify and modify the position memorized from the file object
lines = [
    'prima riga del file\n',
    'seconda riga del file\n',
    'terza riga del file\n'
    ]
f = open('test.txt', 'w')
f.writelines(lines)
f.seek(0, 0)  # we run a seek to move at hte beginning of the file, the second argument 0 indicate the beginning
#0
f.write('PRIMA')  # we write PRIMA to the beginning of the file overwriting prima
#5
f.seek(0, 2) # we move to the end of file, 2 indicate the end
#65
f.write('quarta riga del file\n')  # we add a row to the end
#21
f.close()

f = open('test.txt')
f.readline()
#'PRIMA riga del file\n'
f.readline()
#'seconda riga del file\n'
f.tell() # we see that position in the file moved ahead
#44
f.read()  # we read the rest of rows
#'terza riga del file\nquarta riga del file\n'
f.tell()
#87
# the position moved ahead
f.read()  # after reading all it returns empty string
#''
f.seek(0)  # we move at the beginnig
#0
f.tell()  # position now is 0
#0
f.readlines()
#['PRIMA riga del file\n', 'seconda riga del file\n', 'terza riga del file\n', 'quarta riga del file\n']
f.close()



#constructor with
# we use it to close everytime the file object automatically, especially in case of error and interruption
f = open('test.txt', 'w')
with f:  # we use the file object as context manager in with
    f.write('contenuto del file')  # writing the file
    f.closed  # verify if the file is still open

#18
#False
f.closed  # verify if after with the file is closed
#True


# we do the same here:
with open('test.txt', 'w') as f:
    f.write('contenuto del file')

#18
f.closed
#True

