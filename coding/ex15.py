from sys import argv

script, filename = argv


#run it so you write python ex13.py filename
#opens the file! when i type ex15_sample.txt on the first prompt

# run it like python ex15.py ex15_sample.txt
# and only then will it run it


txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

#this one reopens the file. You can do it either way! Remove the code from
#below this comment and the code above this comment would prompt you to type file user_name
# you can also remove the code from above this comment and the code below this comment would prompt you to
#type the file name. But it would include "again"

print("Type the filename again:")

#this asks you to type the file user_name
#unlike the first half of this exercise which asks you to type:
# python .\ex15.py ex15_sample.txt_again
#running just this code prompts you to type the file user_name
#maybe you could bring out another file this way???


file_again = input ("> ")

txt_again = open(file_again)

print(txt_again.read())

#it closes the file after you enter the file name ex115_sample.txt again. automatically!! YYAYYYYYAYY

txt.close()
