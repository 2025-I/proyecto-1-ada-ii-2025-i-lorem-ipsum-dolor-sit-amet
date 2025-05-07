from collections import defaultdict

def resolver_programacion_dinamica(empleados, relaciones, calificaciones):

    # Resuelve el problema de planificación de fiesta usando programación dinámica.

    # Construir el árbol a partir de la matriz de adyacencia
    grafo = defaultdict(list)
    es_hijo = [False] * empleados
    
    # Crear el grafo y detectar la raíz
    for i in range(empleados):
        for j in range(empleados):
            if relaciones[i][j] == 1:  # i es padre de j
                grafo[i].append(j)
                es_hijo[j] = True
    
    # Encontrar la raíz (nodo que no es hijo de ningún otro nodo)
    raiz = None
    for i in range(empleados):
        if not es_hijo[i]:
            if raiz is not None:
                print("Error: Se encontró más de una raíz en el árbol.")
                return [0] * empleados, 0
            raiz = i
    
    # Verificar que se haya encontrado exactamente una raíz
    if raiz is None:
        print("Error: No se encontró una raíz en el árbol.")
        return [0] * empleados, 0
    
    # Verificar si hay ciclos en el grafo
    visitado = [False] * empleados
    en_pila = [False] * empleados
    
    def tiene_ciclo(nodo):
        visitado[nodo] = True
        en_pila[nodo] = True
        
        for vecino in grafo[nodo]:
            if not visitado[vecino]:
                if tiene_ciclo(vecino):
                    return True
            elif en_pila[vecino]:
                return True
        
        en_pila[nodo] = False
        return False
    
    # Comprobar si hay ciclos comenzando desde la raíz
    if tiene_ciclo(raiz):
        print("Error: Se detectó un ciclo en el árbol. El problema no puede resolverse.")
        return [0] * empleados, 0
    
    # Memoización para almacenar los resultados
    memo_incluir = [-1] * empleados
    memo_excluir = [-1] * empleados
    
    # Función para calcular el puntaje usando programación dinámica
    def dp(nodo, incluir):
        if incluir:
            if memo_incluir[nodo] != -1:
                return memo_incluir[nodo]
            # Puntaje si incluimos el nodo
            puntaje = calificaciones[nodo]
            for hijo in grafo[nodo]:
                puntaje += dp(hijo, False)  # Solo podemos excluir a los hijos
            memo_incluir[nodo] = puntaje
            return puntaje
        else:
            if memo_excluir[nodo] != -1:
                return memo_excluir[nodo]
            # Puntaje si excluimos el nodo
            puntaje = 0
            for hijo in grafo[nodo]:
                puntaje += max(dp(hijo, True), dp(hijo, False))
            memo_excluir[nodo] = puntaje
            return puntaje
    
    # Calcular el puntaje máximo para la raíz
    max_puntaje = max(dp(raiz, True), dp(raiz, False))
    
    # Reconstruir la lista de invitados
    invitados = [0] * empleados
    
    def reconstruir(nodo, incluir):
        if incluir:
            invitados[nodo] = 1
            for hijo in grafo[nodo]:
                reconstruir(hijo, False)
        else:
            for hijo in grafo[nodo]:
                if dp(hijo, True) > dp(hijo, False):
                    reconstruir(hijo, True)
                else:
                    reconstruir(hijo, False)
    
    # Decidir si incluir o no la raíz
    if dp(raiz, True) > dp(raiz, False):
        reconstruir(raiz, True)
    else:
        reconstruir(raiz, False)
    
    # Retornar el vector de invitados y el puntaje total
    return invitados, max_puntaje

# Función para imprimir la estructura del grafo (útil para depuración)
def imprimir_grafo(grafo, empleados):
    print("Estructura del grafo:")
    for i in range(empleados):
        if i in grafo:
            print(f"Empleado {i} es jefe de: {grafo[i]}")
        else:
            print(f"Empleado {i} no tiene subordinados")