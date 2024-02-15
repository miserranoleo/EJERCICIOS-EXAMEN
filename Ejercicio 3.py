#Ejercicio 3: Encontrar Palabras Comunes
#Dadas dos listas de palabras, genera una tercera lista con todas las palabras que se repitan en ambas listas, sin repetición en la nueva lista.
def encontrar_palabras_comunes(lista1, lista2):
    lista_comun = []
    
    for palabra1 in lista1:
        for palabra2 in lista2:
            if palabra1 == palabra2 and palabra1 not in lista_comun:
                lista_comun.append(palabra1)

    return lista_comun

# Ejemplo de uso
lista1 = ["hola", "mundo", "python", "programacion"]
lista2 = ["python", "programacion", "ejercicio", "hola"]

resultado = encontrar_palabras_comunes(lista1, lista2)
print(resultado)
