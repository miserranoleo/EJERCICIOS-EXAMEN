#Ejercicio 1: Extracción de Información de una Receta
#Al extraer texto de un sitio web de recetas, obtuviste una cadena de texto corrupta y al revés. Parece contener el nombre de una receta y la cantidad de calorías. Formatea la cadena para conseguir una estructura como la siguiente:
#La receta de [Nombre de la receta] contiene [Número] calorías. 
#Ayuda:
#Para voltear una cadena rápidamente utilizando slicing: cadena[::-1]

def reverse_string(string):
    return string[::-1]

def extract_recipe_info(string):
    reversed_string = reverse_string(string)
    nombre_receta = reversed_string.split()[1][::-1]
    calorias = reversed_string.split()[0][::-1]
    resultado = f"La receta de {nombre_receta} contiene {calorias} calorías."
    return resultado

def main():
    cadena = input("Ingrese el nombre de la receta seguido del numero de calorias: ")
    resultado = extract_recipe_info(cadena)
    print(resultado)

if __name__ == "__main__":
    main()


