# Take a number as input. Then get the sum of the numbers. If the number is n. Then get
# 0^2+1^2+2^2+3^2+4^2+.............+n^2

i = 0

nb = int(input("Give a number: "))
sum = 0
while (i <= nb):
    sum = sum + i ** 2
    i = i + 1
print(sum)