import random

def generar_numero():
    numeros_disponibles = list(range(1, 10))
    numero = []
    for _ in range(4):
        digito = random.choice(numeros_disponibles)
        numero.append(digito)
        numeros_disponibles.remove(digito)
    return numero

def evaluar_intentos(numero_generado, intento):
    fijas = 0
    picas = 0
    for i in range(4):
        if intento[i] == numero_generado[i]:
            fijas += 1
        elif intento[i] in numero_generado:
            picas += 1
    return fijas, picas

if __name__ == "__main__":
    numero_generado = generar_numero()
    intentos_restantes = 4
    print("Bienvenido al juego de adivinar el número!")
    print("Tienes 4 intentos para adivinar el número de 4 dígitos.")

    #Imprimir el numero generado aleatoriamente para probar el codigo
    print("El numero aleatorio es: ",numero_generado)
    while intentos_restantes > 0:
        intento = input("Ingresa un número de 4 dígitos sin repetir: ")
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print("Por favor ingresa un número válido de 4 dígitos sin repetir.")
            continue
        intento = [int(digito) for digito in intento]
        fijas, picas = evaluar_intentos(numero_generado, intento)
        print(f"Respuesta: Fijas {fijas} y picas {picas}")
        if fijas == 4:
            print("¡Felicidades, has adivinado el número!")
            break
        intentos_restantes -= 1
        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intentos.")
    else:
        print(f"Lo siento, has agotado tus intentos. El número era: {''.join(map(str, numero_generado))}")
