cars = 100
#4.0 is needed since it is a floating point number. A floating point number is a number with a decimal point. 4 is not a floating point number
space_in_a_car = 4.0
drivers = 30
passengers = 90
#Takes the number of cars and subtracts the number of drivers
cars_not_driven = cars - drivers
#Makes a variable that says cars_driven is equal to drivers
cars_driven = drivers
#Makes a variable that takes cars driven and multiples that by the space in the car
carpool_capacity = cars_driven * space_in_a_car
#Takes the passengers and divides it by the cars driven.
#It would give that error if the car pool capacity variable had not yet been setup in a previous line 7.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

cats = 3
dogs = 1
beds = 2
couchs = 1

print "There are" , beds, "beds available."
print "There are" , cats + dogs, "animals in the house."
print "There are" , couchs, "couchs available."

print "Hey %s there." % "you"