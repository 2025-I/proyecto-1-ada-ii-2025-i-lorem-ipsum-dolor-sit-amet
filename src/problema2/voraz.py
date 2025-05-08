import heapq

def fiesta_voraz(relaciones, calificaciones):
    """
    Implementación voraz corregida para el problema 2
    
    Args:
        relaciones: Matriz de adyacencia (n x n) donde 1 indica relación supervisor-subordinado
        calificaciones: Lista de calificaciones de convivencia
        
    Returns:
        list: Vector de invitación (0/1) + suma total en última posición
    """
    n = len(calificaciones)
    invitados = set()
    total = 0
    
    # Max-heap usando valores negativos
    heap = [(-calificaciones[i], i) for i in range(n)]
    heapq.heapify(heap)
    
    while heap:
        _, empleado = heapq.heappop(heap)
        
        # Verificar restricciones más estrictas
        conflicto = False
        
        # Verificar si algún supervisor está invitado
        for supervisor in range(n):
            if relaciones[supervisor][empleado] == 1 and supervisor in invitados:
                conflicto = True
                break
                
        # Verificar si algún subordinado está invitado
        if not conflicto:
            for subordinado in range(n):
                if relaciones[empleado][subordinado] == 1 and subordinado in invitados:
                    conflicto = True
                    break
        
        if not conflicto:
            invitados.add(empleado)
            total += calificaciones[empleado]
    
    # Convertir a formato de salida
    resultado = [1 if i in invitados else 0 for i in range(n)]
    ##vector   = [1 if i in invitados else 0 for i in range(n)]
    ##return vector, total
    resultado.append(total)
    return resultado

def resolver_problema(matriz, calificaciones):
    """
    Función principal corregida
    
    Args:
        matriz: Matriz de adyacencia nxn
        calificaciones: Lista de calificaciones
        
    Returns:
        list: Vector de invitación (0/1) + suma total en última posición
    """
    # Eliminé la construcción del árbol que no se usaba correctamente
    return fiesta_voraz(matriz, calificaciones)