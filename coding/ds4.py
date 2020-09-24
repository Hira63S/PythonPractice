def mean(cars):
    length = len(cars)
    total_sum = 0
    for i in range(length):
        total_sum += cars[i]
    total_sum = sum(cars)
    average = total_sum/length
    return average

teslaspeed_mph = [123, 150, 123, 190, 150, 150]
x = mean(teslaspeed_mph)
print(x)


def median(cars):
    length = len(cars)
    median = 0;
    if length % 2 == 0:
        median = (cars[length//2 -1] + cars[length//2])/2
    else:
        median = cars[length//2]
    return median

y = median(teslaspeed_mph)
print(y)


def mode(cars):
    lenght = len(cars)
    modeint = {c: 0 for c in cars}
    frequency = 0
    for b in cars:
        modeint[b] +=1
        if modeint[b] > frequency:
            frequency = modeint[b]
            mode = b
    return mode

c = mode(teslaspeed_mph)
print(c)
