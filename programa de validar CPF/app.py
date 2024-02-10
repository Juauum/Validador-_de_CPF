# Calculo dos dígitos verificadores(DV) de um CPF 

cpf = []
mult = [10,9,8,7,6,5,4,3,2]
resultado = []

print("\033[1;32mCalculo dos (DV) do cpf \033[m")
print()
cpf = list(map(int, input("Informe os nove números do seu CPF:\n")))
print("="*35)

for x,y in zip(cpf,mult):
				resultado.append(x * y)

print(resultado)

soma_cpf = sum(resultado)
print(f"Soma dos valores do cpf : {soma_cpf}")

resto_div = soma_cpf % 11
print(f"Resto da divisão : {resto_div}")

x = 11 - resto_div
print(f"Valor de X: {x}")

print("-"*35)

# Calculo para o Segundo digito verificador

resultado2 = []

copia_cpf = cpf.copy()
#copia_cpf = cpf[:]

del cpf[0]
#cpf.pop(0)

cpf.append(x)

for x,y in zip(cpf,mult):
  resultado2.append(x * y)
  
print(resultado2) 

soma_cpf2 = sum(resultado2)

print(f"Soma dos valores do cpf : {soma_cpf2}")

resto_div2 = soma_cpf2 % 11
print(f"Resto da divisão : {resto_div2}")

y = 11 - resto_div2
print(f"Valor de Y: {y}")

print("-"*35)

# CPF completo

copia_cpf.insert(10,x)
copia_cpf.insert(11,y)
#copia_cpf.append(x)
#copia_cpf.append(y)

print(f"Seu CPF completo é: ")

for pos, n in enumerate(copia_cpf):
	  print(n,end=" ")
	  if pos == 2:
	     print(". ",end="")
	  if pos == 5:
	  				 print(". ",end="")
	  if pos == 8:
	  				 print("- ",end="")
					  
					    