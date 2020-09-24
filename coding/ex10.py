tabby_cat = "\tI'm tabbbed in." # i am tabbed in meaning the variable will print after a tab.
#like this:
#       I'm tabbed in
persian_cat = "I'm spilt\non a line." #This prints:
#I'm split
#on a line
backlash_cat = "I'm \\ a \\ cat."
# This doesn't have an affect. it prints: "I'm \ a \ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#the first line after \t prints * Cat food
#The second line prints * Fishes and so on. all the lines are on a new lines


print(tabby_cat)
print(persian_cat)
print(backlash_cat)

print(fat_cat)

print("How old are you?", end = ' ')
age = input(38) # after this you would have to press enter again for the
#python to print the next lines of How old are you? and since there is no input
# after that line in the follow lines, both lines "how old are you? and How much do
#you weight" will be printed on the same lines

#Exercise 11

print("how old are you?", end= ' ')
age = input()
print("how tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} years old, {height} inches tall, {weight} pounds")
