x = 3.52 #price per gallon in week 1
y = 3.57 # price per gallon in week 2
p1 = 23 #no. of passengers in week 1
f1 = 29 #fare per passengers in week 1
m1 = 160 #mileage in week 1

p2= 17 #no. of passengers in week2
f2 = 30 #fare per passenger in week2
m2 = 220 #mileage in week 2

w1 = (m1 / 20)*x; #average price for gas week 1
w2 = (m2 / 20)*y; #average price for gas week2

profit1 = (p1*f1) - w1;
profit2 = (p2*f2) - w2;

print(profit1)
print(profit2)

totalprofit = profit1 + profit2;

print(totalprofit)
