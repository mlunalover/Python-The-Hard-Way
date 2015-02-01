name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pountds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

test = 10
print "This is a test %r." % test

inches = 13
centimeters = inches * 2.54

print "%r inches equals %r centimeters." % (inches, centimeters)

pounds = 10
kilograms = pounds * 0.4536

print "%r pounds equals %r kilograms." % (pounds, kilograms)


