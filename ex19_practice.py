def beers(sweet_water_count, eventide_count):
	print "You have %d Sweet Water's." % sweet_water_count
	print "You have %d Eventide's." % eventide_count
	print "Lets have a good time!!\n"
	

print "We can tell the function the exact numbers"
beers(5, 10)

print "We can use variables for our script"
amount_of_sweet = 10
amount_of_even = 12

beers(amount_of_sweet, amount_of_even)

print "We can even do math"
beers(2 + 2, 4 + 2)

print "Lets do more math"
beers(2 * 2, 6 / 2)

beer1 = raw_input("What number is beer 1:\n")
beer2 = raw_input("What number is beer 2:\n")

beers(int(beer1), int(beer2))
