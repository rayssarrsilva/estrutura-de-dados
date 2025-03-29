# Estrutura de chave valor, busca muito rapida
#Exemplos: Dicionários, cache

banco = {
    'nome': 'Rayssa',
    'idade': 19,
    'hobby': 'programar'
}

print(f'O nome do usuario cadastrado é {banco["nome"]}, ele(a) tem {banco['idade']} anos e gosta de {banco['hobby']}')

banco['estado civil'] = 'solteiro'
print(banco)

del banco['estado civil']
print(banco)

for nome, status in banco.items():
    print(f'{nome}: {status}')

print('as chaves no banco são:')
for chave in banco.keys():
    print(f'{chave}')