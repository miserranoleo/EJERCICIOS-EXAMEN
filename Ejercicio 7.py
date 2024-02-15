#Ejercicio 7: Añadir Ítems a un Inventario
#Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.def agregar_item(inventario, item):
def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError(f"El ítem '{item}' ya está en el inventario.")
    else:
        inventario.append(item)
        print(f"Ítem '{item}' añadido al inventario.")

# Ejemplo de uso:
inventario_actual = ["espada", "poción", "escudo"]
nuevo_item = "poción"
try:
    agregar_item(inventario_actual, nuevo_item)
except ValueError as e:
    print(f"Error: {e}")

print("Inventario actual:", inventario_actual)


