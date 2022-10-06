
# VARIAVEIS <= ESPACOS NA MEMORIA DO COMPUTADOR PARA ARMAZENAR INFORMACOES

# ENTRADAS E SAIDAS DE INFORMACOES <= INPUT() PRINT()

# OPERADORES <= ARITMETICOS, RELACIONAIS, LOGICOS

# ESTRUTURA CONDICIONAL <= IF, ELIF E ELSE

"""
    Escrever um programa que solicite ao usuário:

    => O nome de um funcionário; 
    => Seu salário.
    
    Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10% sobre o que ultrapassar R$ 5.000,00.
    No final, apresentar:
    
    => O nome do funcionário; 
    => O salário bruto; 
    => O valor do desconto; 
    => O salário líquido.

    PEGAR NOME E SALARIO, 

"""

"""

funcionario = input('Escreva o nome do funcionario: ')
salario = float(input('Coloque o salario bruto: '))

desconto = 0

if salario > 5000:
    desconto = (salario - 5000)*0.1

salario_liquido = salario - desconto

print('')
print('*=10')

print(f'Nome do funcionario: {funcionario}')
print(f'Salario Bruto {salario}')
print(f'O valor do desconto {desconto}')
print(f'Salario liquido {salario_liquido}')

"""
 # ==================

 # COLECOES

    # listas (list)

minha_lista = ['julio', 10, True, 5.50]

alunos = ['Alan', 'Ricardo', 'Vagner', 'Ana', 'Ramon', 'Renato', 'a', 'a'] # indice[0,1,2,3,4,5]

# print(alunos)

# print(type(alunos))

# print(alunos[5])

# print(alunos[len(alunos) - 1])

# print(alunos[2:])

# print(alunos[2:4])

# alunos[0] = alunos[5]

# alunos[0] = alunos[5]


# METODOS DE LISTAS

alunos.append('julio') # metodo de adicionar

# alunos.clear() # limpa a lista

# retorno = alunos.pop(6) # excluir elemente returnando o que excluiu

# num = alunos.count('a') # conta quanta vezes o elemento(recebido como argumento) tem na lista

# alunos.sort() # ordena a lista de forma crescente

# alunos.remove('a') # remove a primeira posicao encontrada.

# print(alunos)


    # tuplas

minha_tupla = ('julio', 10.8, 10, True)
dias = ('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab')

x = dias.count('dom') # conta quanta vezes o elemento(recebido como argumento) tem na tupla
y = dias.index('sex') # retorn a primeira posicao do elemento informado














