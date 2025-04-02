"""
Utilitário de Operações Matemáticas, Texto e Listas
---------------------------------------------------

Este módulo contém o programa principal que oferece um menu interativo
para executar diversas operações em matemática, manipulação de texto e
operações com listas.

O programa apresenta um menu principal e submenus que permitem ao
utilizador selecionar diferentes funcionalidades implementadas nos
módulos importados.

.. note::
    Este programa é um exemplo de como organizar um código Python
    em modulos, permitindo a reutilização de funções em diferentes
    contextos.

.. warning::
    Este código é apenas um exemplo e não deve ser utilizado em
    produção sem as devidas validações e tratamento de exceções.

:Autor: Pedro Guerreiro
:Data: 1 de abril de 2025
:Versão: 1.0
"""

import modulo_lista
import modulo_matematica
import modulo_texto


def pedir_lista_floats(mensagem):
    """
    Solicita ao utilizador uma lista de números decimais.

    A função apresenta uma mensagem ao utilizador e espera que este
    insira uma sequência de números separados por vírgula. Cada valor
    é convertido para float.

    :param mensagem: Texto a apresentar ao utilizador para solicitar a entrada
    :type mensagem: str
    :return: Lista de números decimais inseridos pelo utilizador
    :rtype: list[float]

    :raise ValueError: Se algum dos valores inseridos não puder ser
                        convertido para float

    Por exemplo:

    >>> pedir_lista_floats("Digite valores: ")
    Digite valores: 1.5,2.7,3.9
    [1.5, 2.7, 3.9]
    """
    valores = input(mensagem)
    lista = []
    for valor in valores.split(","):
        lista.append(float(valor))
    return lista


def pedir_lista_inteiros(mensagem):
    """
    Solicita ao utilizador uma lista de números inteiros.

    A função apresenta uma mensagem ao utilizador e espera que este
    insira uma sequência de números separados por vírgula. Cada valor
    é convertido para int.

    :param mensagem: Texto a apresentar ao utilizador para solicitar a entrada
    :type mensagem: str
    :return: Lista de números inteiros inseridos pelo utilizador
    :rtype: list[int]

    :raises ValueError: Se algum dos valores inseridos não puder ser
                       convertido para int

    Por exemplo:

    >>> pedir_lista_inteiros("Digite valores: ")
    Digite valores: 1,2,3
    [1, 2, 3]
    """
    valores = input(mensagem)
    lista = []
    for valor in valores.split(","):
        lista.append(int(valor))
    return lista


def pedir_lista(mensagem):
    """
    Solicita ao utilizador uma lista de strings.

    A função apresenta uma mensagem ao utilizador e espera que este
    insira uma sequência de valores separados por vírgula.

    :param mensagem: Texto a apresentar ao utilizador para solicitar a entrada
    :type mensagem: str
    :return: Lista de strings inseridas pelo utilizador
    :rtype: list[str]

    Por exemplo:

    >>> pedir_lista("Digite palavras: ")
    Digite palavras: olá,mundo,python
    ['olá', 'mundo', 'python']
    """
    valores = input(mensagem)
    lista = []
    for valor in valores.split(","):
        lista.append(valor)
    return lista


def menu():
    """
    Apresenta o menu principal e processa a escolha do utilizador.

    A função exibe as opções disponíveis e valida se a escolha está
    dentro do intervalo permitido.

    :return: Número inteiro correspondente à opção escolhida
    :rtype: int

    Por exemplo:

    >>> menu()
    Escolha uma opção:
    1. Operações Matemáticas
    2. Operações com Texto
    3. Operações com Listas
    4. Sair
    Digite a opção desejada: 1
    1
    """
    while True:
        print("Escolha uma opção:")
        print("1. Operações Matemáticas")
        print("2. Operações com Texto")
        print("3. Operações com Listas")
        print("4. Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao < "1" or opcao > "4":
            print("Opção inválida. Tente novamente.\n")
        else:
            return int(opcao)


def menu_matematica():
    """
    Apresenta o submenu de operações matemáticas e processa a escolha.

    A função exibe as operações matemáticas disponíveis e valida se
    a escolha está dentro do intervalo permitido.

    :return: Número inteiro correspondente à opção escolhida
    :rtype: int

    Por exemplo:

    >>> menu_matematica()
    Operações Matemáticas:
    1. Média Ponderada
    2. Desvio Padrão
    3. Conversão de Temperatura
    Digite a opção desejada: 1
    1
    """
    while True:
        print("Operações Matemáticas:")
        print("1. Média Ponderada")
        print("2. Desvio Padrão")
        print("3. Conversão de Temperatura")
        opcao = input("Digite a opção desejada: ")
        if opcao < "1" or opcao > "3":
            print("Opção inválida. Tente novamente.\n")
        else:
            return int(opcao)


def menu_texto():
    """
    Apresenta o submenu de operações com texto e processa a escolha.

    A função exibe as operações de texto disponíveis e valida se
    a escolha está dentro do intervalo permitido.

    :return: Número inteiro correspondente à opção escolhida
    :rtype: int

    Por exemplo:

    >>> menu_texto()
    Operações com Texto:
    1. Contar Vogais
    2. Gerar Acrônimo
    3. Criptografia César
    Digite a opção desejada: 2
    2
    """
    while True:
        print("Operações com Texto:")
        print("1. Contar Vogais")
        print("2. Gerar Acrônimo")
        print("3. Criptografia César")
        opcao = input("Digite a opção desejada: ")
        if opcao < "1" or opcao > "3":
            print("Opção inválida. Tente novamente.\n")
        else:
            return int(opcao)


def menu_lista():
    """
    Apresenta o submenu de operações com listas e processa a escolha.

    A função exibe as operações de lista disponíveis e valida se
    a escolha está dentro do intervalo permitido.

    :return: Número inteiro correspondente à opção escolhida
    :rtype: int

    Por exemplo:

    >>> menu_lista()
    Operações com Listas:
    1. Filtrar Pares
    2. Calcular Frequência
    3. Agrupar por Tamanho
    Digite a opção desejada: 1
    1
    """
    while True:
        print("Operações com Listas:")
        print("1. Filtrar Pares")
        print("2. Calcular Frequência")
        print("3. Agrupar por Tamanho")
        opcao = input("Digite a opção desejada: ")
        if opcao < "1" or opcao > "3":
            print("Opção inválida. Tente novamente.\n")
        else:
            return int(opcao)


def main():
    """
    Função principal que controla o fluxo do programa.

    Esta função apresenta o menu principal e direciona para os submenus
    baseando-se na escolha do utilizador. Executa as operações
    solicitadas chamando as funções dos módulos importados com os
    parâmetros apropriados.

    :return: None
    :rtype: NoneType

    Por exemplo:

    >>> main()
    # Inicia o programa interativo com menus
    """
    while True:
        opcao_principal = menu()

        if opcao_principal == 1:
            opcao_matematica = menu_matematica()

            if opcao_matematica == 1:
                notas = pedir_lista_floats("Digite as notas separadas por vírgula: ")
                pesos = pedir_lista_floats("Digite os pesos separados por vírgula: ")
                print(modulo_matematica.calcular_media_ponderada(notas, pesos))

            elif opcao_matematica == 2:
                numeros = pedir_lista_floats("Digite os números separados por vírgula: ")
                print(modulo_matematica.calcular_desvio_padrao(numeros))

            elif opcao_matematica == 3:
                temperatura = float(input("Digite a temperatura: "))
                escala_origem = input("Digite a escala original (C/F/K): ").upper()
                escala_destino = input("Digite a escala de destino (C/F/K): ").upper()
                print(modulo_matematica.converter_temperatura(temperatura, escala_origem, escala_destino))

        elif opcao_principal == 2:
            opcao_texto = menu_texto()

            if opcao_texto == 1:
                texto = input("Digite o texto: ")
                print(modulo_texto.contar_vogais(texto))

            elif opcao_texto == 2:
                texto = input("Digite o texto: ")
                print(modulo_texto.gerar_acronimo(texto))

            elif opcao_texto == 3:
                texto = input("Digite o texto: ")
                deslocamento = int(input("Digite o deslocamento: "))
                print(modulo_texto.criptografar_cesar(texto, deslocamento))

        elif opcao_principal == 3:
            opcao_lista = menu_lista()

            if opcao_lista == 1:
                lista = pedir_lista_inteiros("Digite os números separados por vírgula: ")
                print(modulo_lista.filtrar_pares(lista))

            elif opcao_lista == 2:
                lista = pedir_lista("Digite a lista de itens separados por vírgula: ")
                print(modulo_lista.calcular_frequencia(lista))

            elif opcao_lista == 3:
                lista = pedir_lista("Digite a lista de strings separados por vírgula: ")
                print(modulo_lista.agrupar_por_tamanho(lista))

        elif opcao_principal == 4:
            break


if __name__ == "__main__":
    main()