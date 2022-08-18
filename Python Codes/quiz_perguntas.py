#perguntas e respostas com dicionário
#para mais perguntas basta duplicar os dicionários 'Pergunta1,2,3.. criar as perguntas que preferir

perguntas = {
        'Pergunta1': {
           'pergunta': 'Quanto é 2 + 2 ?',
           'respostas': {'a': '1','b': '4','c': '5'},
           'resposta_certa': 'b',
        },
        'Pergunta2': {
                'pergunta': 'Quanto é 3 * 2 ?',
                'respostas': {'a': '4', 'b': '10', 'c': '6'},
                'resposta_certa': 'c',
        },
}

continuar = True

while continuar == True:
    respostas_certas = 0
    print('')
    for pk, pv in perguntas.items():
            print(f'{pk} : {pv["pergunta"]}')
            print('Opções abaixo: ')
            for rk, rv in pv['respostas'].items():
                    print(f'[{rk}] : [{rv}]')

            resposta = input('Digite a letra correspondente a resposta:\n')

            if pv['resposta_certa'] == resposta:
                    print('a resposta está correta\n')
                    respostas_certas += 1
            else:
                    print('a resposta está incorreta\n')

    qtd_perguntas = len(perguntas)
    print(f"Você acertou {respostas_certas / qtd_perguntas * 100}% resposta(s)\n")

    desejo = input('Deseja continuar o teste?\n'
                          'Digite 1 - Para continuar\n'
                          'Digite 0 - Para sair\n')

    if desejo == '1':
            continuar = True
    elif desejo == '0':
            continuar = False
    else:
        print('Código inválido!\n')
        controle = True
        while controle == True:
            desejo = input('Deseja continuar o teste?\n'
                            'Digite 1 - Para continuar\n'
                            'Digite 0 - Para sair\n')
            if desejo == '1':
                controle = False
                continuar = True
            elif desejo == '0':
                controle = False
                continuar = False
            else:
                print('Código inválido!\n')
