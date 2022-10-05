
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

funcionario = input('Escreva o nome do funcionario: ')
salario = float(input('Coloque o salario bruto: '))

desconto = 0

if salario > 5000:
    desconto = (salario - 5000)*0.1

salario_liquido = salario - desconto

print('')
print('=*info')

print(f'Nome do funcionario: {funcionario}')
print(f'Salario Bruto {salario}')
print(f'O valor do desconto {desconto}')
print(f'Salario liquido {salario_liquido}')










