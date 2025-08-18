import random    
numero_secreto = random.randint(1, 100) 
intentos_maximos = 5 

print("Juego de adivinanza xd")
print("Estoy pensando en un número del 1 al 100.")
print(f"Tienes {intentos_maximos} intentos para adivinarlo.\n")


for intento in range(1, intentos_maximos + 1):
    try:
        adivinanza = int(input(f"Intento {intento}: Ingresa tu número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if adivinanza == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intento} intento(s).")
        break
    elif adivinanza < numero_secreto:
        print("Pista: El número es mayor.\n")
    else:
        print("Pista: El número es menor.\n")

else:
    print(f"\nLo siento, has agotado tus {intentos_maximos} intentos.")
    print(f"El número secreto era: {numero_secreto}")