# Esse programa pede dois numeros e diz qual é maior

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print(n1 - n2)

maior_numero = 0 # inicializando a variavel

if n1 > n2: # se n1 for maior que n2
    maior_numero = n1
else: # se não for, então n1 é maior OU igual a n2
    maior_numero = n2

print(f"Maior numero: {maior_numero}")