from ex115.bibli.interface import *
from ex115.bibli.arquivo import *
from time import sleep

arq = 'arquivoo.txt'

if not arqExiste(arq):
    criarAquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # cadastrar pessoas no arquivo
        cabecalho('Novo Cadastro')
        nome = str(input('Nome: '))
        idd = leiaInt('Idade: ')
        cadastrar(arq, nome, idd)
    elif resposta == 2:
        # ver a lista de pessoas  no arquivo
        lerAquivo(arq)
    elif resposta == 3:
        # sair do sistema
        cabecalho('Encerrando Programa... Volte Sempre!')
        break
    else:
        # digitou errado no menu
        cabecalho('\033[31mErro! digite uma opção valida por favor!\033[m')
    sleep(1)
