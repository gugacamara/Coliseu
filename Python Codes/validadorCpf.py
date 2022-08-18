import re

MULT_CPF = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

def remover_caracteres(cpf):
    return re.sub(r'[^0-9]', '', cpf)

def verificar_sequencia(cnpj):
    #todas as sequencias são validáveis, por isso verificar se é e eliminar
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False

def encontrando_digito(novo_cpf, mult_cpf):
    mult = [x * y for x, y in zip(novo_cpf, mult_cpf)]
    soma = sum(mult)
    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    return digito

def inserindo_caracteres(cpf):
    return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

def valida(cpf):
    #cpf1 é o cpf digitado pelo usuario
    #cpf2 é o cpf fatiado para ser calculado e gerado os dois valores finais
    #cpf_string é o cpf2 para ser comparado com o cpf1

    cpf1 = remover_caracteres(cpf)

    if len(cpf1) != 11:
        print(f'O CPF está incorreto!')
        return False

    if verificar_sequencia(cpf1):
        print('O CPF não pode ser uma sequência!')
        return False

    cpf2 = list(cpf1[0:9])
    cpf2 = [int(i) for i in cpf2]

    #encontrando o primeiro digito
    primeiro_digito = encontrando_digito(cpf2, MULT_CPF[1:10])
    cpf2.append(primeiro_digito)

    #encontrando o segundo digito
    segundo_digito = encontrando_digito(cpf2, MULT_CPF)
    cpf2.append(segundo_digito)

    cpf_string = "".join(map(str, cpf2))

    #quando for válido mostrar o cpf formatado corrigido, inválido mostra o que o usuário digitou
    if cpf1 == cpf_string:
        cpf_formatado = inserindo_caracteres(cpf_string)
        return print(f'O CPF {cpf_formatado} é válido!')
    else:
        cpf_formatado = inserindo_caracteres(cpf1)
        return print(f'O CPF {cpf_formatado} é inválido!')

usuario = input('Digite o seu CPF.\n')
valida(usuario)
