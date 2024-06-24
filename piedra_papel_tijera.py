import random

# Función para obtener la jugada del ordenador de manera aleatoria
def obtener_jugada_ordenador():
    return random.choice(["piedra", "papel", "tijera"])

# Función para determinar el ganador de la partida
def determinar_ganador(jugada_usuario, jugada_ordenador):
    # Casos en los que hay empate
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    # Casos en los que gana el usuario
    elif (jugada_usuario == "piedra" and jugada_ordenador == "tijera") or \
         (jugada_usuario == "papel" and jugada_ordenador == "piedra") or \
         (jugada_usuario == "tijera" and jugada_ordenador == "papel"):
        return "Usuario"
    # Casos restantes: gana el ordenador
    else:
        return "Ordenador"

# Función para validar la jugada introducida por el usuario
def validar_jugada_usuario(jugada):
    return jugada in ["piedra", "papel", "tijera"]

# Variables para llevar la cuenta de las partidas
partidas_ganadas_usuario = 0
partidas_ganadas_ordenador = 0
empates = 0

# Bucle principal del juego
# Bucle principal del juego
while True: 
    ordenador = obtener_jugada_ordenador()
    print("Introduce piedra, papel o tijera:")
    usuario = input()
    # Validación de la jugada del usuario
    if not validar_jugada_usuario(usuario):
        print("Valor incorrecto. Introduce piedra, papel o tijera")
        continue

    print(f"Ordenador: {ordenador}")
    print(f"Usuario: {usuario}")

    # Determinación del ganador
    resultado = determinar_ganador(usuario, ordenador)
    if resultado == "Empate":
        empates += 1
    elif resultado == "Usuario":
        partidas_ganadas_usuario += 1
    else:
        partidas_ganadas_ordenador += 1

    print(resultado)

    # Pregunta al usuario si desea continuar jugando
    respuesta = None
    while respuesta not in ["s", "n"]:
        print("¿Quieres volver a jugar? (s/n)")
        respuesta = input().lower()  # Convertir la respuesta a minúsculas para manejar "S" y "N"
        if respuesta == "n":
            break
        elif respuesta != "s":
            print("Respuesta incorrecta. Introduce s o n")
    if respuesta == "n":
        break  # Rompe el bucle principal si la respuesta es "n"

# Resumen de resultados al final del juego
print("Partidas ganadas por el usuario:", partidas_ganadas_usuario)
print("Partidas ganadas por el ordenador:", partidas_ganadas_ordenador)
print("Empates:", empates)