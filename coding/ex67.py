types_of_cars = 100
x = f"There are {types_of_cars} unique type of cars that I really like."
#the string is put inside the string

sports = "sports"
regular = "regular"
y = f"Those who are {sports} and those who are {regular} type."
#the string is put inside the string # 2, # 3
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious)) # .format would just put the hilarious value in the place or whatever value the variable in the brackets contain
#it would print "isn't that joke so funny?! False"
#.format(hilarious) is putting the string inside a string so this would be no 4


w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
#ummmm since they are both string. if you put them both together. we get printed them together

print("Mary had a little lamb.")
print("Its fleece was white as {}." .format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #what'd that do? # it prints out two periods

end1 = "C" # there are all variables and when you put them
end2 = "h" #together in a print statement, they are printed out
end3 = "e" #one by one next to each other
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#whats that comma at the end. Try removing it to see what happens

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ') # end = ' ' puts the two words together
# if there is no end = ' ', the word Burger would be printed out in the next line
print(end7 + end8 + end9 + end10 + end11 + end12)

# end = ' ' puts the both print(end1....) line and print(end7...) line togehter and only separates it by spaces
# like Cheese Burger instead of
# Cheese
# Burger
