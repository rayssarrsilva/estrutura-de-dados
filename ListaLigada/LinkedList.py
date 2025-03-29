#Lista Ligada, deixa os dados dinamicos pois cada celula possui um ponteiro que aponta para o proximo valor
# Exemplo: Lista de contatos, Lista de tarefas, Lista de compras
# Estrutura de dados: Lista Ligada (Linked List)
# ATENÇÃO: Não é possivel acessar um elemento diretamente, tem que percorrer a lista até chegar no desejado


class No:
    def __init__(self, valor): #construtor
        self.valor = valor 
        self.proximo = None #Um nó sempre aponta para o próximo


No1 = No(10)
No2 = No(40)
No3 = No(60)

No1.proximo = No2 
No2.proximo = No3

iterador = No1 #Nó atual, o qual será iniciada a iteração
while iterador:
    print(iterador.valor) #mostra o valor definido para os respectivos nós, e depois vai para o próximo
    iterador = iterador.proximo #atualiza para o próximo

abc = input("qual valor deseja encontrar?")