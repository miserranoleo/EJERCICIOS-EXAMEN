#Ejercicio 7: Añadir Ítems a un Inventario
#Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.def agregar_item(inventario, item):
def agregar_item(inventario, item):
    try:
        cantidad = int(input(f"Ingrese la cantidad de '{item}' a añadir al inventario: "))
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
    except ValueError:
        print("Ingrese un número entero válido para la cantidad.")
        return

    for i, (existente_item, existente_cantidad) in enumerate(inventario):
        if existente_item == item:
            nuevo_total = existente_cantidad + cantidad
            inventario[i] = (existente_item, nuevo_total)
            print(f"{cantidad} unidades de '{item}' añadidas al inventario. Total: {nuevo_total}.")
            return

    inventario.append((item, cantidad))
    print(f"{cantidad} unidades de '{item}' añadidas al inventario. Total: {cantidad}.")

# Ejemplo de uso:
inventario_actual = [("espada", 2), ("poción", 5), ("escudo", 1)]
nuevo_item = input("Ingrese el nombre del nuevo ítem a añadir: ")

try:
    agregar_item(inventario_actual, nuevo_item)
except ValueError as e:
    print(f"Error: {e}")

print("Inventario actual:", inventario_actual)