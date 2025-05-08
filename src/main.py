# Punto de entrada principal del programa
import sys
from file_chooser import seleccionar_archivo

# Importaciones problema 1
from problema1.fuerza_bruta import resolver_fuerza_bruta
from problema1.programacion_dinamica import resolver_programacion_dinamica as resolver_p1_dinamica
from problema1.voraz import resolver_voraz as palindroma_voraz

# Importaciones problema 2
from problema2.programacion_dinamica import resolver_programacion_dinamica as resolver_p2_dinamica
from problema2.fuerza_bruta import resolver_fuerza_bruta as resolver_p2_fuerza_bruta
from problema2.voraz import resolver_problema as resolver_p2_voraz

def cargar_datos_p1(archivo):
    """Carga los datos del archivo para el problema 1 (subsecuencias palindrómicas)."""
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    
    n = int(lineas[0].strip())
    return [linea.strip() for linea in lineas[1:n+1]]

def cargar_datos_p2(archivo):
    """Carga los datos del archivo para el problema 2 (planificación de fiesta)."""
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    
    n_casos = int(lineas[0].strip())
    casos = []
    linea_actual = 1
    
    for _ in range(n_casos):
        empleados = int(lineas[linea_actual].strip())
        linea_actual += 1
        
        relaciones = []
        for i in range(empleados):
            fila = [int(x) for x in lineas[linea_actual].strip().split()]
            relaciones.append(fila)
            linea_actual += 1
        
        calificaciones = [int(x) for x in lineas[linea_actual].strip().split()]
        linea_actual += 1
        
        casos.append((empleados, relaciones, calificaciones))
    
    return casos

def procesar_p1(cadenas, algoritmo):
    """Procesa cada cadena con el algoritmo seleccionado para el problema 1."""
    for cadena in cadenas:
        print(algoritmo(cadena))

def procesar_p2(casos, algoritmo):
    """Procesa cada caso con el algoritmo seleccionado para el problema 2."""
    for empleados, relaciones, calificaciones in casos:
        invitados, puntaje = algoritmo(empleados, relaciones, calificaciones)
        # Formato de salida: vector de invitados seguido del puntaje total
        print(' '.join(map(str, invitados)) + ' ' + str(puntaje))

def main():
    # Elegir el archivo de entrada
    archivo = seleccionar_archivo()
    
    if not archivo:
        print("No se seleccionó ningún archivo. Saliendo...")
        sys.exit(1)
    
    # Seleccionar el problema
    print("\nSeleccione el problema a resolver:")
    print("1. Subsecuencias palindrómicas")
    print("2. Planificación de fiesta")
    
    problema = input("Problema (1/2): ").strip()
    
    if problema not in ["1", "2"]:
        print("Problema no válido. Saliendo...")
        sys.exit(1)
    
    # Seleccionar criterio de solución
    print("\nSeleccione el criterio de solución:")
    print("1. Fuerza Bruta")
    print("2. Programación Dinámica")
    print("3. Voraz")
    
    criterio = input("Opción (1/2/3): ").strip()
    
    if criterio not in ["1", "2", "3"]:
        print("Criterio no válido. Saliendo...")
        sys.exit(1)
    
    # Procesar según el problema seleccionado
    if problema == "1":
        # Mapeo de algoritmos para problema 1
        algoritmos = {
            "1": resolver_fuerza_bruta if 'resolver_fuerza_bruta' in globals() else None,
            "2": resolver_p1_dinamica,
            "3": palindroma_voraz
        }
        
        algoritmo = algoritmos[criterio]
        if algoritmo is None:
            print(f"El algoritmo para el criterio {criterio} no está implementado para el problema 1. Saliendo...")
            sys.exit(1)
        
        cadenas = cargar_datos_p1(archivo)
        procesar_p1(cadenas, algoritmo)
        
    else:  # problema == "2"
        # Mapeo de algoritmos para problema 2
        algoritmos = {
            "1": resolver_p2_fuerza_bruta if 'resolver_p2_fuerza_bruta' in globals() else None,
            "2": resolver_p2_dinamica,
            "3": resolver_p2_voraz if 'resolver_p2_voraz' in globals() else None
        }
        
        algoritmo = algoritmos[criterio]
        if algoritmo is None:
            print(f"El algoritmo para el criterio {criterio} no está implementado para el problema 2. Saliendo...")
            sys.exit(1)
        
        casos = cargar_datos_p2(archivo)
        procesar_p2(casos, algoritmo)

if __name__ == "__main__":
    main()
