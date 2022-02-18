#Duas palavras podem ser consideradas anagramas de si mesmas se as letras 
# de uma palavra podem ser realocadas para formar a outra palavra. 
# Dada uma string qualquer, desenvolva um algoritmo que encontre 
# o número de pares de substrings que são anagramas.

import itertools

senha = input(str("Digite a senha: "))
lista = list(senha)

x = list(itertools.combinations(lista, 2))
print(x)
print(len(x))