# coleção de elementos indexados, util para alteraões rápidas de acordo com o index do elemento na lista
#Exemplos: Lista de compras, Lista de tarefas, Lista de contatos
#Estrutura de dados: Array (Lista)
#ATENÇÃO: Indicies começam com 0

lista = [1, 1, 2 , 3, 5, 8, 13, 21] #fibonacci

lista[0] = 0 #altera o primeiro pra 0
lista[4] = 4
print(lista)
print(len(lista)) #8
lista.remove(lista[-1]) #remove com base no index da lista
lista.remove(13) #remove com base no valor
print(lista)
print(len(lista)) #6