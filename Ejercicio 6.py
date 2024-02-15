#Ejercicio 6: Separar Personajes de Videojuegos
#Crea una función que tome una lista de personajes de videojuegos y devuelva dos listas ordenadas: la primera con personajes humanos y la segunda con personajes no humanos.

def separar_personajes(lista_personajes):
    personajes_humanos = []
    personajes_no_humanos = []

    for personaje in lista_personajes:
        tipo_personaje = input(f"¿Es {personaje} humano o no humano? (h/n): ").lower()
        if tipo_personaje == 'h':
            personajes_humanos.append(personaje)
        elif tipo_personaje == 'n':
            personajes_no_humanos.append(personaje)
        else:
            print(f"Opción no válida para {personaje}. Se ignorará.")

    personajes_humanos.sort()
    personajes_no_humanos.sort()

    return personajes_humanos, personajes_no_humanos

# Ejemplo de uso:
lista_personajes = ["Mario", "Sonic", "Master Chief", "Link", "Zelda", "Ganondorf"]
humanos, no_humanos = separar_personajes(lista_personajes)

print("Personajes humanos:", humanos)
print("Personajes no humanos:", no_humanos)
