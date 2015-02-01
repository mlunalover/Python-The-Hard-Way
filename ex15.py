#Says hey I want to use the from and import module argument
from sys import argv

#Using script name (ex15.py) then the filename (ex15_sample) complete the argument and allow it to be read.
script, filename = argv

#Says hey file the text document requested in the above argument.
txt = open(filename)

#Says hey print the sentence and use the filename requested at the launch of the argument. Then reads the file.
print "Here's your file %r:" % filename
print txt.read()

#Prints the sentence asking what the filename is then puts the filename in a variable called file_again.
print "Type the filename again:"
file_again = raw_input("> ")

#Takes the filename put into the variable called file_again and opens it.
txt_again = open(file_again)

print txt_again.read()