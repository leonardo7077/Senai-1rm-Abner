def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def maior_numero(a, b):
    return max(a, b)

def menor_numero(a, b):
    return min(a, b)

# Função para exibir o menu
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Somar")
    print("2. Multiplicar")
    print("3. Maior número")
    print("4. Menor número")

# Leitura dos valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Exibição do menu
exibir_menu()

# Leitura da opção escolhida
opcao = int(input("Digite o número da opção desejada: "))

# Verificação da opção escolhida e exibição do resultado
if opcao == 1:
    resultado = somar(valor1, valor2)
    print("Resultado da soma:", resultado)
elif opcao == 2:
    resultado = multiplicar(valor1, valor2)
    print("Resultado da multiplicação:", resultado)
elif opcao == 3:
    resultado = maior_numero(valor1, valor2)
    print("Maior número:", resultado)
elif opcao == 4:
    resultado = menor_numero(valor1, valor2)
    print("Menor número:", resultado)
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

