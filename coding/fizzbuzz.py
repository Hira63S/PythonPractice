#write program that prints numbers from 1 to 20 but for ...

#Method 1: Concatenating Strings

for num in range(1, 21):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)

    print(string)


#Method 2:


for num in range(1, 21):

    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num %3 != 0:
        string = string + str(num)
    print(string, end = ' ')
