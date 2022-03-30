# Swap two variables.

nb1 = int(input("Give first number:"))
nb2 = int(input("Give second number:"))
print("1st number->", nb1, "\n2nd number->", nb2)
temp = nb1
nb1 = nb2
nb2 = temp
print("After swap")
print("1st number->", nb1, "\n2nd number->", nb2)