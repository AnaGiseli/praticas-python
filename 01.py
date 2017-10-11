#Questão 01

frase = input("Digite uma frase: ")
caractere = input("Digite um caractere para pesquisar: ")

frase = frase.upper()
caractere = caractere.upper()

if caractere in frase:
	resultado = frase.count(caractere)
	print("Há %s ocorrência(s) do caractere na frase." % resultado)
else:
	print("Não há esse caractere na frase.")




#Questão 02

palavra = input("Digite uma palavra: ")


contagem = 0

for i in palavra:
	if i in 'aeiouAEIOU':
		contagem +=1		
print("Há %s vogais na palavra." % contagem)



#Questão 03

palavra = input("Digite uma palavra para verificar: ")

palavra_inversa = palavra[::-1]

if palavra == palavra_inversa:
	print("A palavra é um palíndromo. ")
else:
	print("Não é um palíndromo.")



#Questão 04


frase = input("Digite uma frase: ")

#Separar a string
ordem_frase = frase.split() 

#Colocar em ordem alfabética
ordem_frase.sort() 

#Juntar a string separada
frase_final = ' '.join(ordem_frase) 

print(frase_final)




#Questão 05

nome_completo = input("Digite um nome completo: ")

#Primeira letra de cada palavra em maíuscula
nome_maiusculo = nome_completo.title()

nome = nome_maiusculo.split()

primeiro_nome = nome[0]
sobrenome = nome[-1]

print("%s, %s" % (sobrenome, primeiro_nome) )
