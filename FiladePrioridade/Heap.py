# Elementos com prioridade
# Exemplos: algoritmos de busca, agendamentos

import heapq

valores = [5, 7, 9, 1, 3, 2]

heapq.heapify(valores) 
print(valores) 

pacientes = [
    (3, 'paciente'),
    (2, 'paciente com crise'),
    (1, 'paciente em estado de urgencia')
]

heapq.heapify(pacientes)
print(pacientes)

while pacientes:
    prioridade, paciente = heapq.heappop(pacientes) #remove o item de urgencia
    print(f'atendendo {paciente} (prioridade {prioridade})')


tarefas = [(2, "cozinhar"), (1, "dormir")]

heapq.heapify(tarefas)


# Inserir nova tarefa
heapq.heappush(tarefas, (0, "Ir ao médico"))

# Remover a mais prioritária
heapq.heappop(tarefas)

print(tarefas)