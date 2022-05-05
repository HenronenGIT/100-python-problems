# Find the largest element of a list.

biggest = 0
list = [32, 11, 90, 40, 60, 10]

for num in list:
    if (num > biggest):
        biggest = num

print(biggest)