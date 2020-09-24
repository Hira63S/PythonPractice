def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a*b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a/b

print("let's do some math with just functions!")

#age = add(a=input("give later age of Salar Sikander"), b = input("give age when Imama met him"))
#height = multiply(a=input("height when he was younger"), b=input("when he meets imama again"))
#iq = divide(a=input("His IQ as a child"), b=input("his IQ now"))

#print(f"Age: {age}, Height: {height}, iq:{iq}")
age = add((input("Salar Sikander's age when he met Imama ")), (input("time away from imama ")) )
height = subtract((input("His height being older")), (input("his height younger")))
weight = multiply(( input("his weight at the age of 30")), ( input("his weight when he gets tumor ")))
iq = divide((input("his iq when he was younger")), (input("the difference when he got older")))
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


    # A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
