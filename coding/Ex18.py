def print_three(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")


def print_two_again(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

def print_one(arg2):
    print(f"arg2: {arg2}")

def print_none():
    print("I got nothin'.")

print_three("BMW", "Mercedes", "Audi")
print_two_again("billi", "pie", "shoneo")
print_one("just billi")
print_none()
