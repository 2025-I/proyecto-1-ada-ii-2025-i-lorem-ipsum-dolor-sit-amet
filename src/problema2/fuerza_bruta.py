# Implementación fuerza bruta para problema de planificación de fiesta

# Implementación fuerza bruta para problema de planificación de fiesta
"""
Solución de fuerza bruta para el problema 2: Planeando una fiesta de la compañía.
"""
from itertools import combinations

def es_conjunto_valido(conjunto, relaciones):
    """
    Verifica si un conjunto de empleados cumple con la restricción de que
    ningún invitado puede ser supervisor directo de otro invitado.
    
    Args:
        conjunto (list): Lista de índices de empleados invitados
        relaciones (list): Matriz de adyacencia que representa las relaciones de supervisión
    
    Returns:
        bool: True si el conjunto cumple las restricciones, False en caso contrario
    """
    for i in conjunto:
        for j in conjunto:
            if i != j and relaciones[i][j] == 1:  # i es supervisor directo de j
                return False
    
    return True

def resolver_fuerza_bruta(n, relaciones, calificaciones):
    """
    Resuelve el problema de la fiesta de la compañía utilizando fuerza bruta.
    
    El enfoque de fuerza bruta considera todos los posibles subconjuntos de
    empleados, verifica cuáles cumplen las restricciones y encuentra el que
    maximiza la suma de calificaciones.
    
    Args:
        n (int): Número de empleados
        relaciones (list): Matriz de adyacencia que representa las relaciones de supervisión
        calificaciones (list): Lista de calificaciones de convivencia
    
    Returns:
        tuple: (lista de invitados (0 o 1), puntuación total)
    """
    mejor_conjunto = []
    mejor_puntuacion = 0
    
    # Considerar todos los posibles subconjuntos de empleados
    for tamaño in range(1, n + 1):
        for conjunto in combinations(range(n), tamaño):
            if es_conjunto_valido(conjunto, relaciones):
                # Calcular la puntuación total de este conjunto
                puntuacion = sum(calificaciones[i] for i in conjunto)
                
                # Actualizar el mejor conjunto si encontramos uno mejor
                if puntuacion > mejor_puntuacion:
                    mejor_conjunto = conjunto
                    mejor_puntuacion = puntuacion
    
    # Convertir la solución a formato de vector de invitados
    invitados = [0] * n
    for i in mejor_conjunto:
        invitados[i] = 1
    
    return invitados, mejor_puntuacion