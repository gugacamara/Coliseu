import re
import random

MULT_CNPJ = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def encontrando_digito(novo_cnpj, mult_cnpj):
    mult = [x * y for x, y in zip(novo_cnpj, mult_cnpj)]
    soma = sum(mult)
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return digito


def inserindo_caracteres(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'

def geradora():
    randomico = [random.randint(1, 9) for x in range(8)]
    randomico.append(0)
    randomico.append(0)
    randomico.append(0)
    randomico.append(1)

    #encontrando o primeiro digito
    primeiro_digito = encontrando_digito(randomico, MULT_CNPJ[1:13])
    randomico.append(primeiro_digito)

    #encontrando o segundo digito
    segundo_digito = encontrando_digito(randomico, MULT_CNPJ)
    randomico.append(segundo_digito)

    cnpj = "".join(map(str, randomico))
    print(inserindo_caracteres(cnpj))

geradora()


