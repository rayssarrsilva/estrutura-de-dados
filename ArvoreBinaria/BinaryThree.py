# Estrutura hierarquica
#exemplo: Representação de arquivos, representação de cargos superiores e inferiores, árvore genealógica, árvore de decisão
# Binary Three

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
    

raiz = No(50)
raiz.esq = No(20)
raiz.dir = No(60)

def em_ordem(no):
    if no:
        em_ordem(no.esq)
        print(no.valor)
        em_ordem(no.dir)

em_ordem(raiz)
