def maior(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c

a1 = int(input("Numero 1: "))
a2 = int(input("Numero 2: "))
a3 = int(input("Numero 3: "))



print (maior(a1,a2 , a3))