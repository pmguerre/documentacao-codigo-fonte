def calcular_media_ponderada(notas, pesos):
    if len(notas) != len(pesos):
        msg = "A quantidade de notas deve ser igual à quantidade de pesos"
        raise ValueError(msg)
    soma_ponderada = 0
    for nota, peso in zip(notas, pesos):
        soma_ponderada += nota * peso
    soma_pesos = sum(pesos)
    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")
    return soma_ponderada / soma_pesos


def calcular_desvio_padrao(numeros):
    n = len(numeros)
    if n < 2:
        raise ValueError("A lista deve conter pelo menos dois números.")
    media = sum(numeros) / n
    numerador = 0
    for x in numeros:
        numerador += (x - media) ** 2
    desvio_padrao = (numerador / (n - 1)) ** 0.5
    return desvio_padrao


def converter_temperatura(temperatura, escala_origem, escala_destino):
    if escala_origem == "C" and escala_destino == "F":
        return (temperatura * 9/5) + 32
    elif escala_origem == "C" and escala_destino == "K":
        return temperatura + 273.15
    elif escala_origem == "F" and escala_destino == "C":
        return (temperatura - 32) * 5/9
    elif escala_origem == "F" and escala_destino == "K":
        return (temperatura + 459.67) * 5/9
    elif escala_origem == "K" and escala_destino == "C":
        return temperatura - 273.15
    elif escala_origem == "K" and escala_destino == "F":
        return (temperatura * 9/5) - 459.67
    else:
        raise ValueError("Escalas inválidas ou conversão não suportada.")


if __name__ == '__main__':

    a = [10, 15, 20]
    b = [0.5, 0.25, 0.25]

    print(calcular_media_ponderada(a,[1,1]))
    print(calcular_desvio_padrao(a))
    print(converter_temperatura(32, "C", "F"))