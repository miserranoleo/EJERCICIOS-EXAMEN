#Ejercicio 7: Añadir Ítems a un Inventario
#Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.def agregar_item(inventario, item):

def agregar_item(inventario, item, cantidad):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero.")

    for i, (existente_item, existente_cantidad) in enumerate(inventario):
        if existente_item == item:
            nuevo_total = existente_cantidad + cantidad
            inventario[i] = (existente_item, nuevo_total)
            print(f"{cantidad} unidades de '{item}' añadidas al inventario. Total: {nuevo_total}.")
            return

    inventario.append((item, cantidad))
    print(f"{cantidad} unidades de '{item}' añadidas al inventario. Total: {cantidad}.")

# Ejemplo de uso:
inventario_actual = []
nueva_cantidad_espadas = int(input("Ingrese la cantidad de espadas a añadir al inventario: "))
nueva_cantidad_pociones = int(input("Ingrese la cantidad de pociones a añadir al inventario: "))
nueva_cantidad_escudos = int(input("Ingrese la cantidad de escudos a añadir al inventario: "))

try:
    agregar_item(inventario_actual, "espadas", nueva_cantidad_espadas)
    agregar_item(inventario_actual, "pociones", nueva_cantidad_pociones)
    agregar_item(inventario_actual, "escudos", nueva_cantidad_escudos)
except ValueError as e:
    print(f"Error: {e}")

print("Inventario actual:", inventario_actual)
