#Aula 3 - Listas

primeira_lista = ["Igor","Jonathan","Pietro","Tetinha"]
#----Posição---------1º-------2º--------3º--------4º---
#----Indice----------0--------1---------2---------3----


print(primeira_lista)

print(primeira_lista[0])
print(primeira_lista[1])
print(primeira_lista[2])
print(primeira_lista[3])

print("================Alteração Indice 02 ===============")

primeira_lista [2] = "Melo"

print(primeira_lista[0])
print(primeira_lista[1])
print(primeira_lista[2])
print(primeira_lista[3])

print("================Inserir Novo Aluno=================")

#Função que vem para fluxo de "Lista" chamada "append"

primeira_lista.append("Papudo")

print(primeira_lista)