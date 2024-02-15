#Ejercicio 3: Encontrar Palabras Comunes
#Dadas dos listas de palabras, genera una tercera lista con todas las palabras que se repitan en ambas listas, sin repetición en la nueva lista.
def encontrar_palabras_comunes(lista1, lista2):
    lista_comun = set()

    for palabra1 in lista1:
        if palabra1 in lista2 and palabra1 not in lista_comun:
            lista_comun.add(palabra1)

    return list(lista_comun)

def obtener_lista_personalizada():
    try:
        entrada = input("Ingrese palabras separadas por espacios: ")
        lista_personalizada = entrada.split()
        return lista_personalizada
    except Exception as e:
        print(f"Error al procesar la entrada: {e}")
        return []

# Obtener listas personalizadas
print("Ingrese la primera lista:")
lista1 = obtener_lista_personalizada()

print("\nIngrese la segunda lista:")
lista2 = obtener_lista_personalizada()

# Encontrar palabras comunes
resultado = encontrar_palabras_comunes(lista1, lista2)

# Mostrar resultado
if resultado:
    print("\nPalabras comunes en ambas listas (sin repetición):")
    print(resultado)
else:
    print("\nNo hay palabras comunes en las listas proporcionadas.")

