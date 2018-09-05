# Algoritmo de cifra de Playfair
# Desenvolvido por Anderson Oliveira
# Para disciplina de criptografia de dados

import os


def existe(nome_do_arquivo):
    try:
        f = open(nome_do_arquivo, 'r')
        f.close()
        return 1
    except Exception as e:
        print(e)
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


def ler_arquivo_entrada():
    conteudo_arquivo = ''
    while not conteudo_arquivo:
        caminho_arquivo = input('Informe o caminho do arquivo de entrada: ')
        print('------------------------------------')
        print(caminho_arquivo)
        print('------------------------------------')
        caminho_arquivo = caminho_arquivo.replace('\u202a', '')
        resultado = existe(caminho_arquivo)
        print(resultado)

        if existe(caminho_arquivo):
            r = open(caminho_arquivo)
            texto = []
            for x in r:
                texto.append(x)

            conteudo_arquivo = ''.join(map(str, texto))
            print(conteudo_arquivo)
            return conteudo_arquivo
        else:
            return 0


def ler_arquivo_saida():
    caminho = input('Informe o caminho do arquivo de saída: ')
    return caminho.replace('\u202a', '')


def ler_chave():
    chave = input('Informe a chave a ser utilizada: ')
    return chave


def gravar_arquivo(caminho, conteudo):
    f = open(caminho, "w+")
    f.write(conteudo)


def realizar_criptografia(conteudo, chave):
    print('================================================')
    print('Iniciando processamento')
    print(conteudo)
    print(chave)
    return conteudo + chave


def cripografar():
    conteudo_arquivo = ler_arquivo_entrada()
    chave = ler_chave()
    caminho_saida = ler_arquivo_saida()

    resultado = realizar_criptografia(conteudo_arquivo, chave)

    sucesso = gravar_arquivo(caminho_saida, resultado)

    return sucesso


def decriptografar():
    print('método não implementado')
    pass


def inicio():
    resposta = 0

    while resposta != 3:
        resposta = tela_inicial()

        if resposta == 1:
            cripografar()
        elif resposta == 2:
            decriptografar()
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

# 1 - Letras de texto claro repetidas que estão no mesmo par são separadas por uma de preenchimento, como x, de modo que
#     balloon seria tratado como ba lx lo on.
#
# 2 - Duas letras de texto claro que estejam na mesma linha da matriz são substituídas pela letra à direita, com o
#     primeiro elemento da linha vindo após o último, de forma rotativa. Por exemplo, ar é encriptado como RM.
#
# 3 -
#
#
#
