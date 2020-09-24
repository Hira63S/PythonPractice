###  def cheese_and_crackers(cheese_count, boxes_of_crackers):
#    print(f"cheese_count: {cheese_count}, boxes_of_crackers: {boxes_of_crackers}")

#    cheese_and_crackers = (input("How many cheese do you have"), input ("How many crackers you have?"))

# print(" we can do combine the two, variable and math:")
# cheese_and_crackers(cheese_count, boxes_of_crackers)

###
def cheese_and_crackers(cheese_count, boxes_of_crackers):
         print(f"You have {cheese_count} cheeses!")
         print(f"You have {boxes_of_crackers} boxes of crackers!")
         print("Man that's enough for a party!")
         print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = input("how many cheese you want ")
amount_of_crackers = input("how many crackers u got ")


cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
