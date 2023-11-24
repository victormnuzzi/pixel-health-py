from time import sleep
import math
import re

# --------------------- Funções ---------------------

# Função para definir o tamanho do programa no printdo terminal
def tamProg(titulo='Aplicativo PixelHealth'):
    return len(titulo) * 3 # armazenando em uma variável o tamanho do título para formatação do menu

# Função de linha simples para estética
def linha(tam=tamProg(),caractere='-'):
    print(f'{caractere}' * tam)

# Função de sublinhado para estética
def inputSublinhado(frase):
    escolha = input(frase)
    linha(len(frase + str(escolha)))
    sleep(0.5)
    return escolha

# Função para "carregar" o menu
def aviso(frase='Carregando o Menu',menu='', tresPontos='... '):
    frase_aviso = f'{frase} {menu}{tresPontos}'
    print()
    print('\033[34m')
    centralizar(frase_aviso)
    linha(len(frase_aviso), '~')

    centralizar(frase_aviso)
    print(frase_aviso)

    centralizar(frase_aviso)
    linha(len(frase_aviso), '~')
    print('\033[m')
    print()
    sleep(0.5)

# Função para centralizar
def centralizar(frase='', tamanho=tamProg()):
    centralizar =  math.ceil((tamanho - len(frase)) / 2)
    print(' ' * centralizar, end="")

# Função de printar os menus
def printMenu(titulo="",opcoes={},tamanho=tamProg(), menu='Menu '):

    aviso(menu=titulo)

    print(f'\033[36m{f"{menu}{titulo}":^{tamanho}}\033[m')
    linha(tamanho)
    print()


    # Calcular a centralização dos items do menu
    frase_maior = ''

    for k, v in opcoes.items():
        frase_nova = f'[{k}] - {v}'

        if len(frase_nova) > len(frase_maior):
            frase_maior = frase_nova

    # Print do menu
    for k, v in opcoes.items():
        centralizar(frase_maior)
        print(f"[{k}] - {v}")
    print()
    linha(tamanho)

    # Verificando
    escolha_usuario = verificarOpcao(opcoes, titulo.upper())
    
    sleep(1)
    return escolha_usuario

# Tratamento de erro de int e verificar opção
def verificarOpcao(opcoes='', menu=''):

    validacao_input = False

    while not validacao_input:
    
        try:
            print('\033[33m')
            escolha_usuario = int(inputSublinhado("Escolha uma opção: "))
            print('\033[m')

            if escolha_usuario not in opcoes.keys():
                raise ValueError
            else: 
                validacao_input = True

        except:
            print("\033[31mPor favor, insira uma opção válida\033[m\n")

    # Opções
    match escolha_usuario:
        case "0":
            if menu == 'PRINCIPAL':
                print("Saindo do programa...\n")
                sleep(1)
                return escolha_usuario
        
            else:
                print("Voltando para o menu principal...\n")
                sleep(1)
                return escolha_usuario

        case _:

            return escolha_usuario
        
# Tratamento de erro de string
def tratarErroStr(string=''):
    validacao_input = False

    while not validacao_input:
        try:
            print('\033[33m')
            entrada_usuario = inputSublinhado(string)
            print('\033[m')

            # Tratamento de erro para string vazia
            if not entrada_usuario.strip():
                raise ValueError

            validacao_input = True

        except:
            print("\033[31mErro! A string não pode ser vazia\033[m\n")

    return entrada_usuario

# Validar email com REGEX
def validarEmail(email):
    padrao = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    if re.match(padrao, email):
        return True
    else:
        return False
