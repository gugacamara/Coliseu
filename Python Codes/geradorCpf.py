import random

MULT_CPF = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

def encontrando_digito(novo_cpf, mult_cpf):
    mult = [x * y for x, y in zip(novo_cpf, mult_cpf)]
    soma = sum(mult)
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return digito

def inserindo_caracteres(cnpj):
    return f'{cnpj[0:3]}.{cnpj[3:6]}.{cnpj[6:9]}-{cnpj[9:11]}'

def geradora():
    randomico = [random.randint(1, 9) for x in range(9)]

    #encontrando o primeiro digito
    primeiro_digito = encontrando_digito(randomico, MULT_CPF[1:10])
    randomico.append(primeiro_digito)

    #encontrando o segundo digito
    segundo_digito = encontrando_digito(randomico, MULT_CPF)
    randomico.append(segundo_digito)

    cpf = "".join(map(str, randomico))
    print(inserindo_caracteres(cpf))

geradora()