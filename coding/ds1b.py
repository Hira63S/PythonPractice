#   x = 10
#y = 50
#number = 160
#total = 1760

#10*x + 50*y = 1760
#x + y = 160
#find(x)
#find(y)

#if total == 1760:
#    print(x)
#else:
#    print(y)
#with simple arithmatic, I did find that it is 156 10s and 4 fifties.
for tens in range(0, 160):
    for fifties in range(0,160):
        if tens + fifties != 160: #first condition where 10s and 50s have to equal 160
            continue
        if fifties * 50 + tens * 10 != 1760: #second condition where value has to equal 1760 when added together
            continue
        print('Number of 10s: ', tens, 'Number of 50s', fifties, "in the drawer")
        break
