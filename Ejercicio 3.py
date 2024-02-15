#Ejercicio 4: Priorización de Tareas en un Videojuego
#Durante la planificación de un videojuego, se han acordado una serie de misiones con niveles de dificultad. Crea una estructura de cola con todas las misiones ordenadas por dificultad pero sin mostrar los números de dificultad.
from queue import PriorityQueue

class Mision:
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.dificultad = dificultad

    def __lt__(self, other):
        return self.dificultad < other.dificultad

# Crear una cola de prioridad
cola_misiones = PriorityQueue()

# Agregar las misiones a la cola con su respectiva dificultad usando la clase Mision
cola_misiones.put(Mision("Misión 1", 5))
cola_misiones.put(Mision("Misión 2", 3))
cola_misiones.put(Mision("Misión 3", 7))
cola_misiones.put(Mision("Misión 4", 2))
cola_misiones.put(Mision("Misión 5", 6))

# Mostrar las misiones sin los números de dificultad
while not cola_misiones.empty():
    mision = cola_misiones.get()
    print(f"{mision.nombre}")