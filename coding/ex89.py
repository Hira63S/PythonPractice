formatter = "{} {} {} {}" #Python takes the formittor string

car = 'bmw'

#this formatter.format pass to format, four arguments to match up for four {}

print(formatter.format("bmw", "audi", 2 , 3)) # you would alsways needs to have 4 variable
#to replace all four {} in formatter


print(f"love {car}")

one_four = '1, 2, 3, 4'
print(f"{one_four}") #prints out 1,2,3,4

print(formatter.format(1, 2, 3, 4)) # prints out 1 2 3 4. # doesn't print out the commas

print(formatter.format("one", "two", "three", "four")) # this us a way to format without formaing variable first
print(formatter.format(True, False, False, True))

print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


cars_love = "BMW, Audi, Ferrari"
print(f"Some of the Cars Hira Khan loves includes but not limited to: {cars_love}")

print(formatter.format('BMW', 'Audi', "Ferrari", "Lamborghini"))


#EXERCISe 9

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print(months)

print("here are the days: ", days)
print("here are  the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We will be able to type as much as we like.
Even 5 lines if we want, or 5, or 6.
I like ELON MUSK SOOOOO MUCH>
HOPE TO BE LIKE HIM ONE DAY>

""")
