def contar_vogais(texto):
    vogais = "aeiou"
    quantidade = 0
    for caractere in texto.lower():
        if caractere in vogais:
            quantidade += 1
    return quantidade


def gerar_acronimo(texto):
    palavras = texto.split()
    acronimo = ""
    for palavra in palavras:
        acronimo += palavra[0].upper()
    return acronimo


def criptografar_cesar(texto, deslocamento):
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            novo_caractere = chr((ord(caractere) - base + deslocamento) % 26 + base)
        else:
            novo_caractere = caractere
        resultado += novo_caractere
    return resultado


if __name__ == "__main__":
    
    mensagem = "As armas e os barões assinalados,"
    print(contar_vogais(mensagem))
    print(gerar_acronimo(mensagem))
    cifrado = criptografar_cesar(mensagem, 3)
    print(cifrado)
    print(criptografar_cesar(cifrado, -3))