# Algoritmo de cifra de Playfair
# Desenvolvido por Anderson Oliveira
# Para disciplina de criptografia de dados

import os


def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])


def indice_do_elemento(matriz, elemento):
    posicao = 0
    for linha in matriz:
        for coluna in linha:
            if coluna == elemento:
                return [posicao / 5, posicao % 5]

            posicao += 1


#################################################################
#                          ARQUIVO                              #
#################################################################
def existe(nome_do_arquivo):
    try:
        f = open(nome_do_arquivo, 'r')
        f.close()
        return 1
    except Exception as e:
        print(e)
        return 0


def ler_arquivo_entrada():
    conteudo_arquivo = ''
    while not conteudo_arquivo:
        caminho_arquivo = str(input('Informe o caminho do arquivo de entrada: '))
        caminho_arquivo = caminho_arquivo.replace('\u202a', '')  # nos testes esse caracter sempre aparecia :'(

        if existe(caminho_arquivo):
            r = open(caminho_arquivo)
            texto = []
            for x in r:
                texto.append(x)
            r.close()
            conteudo_arquivo = ''.join(map(str, texto))
            return conteudo_arquivo.upper()
        else:
            return 0


def ler_arquivo_saida():
    caminho = input('Informe o caminho do arquivo de saída: ')
    return caminho.replace('\u202a', '')


def gravar_arquivo(caminho, conteudo):
    f = open(caminho, "w+")
    f.write(conteudo)


#################################################################
#                       FIM ARQUIVO                             #
#################################################################


#################################################################
#                            CHAVE                              #
#################################################################
def ler_chave():
    chave = input('Informe a chave a ser utilizada: ')
    return chave.upper()


def obter_alfabeto():
    alfabeto = "a b c d e f g h i j k l m n o p q r s t u v w x z"
    return alfabeto.upper().split()


def gerar_matriz_chave(chave: str):
    alfabeto = obter_alfabeto()

    matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    posicao: int = 0

    for letra in chave:
        linha = int(posicao / 5)
        coluna = int(posicao % 5)

        if letra.upper() == "Y":
            letra = "X"

        if letra in alfabeto:
            alfabeto.remove(letra)
            matriz[linha][coluna] = letra
            posicao += 1

    while len(alfabeto) > 0:
        linha = int(posicao / 5)
        coluna = int(posicao % 5)

        matriz[linha][coluna] = alfabeto.pop(0)
        posicao += 1
    return matriz


#################################################################
#                          FIM CHAVE                            #
#################################################################


#################################################################
#                         CRIPTOGRAFIA                          #
#################################################################
def cifrar(dupla, matriz):
    pass


def normalizar_texto(texto: str):
    texto = texto.upper()
    print(texto)
    novo_texto = ""
    separador = 1
    tamanho_original = len(texto)
    for i in range(0, tamanho_original):
        if (texto[i] >= "A") and (texto[i] <= "Z"):
            if texto[i] != "Y":
                novo_texto = novo_texto + texto[i]

            if separador < 2:
                if i + 1 < tamanho_original and texto[i] == texto[i + 1]:
                    novo_texto = novo_texto + "X"

                separador += 1
            elif i + 1 < tamanho_original:
                novo_texto = novo_texto + " "
                separador = 1

    if novo_texto[len(novo_texto) - 2] == " ":
        novo_texto = novo_texto + "X"

    return novo_texto


def realizar_criptografia(conteudo, chave):
    print('================================================')
    print('Iniciando processamento')
    print(normalizar_texto(conteudo))
    print(gerar_matriz_chave(chave))
    # matriz_chave = gerar_matriz_chave(chave)
    return conteudo + chave


def cripografar():
    conteudo_arquivo = ler_arquivo_entrada()
    chave = ler_chave()

    caminho_saida = ler_arquivo_saida()

    resultado = realizar_criptografia(conteudo_arquivo, chave)

    gravar_arquivo(caminho_saida, resultado)


#################################################################
#                      FIM CRIPTOGRAFIA                         #
#################################################################


#################################################################
#                        DECRIPTOGRAFIA                         #
#################################################################
def decriptografar():
    print('método não implementado')
    pass


#################################################################
#                     FIM DECRIPTOGRAFIA                        #
#################################################################

#################################################################
#                          NAVEGAÇÃO                            #
#################################################################
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


#################################################################
#                      FIM NAVEGAÇÃO                            #
#################################################################


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
