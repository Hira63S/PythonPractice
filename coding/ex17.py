from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")
#I am guessing it copes from test.txt or whatever .txt file I create in window powershell
#and then copies that info to another file.

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
#this code retrieve the .txt file as in_file and then indata commands powershell to open the file as in_file


print(f"The input file is {len(indata)} bytes long")
#len(indata) tells the size of the fiel that we created in .txt and then transeferred to indata

print(f"Does the output file exist? {exists(to_file)}")
#what does exists(to_file) Do?

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
#what is input() for here?


out_file = open(to_file, 'w')
out_file.write(indata)
#

print("Alright, all done.")

out_file.close()
in_file.close()

#cat is an old command that concatenates files together, but mostly it's just an easy
# way to print a file to the screen. Type man cat to read about it.
