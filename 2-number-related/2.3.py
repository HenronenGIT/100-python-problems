# Take numbers from a user and show the average of the numbers the user entered.

nb_count = int(input("How many numbers you would like to input?\n"))
i = 0
sum = 0
while i < nb_count:
    nb = int(input("Give a number\n"))
    sum = sum + nb
    i += 1
average = sum / nb_count
print(average)
