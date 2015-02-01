# this line adds the argument module so to run the script we also have to list the file to run with
from sys import argv

# this line defines the argument and lists the file variable name of input_file
script, input_file = argv

# this line is a function that prints the txt file
def print_all(f):
	print f.read()

# this line rewinds back to the beginning of the file after we just read it
def rewind(f):
	f.seek(0)

# this line is a function that defines print a line with line count and which line to read
def print_a_line(line_count, f):
	print line_count, f.readline()

# this line is a variable called current file opens our input file which is test.txt
current_file = open(input_file)

print "First let's print the whole file:\n"

# this line prints the current file which is our txt file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# this line calls the function rewind which starts the file back at the beginning
rewind(current_file)

print "Let's print three lines:"

# this line calls the function which prints the current line which is 1
current_line = 1
print_a_line(current_line, current_file)

# this line calls the function which print the file line which is 2 now since 1 + 1 is 2
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# this line calls the function which prints the file line which is 3 since 1 + 2 is 3
#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)