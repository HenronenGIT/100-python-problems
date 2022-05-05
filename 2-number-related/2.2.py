# Find the largest of the three numbers.

nb1 = int(input("Give a first number:"))
nb2 = int(input("Give a second number:"))
nb3 = int(input("Give a third number:"))

if (nb1>nb2 & nb1>nb3):
    print("Largest number", nb1)
elif (nb2>nb3 & nb2>nb1):
    print("Largest number", nb2)
else:
    print("Largest number", nb3)

# Could use max() function