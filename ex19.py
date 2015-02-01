# this function defines cheese and crackers with cheese cout and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# this line says cheese and crackers values. cheese cout is 20 and boxes of crackers is 30
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this line then tells the script to use the variables 10 and 50 for the amounts
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# this line defines that cheese and crackers also equal amount of cheese and the amount of crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this lin defines that cheese and crackers are both math problems
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this line says cheese and crackers are the amount of cheese and crackers as defined in line
# 14 and 15 plus 100 and plus 1000
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)