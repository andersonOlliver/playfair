# Algoritmo de cifra de Playfair
# Desenvolvido por Anderson Oliveira
# Para disciplina de criptografia de dados

import os


def existe(nome_do_arquivo):
    try:
        f = open(nome_do_arquivo)
        f.close()
        return 1
    except:
        return 0


def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])


def tela_inicial():
    """
    # Irá apresentar um menu de opções ao usuário e receber sua resposta
    # caso resposta seja válida retornará o valor informado
    :return:
    # valor numerico inteiro
    """
    resposta_usuario = -1
    while resposta_usuario < 0 or resposta_usuario > 3:
        print('Escolha')
        print('1 - Criptografar')
        print('2 - Decriptografar')
        print('3 - Sair')

        resposta_usuario = int(input('Entre com a opção desejada: '))

        if resposta_usuario < 0 or resposta_usuario > 3:
            cls()
            print('resposta inválida')

    return resposta_usuario


def ler_arquivo():
    caminho_arquivo = input('Informe o caminho do arquivo: ')

    if existe(caminho_arquivo):
        print('Arquivo existe')
    else:
        print('arquivo não existe')


def cripografar():
    print('método não implementado')
    pass


def decripografar():
    print('método não implementado')
    pass


def inicio():
    resposta = 0

    while resposta != 3:
        resposta = tela_inicial()

        if resposta == 1:
            cripografar()
        elif resposta == 2:
            decripografar()
        elif resposta == 3:
            cls()
            print('Nunca será um adeus!')
            print('Até mais...')
            exit()

        cls()


##################################
#       Início do programa       #
##################################
print('Bem vindo')
inicio()
