cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car.")

name = 'Hira Khan'
age = 18 #not a like
height = 64 #inches
height_in_centimeters = 64*100
weight = 120 #pounds
weight_in_kilograms = 120 / 5

eyes = 'Brown'
teeth = 'White'
hair = 'black'

print(f"Let's talk about {name}.")
print(f"He's {height_in_centimeters} cm tall.")
print(f"he's {weight_in_kilograms} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depdending on the coffee.")

#this line is tricky, try to get it exactly right

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
