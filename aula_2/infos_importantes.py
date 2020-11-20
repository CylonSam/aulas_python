teste = "teste"
string_padrao = "string" + teste # juntando strings com o operador soma (para strings padrao)
string_f = f"string {teste}" # juntando strings utilizando f strings

texto_n1 = "2.3" # string de um numero decimal
n1 = float(texto_n1) # converte a string em numero decimal (float)
print(f"{n1} é um numero do tipo float")

texto_n2 = "42" # string de um numero inteiro
n2 = int(texto_n1) # converte a string em numero inteiro (int)
print(f"{n2} é um numero do tipo integer")

if n2 > n1: # Lê-se: Se n2 for maior que n1
	print("{n2} é maior que {n1}")
elif n2 == n1: # Lê-se: Se não for maior que n1 e se n2 for igual a n1
	print("{n2} é igual a {n1}")
else:  # Lê-se: Se n2 não for maior que n1 e se n2 não for igual a n1 (ou seja, n2 é menor que n1)
	print("{n2} é menor que {n1}")