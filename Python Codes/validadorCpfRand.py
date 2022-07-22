import random

#num = [random.randint(1, 9) for x in range(9)]
num = [random.randint(1, 9) for x in range(9)]
#print(num)
p2 = [1, 6, 8, 9, 9, 5, 3, 5, 0, 0]
novo_cpf = [1, 6, 8, 9, 9, 5, 3, 5, 0, 0, 9]
reverso = 10 #o valor que multiplicará os valores randomicos
total = 0 # para armazenar as somas da multip dos rand com o reverso

#p vai ser para os indices de 0,8 e 0,9 para percorrer os randomicos
for p in range(19):
    if p > 8: #serve para quando chegar no indice 9, reiniciar e contar mais 10
        p -= 9
    #print(p, reverso)

    total += num[p] * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11 #reverso quando for igual a 1 ele volta ele é modificado para reiniciar
        d = 11 - (total % 11) # valor do primeiro digito, casa 10

        if d > 9:
            d = 0
        total = 0 #reinicar a varivel para acumular a nova soma do reverso modificado(isso está fora do if acima!)
        num.append(d)

num.insert(3, '.') # inserindo os caracterers do CPF
num.insert(7, '.')
num.insert(11, '-')

cpf = "".join(map(str, num)) # conversão da lista de inteiros em uma string, que com a inserção...
                             #dos caracteres acma se tornou uma lista mista
print(cpf)

'''
if cpf == novo_cpf:
    print('CPF válido')

else:
    print('CPF inválido')
'''