def cifrar_cesar(texto, desplazamiento):
    texto = texto.upper()
    texto_cifrado_cesar = ""
    for caracter in texto:
        if caracter.isalpha():
            posicion_original = ord(caracter) - ord('A')
            nueva_posicion = (posicion_original + desplazamiento-1) % 26
            nuevo_caracter = chr(nueva_posicion + ord('A'))
            texto_cifrado_cesar += nuevo_caracter
        else:
            texto_cifrado_cesar += caracter
    return texto_cifrado_cesar

def cifrar_vigenere(texto, clave):
    texto = texto.upper()
    texto_cifrado_vigenere = ""
    clave_repetida = clave * (len(texto) // len(clave)) + clave[:len(texto) % len(clave)]
    for i in range(len(texto)):
        if texto[i].isalpha():
            if texto[i].islower():
                nuevo_caracter = chr(((ord(texto[i]) - 97 + ord(clave_repetida[i]) - 97) % 26) + 97)
            else:
                nuevo_caracter = chr(((ord(texto[i]) - 65 + ord(clave_repetida[i]) - 65) % 26) + 65)
            texto_cifrado_vigenere += nuevo_caracter
        else:
            texto_cifrado_vigenere += texto[i]
    return texto_cifrado_vigenere

if __name__ == "__main__":
    texto_original = input("Ingresa el texto a cifrar: ")
    desplazamiento = 3  # Desplazamiento de 3 posiciones a la derecha
    texto_cifrado_cesar = cifrar_cesar(texto_original, desplazamiento)
    print("Texto cifrado cesar:", texto_cifrado_cesar)
    
    clave = texto_cifrado_cesar
    texto_cifrado_vigenere = cifrar_vigenere(texto_original, clave)
    print("Texto cifrado vigenere:", texto_cifrado_vigenere)

