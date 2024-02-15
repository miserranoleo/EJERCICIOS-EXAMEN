#Ejercicio 5: Descomposición de Dirección IP
#Crea un script que tome una dirección IP como argumento y la descomponga en sus cuatro octetos, mostrándolos línea a línea.

import sys
import re

def descomponer_ip(direccion_ip):
    octetos = direccion_ip.split('.')
    if len(octetos) == 4:
        for i, octeto in enumerate(octetos):
            print(f"Octeto {i + 1}: {octeto}")
    else:
        print("La dirección IP no es válida.")

def validar_ip(direccion_ip):
    patron_ip = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if patron_ip.match(direccion_ip):
        print("La dirección IP es válida.")
    else:
        print("La dirección IP no es válida.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        direccion_ip_argumento = sys.argv[1]
        print("Descomposición de dirección IP proporcionada como argumento:")
        descomponer_ip(direccion_ip_argumento)
    else:
        direccion_ip_manual = input("Ingresa una dirección IP: ")
        print("\nDescomposición de dirección IP ingresada manualmente:")
        descomponer_ip(direccion_ip_manual)

        print("\nValidación de la dirección IP:")
        validar_ip(direccion_ip_manual)
