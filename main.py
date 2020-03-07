import sys
from cachorro import Cachorro
lista_de_caes = []

def main():
    while 1:
        menu = '''1) cadastrar cão
2) listar cães
3) Sair
'''
        try:
            opcao = int(input(menu))
        except ValueError:
            print('Opção Invalida')
            main()
        if opcao == 1:
            print('Cadastrar cachorro!')
            nome = input('Nome do cachorro: ')
            raca = input('Raça do cachorro: ')
            while 1:
                sexo = input('Qual sexo do cachorro: [M] Macho / [F] Femea: ').upper()
                if sexo[0] in 'MF':
                    break
                else:
                    print('[M] Macho / [F] Femea')
            while 1:
                try:
                    idade = int(input('Qual a idade do animal: '))
                    break
                except ValueError:
                    print('Apenas números são permitidos!')
            cao = Cachorro(nome,raca,sexo,idade)
            lista_de_caes.append(cao)
        elif opcao == 2:
            if lista_de_caes:
                for caes in range(len(lista_de_caes)):
                    print(f'{caes+1} - {lista_de_caes[caes].nome}')
                posicao = input('\nEscolha o cachorro a manipular: ')

                if posicao:
                    try:
                        posicao = int(posicao)
                        manipular_cachorro(lista_de_caes[posicao - 1], lista_de_caes)
                    except ValueError:
                        print('Apenas números!')
                    except IndexError:
                        print('Posição invalida.')
                else:
                    print('Precisa cadastrar algum cachorro primeiro.')

        elif opcao ==3:
            sys.exit(0)

        else:
            print('Escolha uma opção valida!')


def manipular_cachorro(cao_atual, lista_de_cachorros):
    while 1:
        menu = '''1) Ver dados do cachorro
2) Alimentar
3) Brincar
4) Cruzar
5) Menu Inicial
'''

        try:
            opcao = int(input(menu))
        except ValueError:
            print('\n 1,2,3,4 ou 5 !!!!')
            continue

        if opcao ==1:
            print('\n Aqui estão os dados do seu animalzinho')
            print(cao_atual.obter_dados())

        elif opcao ==2:
            if cao_atual.energia < 50:
                comida = input('''\n Alimentar Cachorro
[R] Ração
[C] Carne
[L] Legumes'''
).upper()
                if comida not in 'RCL':
                    print('\n Não temos essa comida!')
                    continue
                print(f'Energia apos comer uma otima refeição: {cao_atual.comer(comida)}')
            else:
                print(f'\n {cao_atual} não precisa comer por agora')

        elif opcao == 3:
            if cao_atual.energia >=40:
                brincadeira = input(f'''\n Vamos brincar {cao_atual}
[B] Buscar bolinha
[S] Saltar
[G] Girar pelo chão
''').upper()
                if brincadeira not in 'BSG':
                    print('Não tem essa brincadeira')
                    continue
                print(f'\n Energia apos brincar: {cao_atual.brincar(brincadeira)} ')
            else:
                print(f'\n {cao_atual} tem que comer primeiro!')

        elif opcao == 4:
            if not cao_atual.energia >= 80:
                print(f'\n {cao_atual} precisa de energia antes do vuco vuco!')
                continue
            tinder_canino = []
            for cao in lista_de_caes:
                if cao_atual.pode_cruzar(cao):
                    tinder_canino.append(cao)
            if not tinder_canino:
                print('\n Nenhum parceiro disponivel, volte mais tarde!')
            else:
                print('Escolha um para dar match ( ͡° ͜ʖ ͡°) ')
                for disponiveis in range(len(tinder_canino)):
                    print(f'{disponiveis+1} - {tinder_canino[disponiveis].nome}')
                while 1:
                    try:
                        selecao = int(input(f'Escolha o número do cachorro para cruzar [0 - Voltar] : '))
                        break
                    except ValueError:
                        print('\n Apenas números !')
                        continue

                if not selecao:
                    break
                try:
                    parceiro = tinder_canino[selecao - 1]
                except IndexError:
                    print('\n Opção invalida')

                else:
                    resultado  = cao_atual.cruzar(parceiro)
                    print(f'O vuco vuco gerou : {resultado}')

        elif opcao == 5:
            main()

        else:
            print('Escolha um opção valida !')


main()