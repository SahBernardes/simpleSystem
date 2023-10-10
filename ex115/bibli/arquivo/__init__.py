from ex115.bibli.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas Cadastradas')
        for l in a:
            dd = l.split(';')
            dd[1] = dd[1].replace('\n', '')
            print(f'{dd[0]:<30}{dd[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idd=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idd}\n')
        except:
            print('Erro no registro dos dados!')
        else:
            print(f'Novo registro de {nome} adcionado')
            a.close()

