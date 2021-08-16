# PESQUISA COM PALAVRAS

import time

a_pesquisar = input("Qual o nome que queres pesquisar? ")

#Pesquisa em uma lista
ini_lista = time.time()
lista = ["Homem de Ferro", "Capitão América", "Luke Cage", "Mulher-Aranha", "Homem-Aranha", "Wolverine", "Sentinela", "Ronin", "Doutor Estranho", "Punho de Ferro", "Harpia", "Miss Marvel", "Jessica Jones", "Coisa", "Demolidor", "Raio Negro", "Pantera Negra", "Senhor Fantástico", "Namor", "Fera"]
a_pesquisar in lista
fim_lista = time.time()

#Pesquisa em uma tupla
ini_tupla = time.time()
tupla = ("Homem de Ferro", "Capitão América", "Luke Cage", "Mulher-Aranha", "Homem-Aranha", "Wolverine", "Sentinela", "Ronin", "Doutor Estranho", "Punho de Ferro", "Harpia", "Miss Marvel", "Jessica Jones", "Coisa", "Demolidor", "Raio Negro", "Pantera Negra", "Senhor Fantástico", "Namor", "Fera")
a_pesquisar in tupla
fim_tupla = time.time()

# Pesquisa em um Dicionário
ini_dic = time.time()
dic = {'Homem de Ferro': 0, 'Capitão América':1,'Luke Cage':2, 'Mulher-Aranha':3, 'Homem-Aranha': 4, 'Wolverine': 5, 'Sentinela':6, 'Ronin':7, 'Doutor Estranho':8, 'Punho de Ferro': 9, 'Harpia':10, 'Miss Marvel':11, 'Jessica Jones':12, 'Coisa':13, 'Demolidor':14,'Raio Negro':15, 'Pantera Negra':16, 'Senhor Fantástico':17, 'Namor':18}
a_pesquisar in dic
fim_dic = time.time()

# Pesquisa em um Conjunto
ini_sets = time.time()
conjuntos = {"Homem de Ferro", "Capitão América", "Luke Cage", "Mulher-Aranha", "Homem-Aranha", "Wolverine", "Sentinela", "Ronin", "Doutor Estranho", "Punho de Ferro", "Harpia", "Miss Marvel", "Jessica Jones", "Coisa", "Demolidor", "Raio Negro", "Pantera Negra", "Senhor Fantástico", "Namor", "Fera"}
a_pesquisar in conjuntos
fim_sets = time.time()

print("")
#print(a_pesquisar in lista)
#print(a_pesquisar in tupla)
#print(a_pesquisar in dic)
print(a_pesquisar in conjuntos)
#print("")
#print("Tempo de pesquisa em Lista............", fim_lista-ini_lista)
#print("Tempo de pesquisa em Tupla............", fim_tupla-ini_tupla)
#print("Tempo de pesquisa em Dicionário.......", fim_dic-ini_dic)
#print("Tempo de pesquisa em Conjunto.........", fim_sets-ini_sets)
#print(lista)
#print(tupla)
#print(dic)
#print(conjuntos)


resultado = {"Conjunto": fim_sets-ini_sets, "Tupla": fim_tupla-ini_tupla,"Dicionário": fim_dic-ini_dic, "Lista": fim_lista-ini_lista}
print("")

for i in sorted(resultado, key = resultado.get):
    print(i, " > ", resultado[i])