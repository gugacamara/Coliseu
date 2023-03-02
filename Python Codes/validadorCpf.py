import re


class ValidadorCpf:
    def __init__(self):
        pass
        
    #removendo caracteres especiais com expressão regular
    def remover_caracteres(self, cpf):
        return re.sub(r'[^0-9]', '', cpf)

    #todas as sequencias são validáveis, por isso verificar se é e eliminar
    def verificar_sequencia(self, cpf):
        sequencia = cpf[0] * len(cpf)
        if sequencia == cpf:
            return True
        else:
            return False

    #encontrando o digito
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

    #inserindo caracteres especiais
    def inserindo_caracteres(self, cpf):
        return f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'

    def valida(self, cpf):
        #cpfUser é o cpf digitado pelo usuario
        #cpf_teste é o cpf fatiado para ser calculado e gerado os dois valores finais
        #cpf_teste_string é o cpf_teste para ser comparado com o cpfUser

        cpfUser = self.remover_caracteres(cpf)

        if len(cpfUser) != 11:
            print(f'O CPF está incorreto!')
            return False

        if self.verificar_sequencia(cpfUser):
            print('O CPF não pode ser uma sequência!')
            return False

        cpf_teste = list(cpfUser[0:9])
        cpf_teste = [int(i) for i in cpf_teste]
        
        #encontrando o primeiro digito
        primeiro_digito = self.encontrando_digito(cpf_teste)
        cpf_teste.append(primeiro_digito)

        #encontrando o segundo digito
        segundo_digito = self.encontrando_digito(cpf_teste)
        cpf_teste.append(segundo_digito)

        #transformando em string para comparar com o cpfUser
        cpf_teste_string = "".join(map(str, cpf_teste))

        #quando for válido mostrar o cpf formatado corrigido, inválido mostra o que o usuário digitou
        if cpfUser == cpf_teste_string:
            cpf_formatado = self.inserindo_caracteres(cpf_teste_string)
            return print(f'O CPF {cpf_formatado} é válido!')
        else:
            cpf_formatado = self.inserindo_caracteres(cpfUser)
            return print(f'O CPF {cpf_formatado} é inválido!')

if __name__ == '__main__':
    usuario = ValidadorCpf()
    cpf = input('Digite o seu CPF.\n')
    usuario.valida(cpf)

