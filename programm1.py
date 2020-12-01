a = int(input("Enter triangle side A length "))
b = int(input("Enter triangle side B length "))
c = int(input("Enter triangle side C length "))

z = (a + b + c) // 2
area = (z *(z - a) * (z - b) * (z - c)) ** 0.5

print("Side A =", a, "Side B =", b, "Side C =", c)
print("Triangle area is ", area)
