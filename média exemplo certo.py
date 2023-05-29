nota_1 = float(input("informe a nota 1: "))
nota_2 = float(input("informe a nota 2: "))
nota_3 = float(input("informe a nota 3: "))

media = (nota_1 + nota_2 + nota_3) /3

if media >= 6:
    print("Aprovado")
else:
    if media >= 5:
     print("conselho de classe")
    else:
       print("reproveiton")

print ("a sua media final foi: ", media)

