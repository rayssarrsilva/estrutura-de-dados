#Primeiro que entra e primeiro que sai
#Exemplo: Fila de espera, Impressão de documentos, Navegação em páginas web, atividades em ordem de chegada
#Estrutura de dados: Fila (Queue)

from collections import deque #Biblioteca para trabalhhar com Queue

atividades = deque()

atividades.append("Lavar louça") #insere no final
atividades.append("Estudar")
atividades.append("Fazer compras")
atividades.append("dormir")

atividades.popleft() #remove a primeira tarefa, a primeira que deve ser concluida primeiro
print(atividades) #Imprime as atividades restantes
