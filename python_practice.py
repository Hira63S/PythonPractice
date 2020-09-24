''' Print out all of the strings in the following array in alphabetical order, each on a separate line.
['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
The expected output is:
'Cha Cha'
'Foxtrot'
'Jive'
'Paso Doble'
'Rumba'
'Samba'
'Tango'
'Viennese Waltz'
'Waltz'
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
'''

words = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
words_1 = ['W', 'T', 'V', 'F', 'C', 'S']
words.sort

print(words)

'''
Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line.
If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.

'''
# slice the strings:
# len(i) // 2 would give is the middle character
for i in words:
    mid = len(i) // 2
    

#print(words)
# sorted = words.sort()
# words_1.sort()
#print(words_1)
# slice the string:
#for i in words:
#    print(i)
#    words.sort(key=words[i])
#    print(words)
