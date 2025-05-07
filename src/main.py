# Punto de entrada principal del programa
import sys
from file_chooser import seleccionar_archivo
from problema1.fuerza_bruta import resolver_fuerza_bruta
from problema1.programacion_dinamica import resolver_programacion_dinamica
from problema1.voraz import palindroma_voraz

def main():
    # Elegir el archivo de entrada
    archivo = seleccionar_archivo()
    
    if not archivo:
        print("No se seleccionó ningún archivo. Saliendo...")
        sys.exit(1)
    
    # Seleccionar criterio de solución
    print("Seleccione el criterio de solución:")
    print("1. Fuerza Bruta")
    print("2. Programación Dinámica")
    print("3. Voraz")
    
    criterio = input("Opción (1/2/3): ").strip()
    
    # Leer las cadenas del archivo seleccionado
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    
    n = int(lineas[0].strip())
    cadenas = [linea.strip() for linea in lineas[1:n+1]]
    
    # Procesar las cadenas según el criterio seleccionado
    if criterio == '1':
        for cadena in cadenas:
            print(resolver_fuerza_bruta(cadena))
    elif criterio == '2':
        for cadena in cadenas:
            print(resolver_programacion_dinamica(cadena))
    elif criterio == '3':
        for cadena in cadenas:
            print(palindroma_voraz(cadena))
    else:
        print("Opción no válida. Saliendo...")
        sys.exit(1)

if __name__ == "__main__":
    main()
