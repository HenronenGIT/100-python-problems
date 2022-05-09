# Divisible by 3 and 5
nb = int(input('Please give a number:'))

while nb > 0:
    nb_2 = (nb - 1)
    #if ((nb_2 % 3) == 0) | 
    if ((nb_2 % 5) == 0):
        print (nb_2)
    nb = nb - 1
