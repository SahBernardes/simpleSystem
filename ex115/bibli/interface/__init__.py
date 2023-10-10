'''
Crie um pequeno sistema modularizado q permita cadastrar pessoas
pelo nome, idade em um arquivo de txt simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
tds as pessoas cadastradas
'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um n° inteiro valido: \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo Usuario. \033[m')
            return 0
        else:
            return n


def linha(t=50):
    return '*' * t


def cabecalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32m Sua opção: \033[m')
    return opc
