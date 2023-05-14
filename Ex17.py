'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triagulo retangulo, calcule e mostre o comprimento da hipotenusa'''

import math

def calcular_hipotenusa(cateto_oposto, cateto_adjacente):
    """
    Calcula o comprimento da hipotenusa de um triângulo retângulo dado os comprimentos
    dos catetos usando o teorema de Pitágoras.
    """
    return math.hypot(cateto_oposto, cateto_adjacente)

def validar_comprimento(valor):
    """
    Valida um valor de comprimento, verificando se é um número positivo.
    Se for válido, retorna o valor convertido para float.
    Caso contrário, lança uma exceção ValueError com uma mensagem de erro adequada.
    """
    try:
        valor_float = float(valor)
    except ValueError:
        raise ValueError("Valor inválido. Digite um número positivo.")
    if valor_float <= 0:
        raise ValueError("Valor inválido. O comprimento deve ser positivo.")
    return valor_float

def pedir_comprimento(nome_cateto):
    """
    Pede ao usuário o comprimento de um cateto, validando a entrada.
    Retorna o valor convertido para float.
    """
    while True:
        valor = input(f"Digite o comprimento do {nome_cateto}: ")
        try:
            valor = validar_comprimento(valor)
            return valor
        except ValueError as e:
            print(f"Erro: {e}")

def mostrar_resultado(cateto_oposto, cateto_adjacente, hipotenusa):
    """
    Mostra o resultado do cálculo dos comprimentos do triângulo retângulo,
    formatando uma mensagem com os valores dos catetos e da hipotenusa.
    """
    mensagem = f"Comprimento do cateto oposto: {cateto_oposto:.2f}\nComprimento do cateto adjacente: {cateto_adjacente:.2f}\nComprimento da hipotenusa: {hipotenusa:.2f}"
    print(mensagem)

def menu_principal():
    """
    Exibe o menu principal e pede a opção do usuário.
    """
    print("MENU PRINCIPAL")
    print("1. Calcular hipotenusa")
    print("2. Sair")
    while True:
        opcao = input("Digite sua opção: ")
        if opcao in ["1", "2"]:
            return opcao
        else:
            print("Opção inválida. Digite 1 ou 2.")

while True:
    # exibir o menu principal e pedir a opção do usuário
    opcao = menu_principal()

    if opcao == "1":
        # pedir o comprimento dos catetos
        cateto_oposto = pedir_comprimento("cateto oposto")
        cateto_adjacente = pedir_comprimento("cateto adjacente")

        # calcular a hipotenusa usando a função math.hypot
        hipotenusa = calcular_hipotenusa(cateto_oposto, cateto_adjacente)

        # mostrar o resultado com uma mensagem formatada
        mostrar_resultado(cateto_oposto, cateto_adjacente, hipotenusa)
    elif opcao == "2":
        # sair do programa
        print("Obrigado por usar o programa!")
        break
