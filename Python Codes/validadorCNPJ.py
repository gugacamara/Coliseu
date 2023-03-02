import re

MULT_CNPJ = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida(cnpj):

    cnpj1 = remover_caracteres(cnpj)

    if len(cnpj1) != 14:
        print(f'O CNPJ está incorreto!')
        return False

    if verificar_sequencia(cnpj1):
        print('O CNPJ não pode ser uma sequência!')
        return False

    #formatando a string e transformando em lista
    #cnpj2 é o cnpj do usuário fatiado para ser usado nos calculos e chegar no mesmo resultado do cnpj1
    cnpj2 = list(cnpj1[0:12])
    cnpj2 = [int(i) for i in cnpj2]

    #encontrando o primeiro digito
    num = encontrando_digito(cnpj2, MULT_CNPJ[1:13])
    cnpj2.append(num)
    #encontrando o segundo digito
    num = encontrando_digito(cnpj2, MULT_CNPJ)
    cnpj2.append(num)

    #lista formatada serve para exibir e a sem para comparação
    cnpj_string = "".join(map(str, cnpj2))

    #quando for válido mostrar o cnpj formatado corrigido, inválido mostra o que o usuário digitou
    if cnpj1 == cnpj_string:
        return print(f'O CNPJ {inserindo_caracteres(cnpj_string)} é válido!')
    else:
        return print(f'O CNPJ {inserindo_caracteres(cnpj1)} é inválido!')

def verificar_sequencia(cnpj):
    #todas as sequencias são validáveis, por isso verificar se é e eliminar
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def encontrando_digito(novo_cnpj, mult_cnpj):
    mult = [x * y for x, y in zip(novo_cnpj, mult_cnpj)]
    soma = sum(mult)
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return digito

def inserindo_caracteres(cnpj):
    return f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'


usuario = input('Digite o seu CNPJ.\n')
valida(usuario)

