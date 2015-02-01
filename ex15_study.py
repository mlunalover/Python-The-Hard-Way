from sys import argv

script, filename = argv

txt = open(filename)

print "This is your file %r:" % filename
print txt.read()