numero = int(input("informe um numero : "))

fatorial = 1

for cont in range(1,numero +1):
    fatorial *= cont
print("o fatorial", numero, "é", fatorial)
