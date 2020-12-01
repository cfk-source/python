for x in range(1,101):
    if ((x % 3 == 0) & (x % 5 == 0)):
        print(x,"Fizz & Buzz")
    elif (x % 3 == 0):
        print(x,"Fizz")
    elif (x % 5 == 0):
        print(x,"Buzz")