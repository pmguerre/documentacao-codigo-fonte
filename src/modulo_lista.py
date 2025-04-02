def filtrar_pares(lista_numeros):
    numeros = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            numeros.append(numero)
    return numeros


def calcular_frequencia(lista):
    frequencia = {}
    for item in lista:
        frequencia[item] = frequencia.get(item, 0) + 1
    return frequencia


def agrupar_por_tamanho(lista_strings):
    agrupado = {}
    for string in lista_strings:
        tamanho = len(string)
        if tamanho not in agrupado:
            agrupado[tamanho] = []
        agrupado[tamanho].append(string)
    return agrupado


if __name__ == "__main__":
    
    numeros = [1, 4, 7, 3, 8, 10, 24, 1, 5, 7, 10]
    strings = ['ola', 'mundo', 'maria', 'xutos', 'colaboração', 'a', 'e', 'xutos']
    
    print(filtrar_pares(numeros))
    print(calcular_frequencia(numeros))
    print(calcular_frequencia(strings))
    print(agrupar_por_tamanho(strings))