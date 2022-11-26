import random

class GeradorCpf:
    def __init__(self):
        pass

    def encontrando_digito(self, cut_cpf):
        MULT_CPF = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        if len(cut_cpf) == 9:
            MULT_CPF = MULT_CPF[1:10]

        mult = [x * y for x, y in zip(cut_cpf, MULT_CPF)]
        soma = sum(mult)
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0
        return digito

    def inserindo_caracteres(self, cnpj):
        return f'{cnpj[0:3]}.{cnpj[3:6]}.{cnpj[6:9]}-{cnpj[9:11]}'

    def geradora(self, encontrando_digito, inserindo_caracteres):
        randomico = [random.randint(1, 9) for x in range(9)]

        #encontrando o primeiro digito
        primeiro_digito = encontrando_digito(randomico)
        randomico.append(primeiro_digito)

        #encontrando o segundo digito
        segundo_digito = encontrando_digito(randomico)
        randomico.append(segundo_digito)

        cpf = "".join(map(str, randomico))
        print(inserindo_caracteres(cpf))

