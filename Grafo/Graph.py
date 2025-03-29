# Conjunto de nós e arestas
# Exemplos: Redes sociais, mapas

graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'E'],
    'C': ['D', 'D', 'E'],
    'D': ['E', 'F', 'G']
}

#for iterador in graph:
    #print(f'{iterador} -> {graph[iterador]}')

for iterador in graph['A']:
    print(iterador)