#Ejercicio 2: Cálculo de Interés Compuesto
#Crea un programa que calcule el interés compuesto.
#Guarda en una variable capital_inicial el valor 1000.
#Lee por pantalla la tasa de interés anual, que deberá estar entre 1% y 10%.
#Eleva la tasa de interés a sí misma por el número de años (por ejemplo, 5 años).
#Multiplica el capital_inicial por el resultado anterior en sí mismo.
#Muestra el capital final.
def calcular_interes_compuesto(capital_inicial, tasa_anual, años, capitalizacion_anual=1):
    if not (1 <= tasa_anual <= 10):
        raise ValueError("La tasa de interés anual debe estar entre 1% y 10%.")

    if capitalizacion_anual <= 0 or type(capitalizacion_anual) != int:
        raise ValueError("La frecuencia de capitalización anual debe ser un número entero positivo.")

    tasa_decimal = tasa_anual / 100
    tasa_periodo = tasa_decimal / capitalizacion_anual

    capital_final = capital_inicial * (1 + tasa_periodo) ** (años * capitalizacion_anual)

    return capital_final

def main():
    try:
        capital_inicial = float(input("Ingrese el capital inicial: $"))
        tasa_anual = float(input("Ingrese la tasa de interés anual (entre 1 y 10): "))
        años = int(input("Ingrese el número de años: "))
        capitalizacion_anual = int(input("Ingrese la frecuencia de capitalización anual (por ejemplo, 1 para anual, 12 para mensual): "))

        capital_final = calcular_interes_compuesto(capital_inicial, tasa_anual, años, capitalizacion_anual)
        print(f"\nEl capital final después de {años} años es: ${capital_final:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
