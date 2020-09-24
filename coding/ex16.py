from sys import argv

script, filename = argv

# run the file like 'python ex16.py test.txt' and then it will ask that we are going to erase the filename
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-c (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
#then it opens the file and

print("Truncating the file. Goodbye!")
target.truncate()
#then it shows the prompt that it is truncating the file;

print("Now I'm going to ask you for three lines.")

#asks you to enter three lines

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("opening the file...")
target = open(filename, 'w')


print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


target = open(filename, 'w')


print("And finally, we close it.")
target.close()

#I think
