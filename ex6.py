#Says there are 10 types of people by using the d format variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#Says that there are those who know binary and those who don't by using two format variables
y = "Those who know %s and those who %s." %(binary, do_not)

print x 
print y
#This prints I said then the x variable that we defined in the above code
#
print "I said: %r." % x
#This prints I also said then the y variable that we defined in the above code
#
print "I also said: '%s'." % y

#Created a variable hilarious that equals false
hilarious = False
#Creates a variable called joke evaluation that equals isn't that joke funny with the format variable that prints that raw data
joke_evaluation = "Isn't that joke so funny?! %r"

#Prints the joke evaluation variable that we setup above and then we tell it to then print the hilarious variable which equals false by using the format variable
#
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#This prints the above two variables first prints w then adds e to the end completing the sentence.
#
print w + e